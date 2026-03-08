"""
Cloud fine-tuning and inference management.

Manages the complete lifecycle of fine-tuning models on cloud platforms:
1. Upload training data (JSONL)
2. Create fine-tuning job
3. Poll until complete
4. Deploy for inference
5. Return an endpoint config compatible with UnifiedAPIClient

Supported platforms:
- Together AI: Fine-tune API + serverless inference
- HuggingFace: Training API + Inference Endpoints
- RunPod: Serverless vLLM + custom model deployment
- OpenAI: Fine-tuning API (for comparison testing)

These are designed to work when API keys are available.
All methods handle missing credentials gracefully.
"""

from __future__ import annotations

import asyncio
import json
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from pydantic import BaseModel


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

class CloudConfig(BaseModel):
    """Base configuration for cloud platforms."""
    api_key: str = ""
    timeout: float = 600  # 10 min timeout for polling
    poll_interval: float = 30  # Check every 30s


class TogetherConfig(CloudConfig):
    """Together AI configuration."""
    base_url: str = "https://api.together.xyz/v1"
    base_model: str = "meta-llama/Llama-3.1-8B-Instruct"
    n_epochs: int = 3
    learning_rate: float = 1e-5
    batch_size: int = 4
    lora: bool = True
    lora_r: int = 16
    suffix: str = "safety-redteam"


class HuggingFaceConfig(CloudConfig):
    """HuggingFace configuration."""
    base_url: str = "https://huggingface.co/api"
    base_model: str = "mistralai/Mistral-7B-Instruct-v0.3"
    namespace: str = ""  # HF username or org
    instance_type: str = "gpu.a10g.xlarge"  # For Inference Endpoints
    region: str = "us-east-1"
    framework: str = "pytorch"


class RunPodConfig(CloudConfig):
    """RunPod configuration."""
    base_url: str = "https://api.runpod.ai/v2"
    gpu_type: str = "NVIDIA A100 80GB"
    template_id: str = ""  # vLLM template
    volume_id: str = ""  # Persistent storage
    max_workers: int = 1


class OpenAIFinetuneConfig(CloudConfig):
    """OpenAI fine-tuning configuration."""
    base_url: str = "https://api.openai.com/v1"
    base_model: str = "gpt-4o-mini-2024-07-18"
    n_epochs: int | str = "auto"
    suffix: str = "safety-redteam"


# ---------------------------------------------------------------------------
# Job Status
# ---------------------------------------------------------------------------

@dataclass
class FinetuneJob:
    """Represents a fine-tuning job on any platform."""
    platform: str
    job_id: str
    status: str = "pending"  # pending, running, completed, failed
    base_model: str = ""
    fine_tuned_model: str = ""
    created_at: float = 0.0
    completed_at: float = 0.0
    error: str = ""
    metrics: dict[str, Any] = field(default_factory=dict)
    endpoint_config: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "platform": self.platform,
            "job_id": self.job_id,
            "status": self.status,
            "base_model": self.base_model,
            "fine_tuned_model": self.fine_tuned_model,
            "created_at": self.created_at,
            "completed_at": self.completed_at,
            "error": self.error,
            "metrics": self.metrics,
            "endpoint_config": self.endpoint_config,
        }

    @property
    def is_complete(self) -> bool:
        return self.status == "completed"

    @property
    def is_failed(self) -> bool:
        return self.status == "failed"

    @property
    def duration_minutes(self) -> float:
        if self.completed_at and self.created_at:
            return round((self.completed_at - self.created_at) / 60, 1)
        return 0.0


# ---------------------------------------------------------------------------
# Together AI Client
# ---------------------------------------------------------------------------

class TogetherFinetuneClient:
    """Manage fine-tuning on Together AI.

    Together AI provides:
    - Fine-tuning API for LoRA/full fine-tuning
    - Automatic deployment of fine-tuned models
    - Serverless inference (pay per token)
    """

    def __init__(self, config: TogetherConfig | None = None):
        self.config = config or TogetherConfig()

    async def upload_dataset(self, file_path: Path) -> str:
        """Upload a JSONL training file to Together AI.

        Returns the file ID for use in fine-tuning.
        """
        import httpx

        async with httpx.AsyncClient(timeout=120) as client:
            with open(file_path, "rb") as f:
                resp = await client.post(
                    f"{self.config.base_url}/files",
                    headers={"Authorization": f"Bearer {self.config.api_key}"},
                    files={"file": (file_path.name, f, "application/jsonl")},
                    data={"purpose": "fine-tune"},
                )
                resp.raise_for_status()
                return resp.json()["id"]

    async def create_finetune(
        self, training_file_id: str
    ) -> FinetuneJob:
        """Create a fine-tuning job on Together AI."""
        import httpx

        payload = {
            "model": self.config.base_model,
            "training_file": training_file_id,
            "n_epochs": self.config.n_epochs,
            "learning_rate": self.config.learning_rate,
            "batch_size": self.config.batch_size,
            "suffix": self.config.suffix,
        }
        if self.config.lora:
            payload["training_type"] = {"type": "Lora", "lora_r": self.config.lora_r}

        async with httpx.AsyncClient(timeout=60) as client:
            resp = await client.post(
                f"{self.config.base_url}/fine-tunes",
                headers={
                    "Authorization": f"Bearer {self.config.api_key}",
                    "Content-Type": "application/json",
                },
                json=payload,
            )
            resp.raise_for_status()
            data = resp.json()

            return FinetuneJob(
                platform="together",
                job_id=data["id"],
                status="pending",
                base_model=self.config.base_model,
                created_at=time.time(),
            )

    async def poll_status(self, job: FinetuneJob) -> FinetuneJob:
        """Poll the status of a fine-tuning job."""
        import httpx

        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.get(
                f"{self.config.base_url}/fine-tunes/{job.job_id}",
                headers={"Authorization": f"Bearer {self.config.api_key}"},
            )
            resp.raise_for_status()
            data = resp.json()

            status = data.get("status", "unknown")
            if status in ("completed", "succeeded"):
                job.status = "completed"
                job.fine_tuned_model = data.get("output_name", data.get("fine_tuned_model", ""))
                job.completed_at = time.time()
                job.metrics = data.get("training_metrics", {})
                job.endpoint_config = self._make_endpoint_config(job.fine_tuned_model)
            elif status in ("failed", "error", "cancelled"):
                job.status = "failed"
                job.error = data.get("error", "Unknown error")
            else:
                job.status = "running"

            return job

    async def wait_for_completion(self, job: FinetuneJob) -> FinetuneJob:
        """Poll until the job completes or times out."""
        start = time.time()
        while time.time() - start < self.config.timeout:
            job = await self.poll_status(job)
            if job.is_complete or job.is_failed:
                return job
            await asyncio.sleep(self.config.poll_interval)

        job.status = "failed"
        job.error = f"Timed out after {self.config.timeout}s"
        return job

    async def run_full_pipeline(self, training_file: Path) -> FinetuneJob:
        """Upload data, create job, wait for completion.

        Returns a FinetuneJob with endpoint_config ready for inference.
        """
        file_id = await self.upload_dataset(training_file)
        job = await self.create_finetune(file_id)
        return await self.wait_for_completion(job)

    def _make_endpoint_config(self, model_name: str) -> dict[str, Any]:
        """Create endpoint config compatible with UnifiedAPIClient."""
        return {
            "name": f"together-{self.config.suffix}",
            "provider": "together",
            "base_url": "https://api.together.xyz/v1",
            "api_key": self.config.api_key,
            "model": model_name,
            "enabled": True,
        }

    def run_full_pipeline_sync(self, training_file: Path) -> FinetuneJob:
        """Synchronous wrapper."""
        return asyncio.run(self.run_full_pipeline(training_file))


# ---------------------------------------------------------------------------
# HuggingFace Client
# ---------------------------------------------------------------------------

class HuggingFaceFinetuneClient:
    """Manage fine-tuning and deployment on HuggingFace.

    Uses HuggingFace's:
    - AutoTrain for fine-tuning
    - Inference Endpoints for deployment
    """

    def __init__(self, config: HuggingFaceConfig | None = None):
        self.config = config or HuggingFaceConfig()

    async def upload_dataset(
        self, file_path: Path, repo_name: str = "safety-redteam-data"
    ) -> str:
        """Upload training data to a HuggingFace dataset repo.

        Returns the dataset repo ID (namespace/repo_name).
        """
        import httpx

        namespace = self.config.namespace or "user"
        repo_id = f"{namespace}/{repo_name}"

        # Create repo if needed
        async with httpx.AsyncClient(timeout=60) as client:
            await client.post(
                f"{self.config.base_url}/repos/create",
                headers={"Authorization": f"Bearer {self.config.api_key}"},
                json={
                    "type": "dataset",
                    "name": repo_name,
                    "private": True,
                },
            )

            # Upload file
            with open(file_path, "rb") as f:
                await client.put(
                    f"{self.config.base_url}/repos/{repo_id}/upload/train.jsonl",
                    headers={"Authorization": f"Bearer {self.config.api_key}"},
                    content=f.read(),
                )

        return repo_id

    async def create_inference_endpoint(
        self, model_id: str, endpoint_name: str = "safety-redteam"
    ) -> FinetuneJob:
        """Deploy a model to a HuggingFace Inference Endpoint."""
        import httpx

        namespace = self.config.namespace or "user"

        payload = {
            "name": endpoint_name,
            "model": {
                "repository": model_id,
                "framework": self.config.framework,
                "task": "text-generation",
            },
            "provider": {
                "region": self.config.region,
                "vendor": "aws",
            },
            "compute": {
                "instanceType": self.config.instance_type,
                "scaling": {"minReplica": 0, "maxReplica": 1},
            },
            "type": "protected",
        }

        async with httpx.AsyncClient(timeout=60) as client:
            resp = await client.post(
                f"https://api.endpoints.huggingface.cloud/v2/endpoint/{namespace}",
                headers={
                    "Authorization": f"Bearer {self.config.api_key}",
                    "Content-Type": "application/json",
                },
                json=payload,
            )
            resp.raise_for_status()
            data = resp.json()

            endpoint_url = data.get("status", {}).get("url", "")

            return FinetuneJob(
                platform="huggingface",
                job_id=data.get("name", endpoint_name),
                status="pending",
                base_model=model_id,
                fine_tuned_model=model_id,
                created_at=time.time(),
                endpoint_config=self._make_endpoint_config(endpoint_url, model_id),
            )

    def _make_endpoint_config(
        self, endpoint_url: str, model_id: str
    ) -> dict[str, Any]:
        """Create endpoint config compatible with UnifiedAPIClient."""
        return {
            "name": "hf-inference-endpoint",
            "provider": "huggingface",
            "base_url": endpoint_url,
            "api_key": self.config.api_key,
            "model": model_id,
            "enabled": True,
        }


# ---------------------------------------------------------------------------
# RunPod Client
# ---------------------------------------------------------------------------

class RunPodClient:
    """Manage serverless inference on RunPod.

    RunPod provides:
    - Serverless vLLM endpoints with custom models
    - GPU pods for training
    - Persistent volumes for model storage
    """

    def __init__(self, config: RunPodConfig | None = None):
        self.config = config or RunPodConfig()

    async def create_serverless_endpoint(
        self,
        model_name: str,
        endpoint_name: str = "safety-redteam",
    ) -> FinetuneJob:
        """Create a serverless vLLM endpoint on RunPod."""
        import httpx

        payload = {
            "name": endpoint_name,
            "templateId": self.config.template_id,
            "gpuIds": self.config.gpu_type,
            "workersMin": 0,
            "workersMax": self.config.max_workers,
            "env": {
                "MODEL_NAME": model_name,
            },
        }

        if self.config.volume_id:
            payload["volumeId"] = self.config.volume_id

        async with httpx.AsyncClient(timeout=60) as client:
            resp = await client.post(
                f"{self.config.base_url}/endpoints",
                headers={
                    "Authorization": f"Bearer {self.config.api_key}",
                    "Content-Type": "application/json",
                },
                json=payload,
            )
            resp.raise_for_status()
            data = resp.json()

            endpoint_id = data.get("id", "")

            return FinetuneJob(
                platform="runpod",
                job_id=endpoint_id,
                status="pending",
                base_model=model_name,
                fine_tuned_model=model_name,
                created_at=time.time(),
                endpoint_config=self._make_endpoint_config(endpoint_id),
            )

    def _make_endpoint_config(self, endpoint_id: str) -> dict[str, Any]:
        """Create endpoint config compatible with UnifiedAPIClient."""
        return {
            "name": "runpod-serverless",
            "provider": "runpod",
            "base_url": f"https://api.runpod.ai/v2/{endpoint_id}/openai/v1",
            "api_key": self.config.api_key,
            "model": "default",
            "enabled": True,
        }


# ---------------------------------------------------------------------------
# OpenAI Fine-tuning Client
# ---------------------------------------------------------------------------

class OpenAIFinetuneClient:
    """Manage fine-tuning on OpenAI.

    Uses OpenAI's fine-tuning API for comparison testing.
    Fine-tuned models are automatically available for inference.
    """

    def __init__(self, config: OpenAIFinetuneConfig | None = None):
        self.config = config or OpenAIFinetuneConfig()

    async def upload_file(self, file_path: Path) -> str:
        """Upload a training file to OpenAI."""
        import httpx

        async with httpx.AsyncClient(timeout=120) as client:
            with open(file_path, "rb") as f:
                resp = await client.post(
                    f"{self.config.base_url}/files",
                    headers={"Authorization": f"Bearer {self.config.api_key}"},
                    files={"file": (file_path.name, f, "application/jsonl")},
                    data={"purpose": "fine-tune"},
                )
                resp.raise_for_status()
                return resp.json()["id"]

    async def create_finetune(self, training_file_id: str) -> FinetuneJob:
        """Create a fine-tuning job on OpenAI."""
        import httpx

        payload = {
            "model": self.config.base_model,
            "training_file": training_file_id,
            "suffix": self.config.suffix,
            "hyperparameters": {
                "n_epochs": self.config.n_epochs,
            },
        }

        async with httpx.AsyncClient(timeout=60) as client:
            resp = await client.post(
                f"{self.config.base_url}/fine_tuning/jobs",
                headers={
                    "Authorization": f"Bearer {self.config.api_key}",
                    "Content-Type": "application/json",
                },
                json=payload,
            )
            resp.raise_for_status()
            data = resp.json()

            return FinetuneJob(
                platform="openai",
                job_id=data["id"],
                status="pending",
                base_model=self.config.base_model,
                created_at=time.time(),
            )

    async def poll_status(self, job: FinetuneJob) -> FinetuneJob:
        """Poll status of an OpenAI fine-tuning job."""
        import httpx

        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.get(
                f"{self.config.base_url}/fine_tuning/jobs/{job.job_id}",
                headers={"Authorization": f"Bearer {self.config.api_key}"},
            )
            resp.raise_for_status()
            data = resp.json()

            status = data.get("status", "")
            if status == "succeeded":
                job.status = "completed"
                job.fine_tuned_model = data.get("fine_tuned_model", "")
                job.completed_at = time.time()
                job.endpoint_config = self._make_endpoint_config(job.fine_tuned_model)
            elif status in ("failed", "cancelled"):
                job.status = "failed"
                job.error = str(data.get("error", ""))
            else:
                job.status = "running"

            return job

    async def wait_for_completion(self, job: FinetuneJob) -> FinetuneJob:
        """Poll until complete."""
        start = time.time()
        while time.time() - start < self.config.timeout:
            job = await self.poll_status(job)
            if job.is_complete or job.is_failed:
                return job
            await asyncio.sleep(self.config.poll_interval)

        job.status = "failed"
        job.error = "Timed out"
        return job

    async def run_full_pipeline(self, training_file: Path) -> FinetuneJob:
        """Upload, fine-tune, and wait."""
        file_id = await self.upload_file(training_file)
        job = await self.create_finetune(file_id)
        return await self.wait_for_completion(job)

    def _make_endpoint_config(self, model_name: str) -> dict[str, Any]:
        return {
            "name": f"openai-{self.config.suffix}",
            "provider": "openai",
            "base_url": "https://api.openai.com/v1",
            "api_key": self.config.api_key,
            "model": model_name,
            "enabled": True,
        }


# ---------------------------------------------------------------------------
# CloudInferenceRouter — unified entry point
# ---------------------------------------------------------------------------

class CloudInferenceRouter:
    """Unified router for cloud fine-tuning and inference.

    Given a platform and training data, handles the complete lifecycle:
    upload -> fine-tune -> deploy -> return endpoint config.

    The returned endpoint_config is compatible with UnifiedAPIClient.
    """

    PLATFORMS = {
        "together": TogetherFinetuneClient,
        "huggingface": HuggingFaceFinetuneClient,
        "openai": OpenAIFinetuneClient,
        "runpod": RunPodClient,
    }

    def __init__(self):
        self._jobs: list[FinetuneJob] = []

    @staticmethod
    def list_platforms() -> list[dict[str, str]]:
        """List available cloud platforms."""
        return [
            {
                "id": "together",
                "name": "Together AI",
                "description": "LoRA fine-tuning + serverless inference. Best for quick iterations.",
                "supports_finetune": True,
                "supports_inference": True,
            },
            {
                "id": "huggingface",
                "name": "HuggingFace",
                "description": "AutoTrain + Inference Endpoints. Best for HF ecosystem.",
                "supports_finetune": True,
                "supports_inference": True,
            },
            {
                "id": "openai",
                "name": "OpenAI",
                "description": "Fine-tuning API. For comparison testing against GPT models.",
                "supports_finetune": True,
                "supports_inference": True,
            },
            {
                "id": "runpod",
                "name": "RunPod",
                "description": "Serverless vLLM endpoints. Best for custom model deployment.",
                "supports_finetune": False,
                "supports_inference": True,
            },
        ]

    async def finetune_and_deploy(
        self,
        platform: str,
        training_file: Path,
        config: dict[str, Any] | None = None,
    ) -> FinetuneJob:
        """Fine-tune a model on the specified platform and deploy for inference.

        Args:
            platform: 'together', 'huggingface', 'openai', or 'runpod'
            training_file: Path to JSONL training data
            config: Platform-specific configuration overrides

        Returns:
            FinetuneJob with endpoint_config ready for UnifiedAPIClient
        """
        config = config or {}

        if platform == "together":
            client = TogetherFinetuneClient(TogetherConfig(**config))
            job = await client.run_full_pipeline(training_file)
        elif platform == "openai":
            client = OpenAIFinetuneClient(OpenAIFinetuneConfig(**config))
            job = await client.run_full_pipeline(training_file)
        elif platform == "huggingface":
            hf_client = HuggingFaceFinetuneClient(HuggingFaceConfig(**config))
            repo_id = await hf_client.upload_dataset(training_file)
            job = await hf_client.create_inference_endpoint(repo_id)
        elif platform == "runpod":
            rp_client = RunPodClient(RunPodConfig(**config))
            model = config.get("model_name", "mistralai/Mistral-7B-Instruct-v0.3")
            job = await rp_client.create_serverless_endpoint(model)
        else:
            raise ValueError(f"Unknown platform: {platform}. Use: {list(self.PLATFORMS.keys())}")

        self._jobs.append(job)
        return job

    def get_jobs(self) -> list[dict[str, Any]]:
        """Get all tracked fine-tuning jobs."""
        return [j.to_dict() for j in self._jobs]

    def get_latest_endpoint(self) -> dict[str, Any] | None:
        """Get the endpoint config from the most recent completed job."""
        for job in reversed(self._jobs):
            if job.is_complete and job.endpoint_config:
                return job.endpoint_config
        return None
