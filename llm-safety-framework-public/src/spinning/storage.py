"""
JSON file storage for spin jobs and pipeline data.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

from .models import SpinJob, SpinType, ActivePipeline, PipelineSource, PipelinePrompt


class SpinStorage:
    """Manages file storage for spin jobs and the active pipeline."""

    def __init__(self, pipeline_dir: str = "data/pipeline"):
        self.pipeline_dir = Path(pipeline_dir)
        self.spun_dir = self.pipeline_dir / "spun"
        self.prompt_sets_dir = self.pipeline_dir / "prompt_sets"

    def _ensure_dirs(self) -> None:
        self.pipeline_dir.mkdir(parents=True, exist_ok=True)
        self.spun_dir.mkdir(parents=True, exist_ok=True)

    def save_job(self, job: SpinJob) -> None:
        """Save a spin job to disk."""
        self._ensure_dirs()
        data = {
            "id": job.id,
            "type": job.type.value,
            "created_at": job.created_at.isoformat(),
            "config": job.config,
            "prompts": job.prompts,
        }
        if job.details:
            data["details"] = job.details

        with open(self.spun_dir / f"{job.id}.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load_job(self, job_id: str) -> Optional[SpinJob]:
        """Load a spin job from disk."""
        job_file = self.spun_dir / f"{job_id}.json"
        if not job_file.exists():
            return None

        with open(job_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        return SpinJob(
            id=data["id"],
            type=SpinType(data["type"]),
            created_at=datetime.fromisoformat(data["created_at"]),
            config=data.get("config", {}),
            prompts=data.get("prompts", []),
            details=data.get("details"),
        )

    def list_jobs(self) -> List[Dict[str, Any]]:
        """List all spin jobs with summary info."""
        if not self.spun_dir.exists():
            return []

        jobs = []
        for f in sorted(self.spun_dir.glob("*.json"), key=lambda x: x.stat().st_mtime, reverse=True):
            try:
                with open(f, 'r', encoding='utf-8') as fh:
                    data = json.load(fh)
                jobs.append({
                    "id": data.get("id", f.stem),
                    "type": data.get("type", "unknown"),
                    "created_at": data.get("created_at", ""),
                    "count": len(data.get("prompts", [])),
                })
            except Exception:
                continue
        return jobs

    def delete_job(self, job_id: str) -> bool:
        """Delete a spin job."""
        job_file = self.spun_dir / f"{job_id}.json"
        if job_file.exists():
            job_file.unlink()
            return True
        return False

    def get_pipeline_config(self) -> Dict[str, Any]:
        """Get pipeline configuration (disabled sets, preparation rules)."""
        config_file = self.pipeline_dir / "pipeline_config.json"
        if config_file.exists():
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def save_pipeline_config(self, config: Dict[str, Any]) -> None:
        """Save pipeline configuration."""
        self._ensure_dirs()
        with open(self.pipeline_dir / "pipeline_config.json", 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)

    def load_active_pipeline(self) -> Optional[Dict[str, Any]]:
        """Load the active pipeline."""
        pipeline_file = self.pipeline_dir / "active_pipeline.json"
        if not pipeline_file.exists():
            return None
        with open(pipeline_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_active_pipeline(self, pipeline: Dict[str, Any]) -> None:
        """Save the active pipeline."""
        self._ensure_dirs()
        with open(self.pipeline_dir / "active_pipeline.json", 'w', encoding='utf-8') as f:
            json.dump(pipeline, f, indent=2, ensure_ascii=False)

    def get_all_spun_prompts(self) -> List[Dict[str, Any]]:
        """Get all prompts from all spin jobs."""
        if not self.spun_dir.exists():
            return []

        all_prompts = []
        for f in self.spun_dir.glob("*.json"):
            try:
                with open(f, 'r', encoding='utf-8') as fh:
                    data = json.load(fh)
                job_id = data.get("id", f.stem)
                for p in data.get("prompts", []):
                    text = p if isinstance(p, str) else p.get("text", str(p))
                    all_prompts.append({
                        "text": text,
                        "source": f"spun:{job_id}",
                        "metadata": {},
                    })
            except Exception:
                continue
        return all_prompts
