"""
HuggingFace Hub dataset management for the safety training pipeline.

Provides:
1. Push training datasets (JSONL) to HuggingFace Hub with auto-generated cards
2. Pull community datasets for evaluation or fine-tuning
3. Version tracking with git tags on dataset repos
4. Local dataset management (merge, split, filter, sample, stats)

All network methods are async (httpx) and handle missing tokens gracefully.
"""

from __future__ import annotations

import hashlib
import json
import os
import random
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

HF_API_BASE = "https://huggingface.co/api"
HF_UPLOAD_BASE = "https://huggingface.co/api"


class HubConfig(BaseModel):
    """Configuration for HuggingFace Hub integration."""

    token: str = Field(default="", description="HuggingFace API token (HF_TOKEN)")
    namespace: str = Field(default="", description="HF username or organization")
    default_repo: str = Field(
        default="safety-redteam-training",
        description="Default dataset repository name",
    )
    private: bool = Field(default=True, description="Create repos as private")
    revision: str = Field(default="main", description="Default branch/revision")

    def resolve_token(self) -> str:
        """Return token from config or HF_TOKEN env var."""
        return self.token or os.environ.get("HF_TOKEN", "")

    def resolve_namespace(self) -> str:
        """Return namespace from config or empty string."""
        return self.namespace or os.environ.get("HF_NAMESPACE", "")

    @property
    def has_credentials(self) -> bool:
        return bool(self.resolve_token())


# ---------------------------------------------------------------------------
# Dataset Card
# ---------------------------------------------------------------------------

class DatasetCard(BaseModel):
    """Metadata card for a pushed dataset."""

    name: str
    description: str = ""
    version: str = "1.0.0"
    format: str = "dpo"  # sft, dpo, rlhf, chatml, alpaca, sharegpt, orpo, kto, llama3
    num_examples: int = 0
    categories: list[str] = Field(default_factory=list)
    corridors: list[str] = Field(default_factory=list)
    mutations_used: list[str] = Field(default_factory=list)
    base_model: str = ""
    created_at: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    metadata: dict[str, Any] = Field(default_factory=dict)


# ---------------------------------------------------------------------------
# HTTP Helpers
# ---------------------------------------------------------------------------

def _auth_headers(token: str) -> dict[str, str]:
    """Build authorization headers."""
    return {"Authorization": f"Bearer {token}"}


def _no_token_error(method: str) -> dict[str, Any]:
    """Standard error for missing credentials."""
    return {
        "error": "no_token",
        "message": (
            f"HuggingFace token not configured. Cannot execute '{method}'. "
            "Set HF_TOKEN environment variable or pass token in HubConfig."
        ),
    }


# ---------------------------------------------------------------------------
# HubIntegration — async push/pull/version management
# ---------------------------------------------------------------------------

class HubIntegration:
    """Manage dataset lifecycle on HuggingFace Hub.

    All network operations are async and use httpx.  When the token is
    missing, methods return an informative error dict instead of raising.
    """

    def __init__(self, config: HubConfig | None = None) -> None:
        self.config = config or HubConfig()

    # -- internal helpers ---------------------------------------------------

    def _token(self) -> str:
        return self.config.resolve_token()

    def _repo_id(self, repo_name: str | None) -> str:
        ns = self.config.resolve_namespace()
        name = repo_name or self.config.default_repo
        if ns:
            return f"{ns}/{name}"
        return name

    # -- create dataset readme ----------------------------------------------

    def create_dataset_readme(self, card: DatasetCard) -> str:
        """Generate a HuggingFace-compatible dataset README with YAML front-matter."""

        cats_yaml = "\n".join(f"  - {c}" for c in card.categories) if card.categories else "  - safety"
        corridors_yaml = "\n".join(f"  - {c}" for c in card.corridors) if card.corridors else ""
        mutations_yaml = "\n".join(f"  - {m}" for m in card.mutations_used) if card.mutations_used else ""

        yaml_block = (
            "---\n"
            "language:\n"
            "  - en\n"
            "license: apache-2.0\n"
            "task_categories:\n"
            "  - text-classification\n"
            "  - text-generation\n"
            "tags:\n"
            "  - safety\n"
            "  - red-teaming\n"
            "  - llm-safety\n"
            "  - migrant-worker-protection\n"
            "  - human-trafficking-detection\n"
            f"size_categories:\n"
            f"  - {_size_category(card.num_examples)}\n"
            "---\n"
        )

        body = (
            f"# {card.name}\n\n"
            f"{card.description}\n\n"
            "## Dataset Details\n\n"
            f"- **Format:** {card.format}\n"
            f"- **Version:** {card.version}\n"
            f"- **Examples:** {card.num_examples:,}\n"
            f"- **Base Model:** {card.base_model or 'N/A'}\n"
            f"- **Created:** {card.created_at}\n\n"
        )

        if card.categories:
            body += "## Categories\n\n"
            for c in card.categories:
                body += f"- {c}\n"
            body += "\n"

        if card.corridors:
            body += "## Migration Corridors\n\n"
            for c in card.corridors:
                body += f"- {c}\n"
            body += "\n"

        if card.mutations_used:
            body += "## Mutation Techniques Applied\n\n"
            for m in card.mutations_used:
                body += f"- {m}\n"
            body += "\n"

        body += (
            "## Purpose\n\n"
            "This dataset is part of the **LLM Safety Testing Framework** for "
            "evaluating whether Large Language Models properly refuse requests "
            "that could facilitate human trafficking and migrant worker exploitation.\n\n"
            "**SUCCESS = Model REFUSES harmful requests.**\n\n"
            "## Citation\n\n"
            "```bibtex\n"
            "@misc{safety-redteam-training,\n"
            "  title={LLM Safety Testing Framework},\n"
            "  author={Taylor Amarel},\n"
            "  year={2026},\n"
            "  howpublished={HuggingFace Hub},\n"
            "}\n"
            "```\n"
        )

        if card.metadata:
            body += "\n## Additional Metadata\n\n"
            body += "```json\n"
            body += json.dumps(card.metadata, indent=2)
            body += "\n```\n"

        return yaml_block + "\n" + body

    # -- push dataset -------------------------------------------------------

    async def push_dataset(
        self,
        file_path: Path,
        card: DatasetCard,
        repo_name: str | None = None,
    ) -> str:
        """Upload a JSONL dataset and auto-generated README to HuggingFace Hub.

        Returns the repo URL on success, or an error dict string on failure.
        """
        import httpx

        token = self._token()
        if not token:
            return json.dumps(_no_token_error("push_dataset"))

        repo_id = self._repo_id(repo_name)

        # 1. Ensure repo exists (create if needed)
        await self._ensure_repo(token, repo_id)

        headers = _auth_headers(token)
        revision = self.config.revision

        async with httpx.AsyncClient(timeout=120) as client:
            # 2. Upload the JSONL file
            file_bytes = file_path.read_bytes()
            upload_url = (
                f"{HF_UPLOAD_BASE}/datasets/{repo_id}/upload/{revision}/"
                f"{file_path.name}"
            )
            resp = await client.put(
                upload_url,
                headers={**headers, "Content-Type": "application/octet-stream"},
                content=file_bytes,
            )
            if resp.status_code >= 400:
                return json.dumps({
                    "error": "upload_failed",
                    "status": resp.status_code,
                    "detail": resp.text,
                })

            # 3. Upload README.md
            readme_content = self.create_dataset_readme(card).encode("utf-8")
            readme_url = (
                f"{HF_UPLOAD_BASE}/datasets/{repo_id}/upload/{revision}/README.md"
            )
            resp2 = await client.put(
                readme_url,
                headers={**headers, "Content-Type": "application/octet-stream"},
                content=readme_content,
            )
            if resp2.status_code >= 400:
                return json.dumps({
                    "error": "readme_upload_failed",
                    "status": resp2.status_code,
                    "detail": resp2.text,
                })

        return f"https://huggingface.co/datasets/{repo_id}"

    # -- push training results directory ------------------------------------

    async def push_training_results(
        self,
        results_dir: Path,
        card: DatasetCard,
        repo_name: str | None = None,
    ) -> str:
        """Upload an entire training results directory to HuggingFace Hub.

        Walks the directory and uploads every file.  Returns the repo URL.
        """
        import httpx

        token = self._token()
        if not token:
            return json.dumps(_no_token_error("push_training_results"))

        repo_id = self._repo_id(repo_name)
        await self._ensure_repo(token, repo_id)

        headers = _auth_headers(token)
        revision = self.config.revision
        errors: list[dict[str, Any]] = []

        async with httpx.AsyncClient(timeout=120) as client:
            # Upload README first
            readme_content = self.create_dataset_readme(card).encode("utf-8")
            readme_url = (
                f"{HF_UPLOAD_BASE}/datasets/{repo_id}/upload/{revision}/README.md"
            )
            await client.put(
                readme_url,
                headers={**headers, "Content-Type": "application/octet-stream"},
                content=readme_content,
            )

            # Walk directory and upload each file
            for fpath in sorted(results_dir.rglob("*")):
                if fpath.is_dir():
                    continue
                rel = fpath.relative_to(results_dir).as_posix()
                upload_url = (
                    f"{HF_UPLOAD_BASE}/datasets/{repo_id}/upload/{revision}/{rel}"
                )
                try:
                    file_bytes = fpath.read_bytes()
                    resp = await client.put(
                        upload_url,
                        headers={
                            **headers,
                            "Content-Type": "application/octet-stream",
                        },
                        content=file_bytes,
                    )
                    if resp.status_code >= 400:
                        errors.append({
                            "file": rel,
                            "status": resp.status_code,
                            "detail": resp.text[:200],
                        })
                except Exception as exc:
                    errors.append({"file": rel, "error": str(exc)})

        url = f"https://huggingface.co/datasets/{repo_id}"
        if errors:
            return json.dumps({
                "url": url,
                "partial": True,
                "errors": errors,
            })
        return url

    # -- pull dataset -------------------------------------------------------

    async def pull_dataset(
        self,
        repo_id: str,
        output_dir: Path,
        revision: str = "main",
    ) -> Path:
        """Download a dataset from HuggingFace Hub.

        Fetches the file listing and downloads each file into *output_dir*.
        Returns the output directory path.
        """
        import httpx

        token = self._token()
        headers = _auth_headers(token) if token else {}
        output_dir.mkdir(parents=True, exist_ok=True)

        async with httpx.AsyncClient(timeout=120, follow_redirects=True) as client:
            # List files in the repo
            list_url = f"{HF_API_BASE}/datasets/{repo_id}/tree/{revision}"
            resp = await client.get(list_url, headers=headers)
            if resp.status_code >= 400:
                raise RuntimeError(
                    f"Failed to list repo {repo_id}: {resp.status_code} {resp.text}"
                )

            files = resp.json()
            for entry in files:
                if entry.get("type") != "file":
                    continue
                rfilename = entry["rfilename"]
                download_url = (
                    f"https://huggingface.co/datasets/{repo_id}"
                    f"/resolve/{revision}/{rfilename}"
                )
                dl_resp = await client.get(download_url, headers=headers)
                if dl_resp.status_code >= 400:
                    continue  # skip inaccessible files silently

                dest = output_dir / rfilename
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(dl_resp.content)

        return output_dir

    # -- list datasets ------------------------------------------------------

    async def list_datasets(
        self, namespace: str | None = None
    ) -> list[dict[str, Any]]:
        """List available datasets in a namespace.

        Returns a list of dicts with repo metadata.  If no token is set and
        the namespace is private, this will return an empty list.
        """
        import httpx

        ns = namespace or self.config.resolve_namespace()
        if not ns:
            return [{"error": "no_namespace", "message": "Namespace not configured."}]

        token = self._token()
        headers = _auth_headers(token) if token else {}

        async with httpx.AsyncClient(timeout=60) as client:
            url = f"{HF_API_BASE}/datasets?author={ns}&full=true"
            resp = await client.get(url, headers=headers)
            if resp.status_code >= 400:
                return [{
                    "error": "list_failed",
                    "status": resp.status_code,
                    "detail": resp.text[:300],
                }]
            datasets = resp.json()

        results: list[dict[str, Any]] = []
        for ds in datasets:
            results.append({
                "id": ds.get("id", ""),
                "private": ds.get("private", False),
                "downloads": ds.get("downloads", 0),
                "likes": ds.get("likes", 0),
                "tags": ds.get("tags", []),
                "last_modified": ds.get("lastModified", ""),
                "card_data": ds.get("cardData", {}),
            })
        return results

    # -- version management -------------------------------------------------

    async def get_dataset_versions(
        self, repo_id: str
    ) -> list[dict[str, Any]]:
        """List all refs (branches and tags) on a dataset repo."""
        import httpx

        token = self._token()
        if not token:
            return [_no_token_error("get_dataset_versions")]

        headers = _auth_headers(token)

        async with httpx.AsyncClient(timeout=30) as client:
            url = f"{HF_API_BASE}/datasets/{repo_id}/refs"
            resp = await client.get(url, headers=headers)
            if resp.status_code >= 400:
                return [{
                    "error": "refs_failed",
                    "status": resp.status_code,
                    "detail": resp.text[:300],
                }]
            data = resp.json()

        versions: list[dict[str, Any]] = []
        for branch in data.get("branches", []):
            versions.append({
                "type": "branch",
                "name": branch.get("name", ""),
                "ref": branch.get("ref", ""),
                "target_commit": branch.get("targetCommit", ""),
            })
        for tag in data.get("tags", []):
            versions.append({
                "type": "tag",
                "name": tag.get("name", ""),
                "ref": tag.get("ref", ""),
                "target_commit": tag.get("targetCommit", ""),
            })
        return versions

    async def tag_version(
        self, repo_id: str, tag: str, message: str
    ) -> None:
        """Create a git tag on a dataset repo.

        Uses the HuggingFace Hub API to create an annotated tag pointing at
        the latest commit on the default branch.
        """
        import httpx

        token = self._token()
        if not token:
            raise ValueError(
                "HuggingFace token required for tagging. "
                "Set HF_TOKEN or pass token in HubConfig."
            )

        headers = _auth_headers(token)

        async with httpx.AsyncClient(timeout=30) as client:
            # Resolve HEAD commit on the default branch
            refs_url = f"{HF_API_BASE}/datasets/{repo_id}/refs"
            refs_resp = await client.get(refs_url, headers=headers)
            refs_resp.raise_for_status()
            refs_data = refs_resp.json()

            target_sha = ""
            for branch in refs_data.get("branches", []):
                if branch.get("name") == self.config.revision:
                    target_sha = branch.get("targetCommit", "")
                    break
            if not target_sha:
                raise RuntimeError(
                    f"Could not resolve HEAD for {repo_id}@{self.config.revision}"
                )

            # Create the tag
            tag_url = f"{HF_API_BASE}/datasets/{repo_id}/tag"
            resp = await client.post(
                tag_url,
                headers={**headers, "Content-Type": "application/json"},
                json={"tag": tag, "message": message, "sha": target_sha},
            )
            resp.raise_for_status()

    # -- internal: ensure repo exists ---------------------------------------

    async def _ensure_repo(self, token: str, repo_id: str) -> None:
        """Create the dataset repo if it doesn't already exist."""
        import httpx

        headers = {**_auth_headers(token), "Content-Type": "application/json"}

        async with httpx.AsyncClient(timeout=30) as client:
            check_url = f"{HF_API_BASE}/datasets/{repo_id}"
            resp = await client.get(check_url, headers=headers)
            if resp.status_code == 200:
                return  # already exists

            # Parse name from repo_id
            parts = repo_id.split("/", 1)
            org = parts[0] if len(parts) == 2 else None
            name = parts[-1]

            create_payload: dict[str, Any] = {
                "name": name,
                "type": "dataset",
                "private": self.config.private,
            }
            if org:
                create_payload["organization"] = org

            create_url = f"{HF_API_BASE}/repos/create"
            create_resp = await client.post(
                create_url, headers=headers, json=create_payload
            )
            # 409 = already exists (race condition), which is fine
            if create_resp.status_code >= 400 and create_resp.status_code != 409:
                raise RuntimeError(
                    f"Failed to create repo {repo_id}: "
                    f"{create_resp.status_code} {create_resp.text}"
                )


# ---------------------------------------------------------------------------
# LocalDatasetManager — offline file operations
# ---------------------------------------------------------------------------

class LocalDatasetManager:
    """Manage local JSONL dataset files without network access.

    Handles merging, splitting, filtering, sampling, and statistics for
    training data stored on disk.
    """

    def __init__(self, data_dir: Path) -> None:
        self.data_dir = data_dir
        self.data_dir.mkdir(parents=True, exist_ok=True)

    # -- list local datasets ------------------------------------------------

    def list_local_datasets(self) -> list[dict[str, Any]]:
        """Scan data_dir (recursively) for JSONL files and return metadata."""
        results: list[dict[str, Any]] = []
        for fpath in sorted(self.data_dir.rglob("*.jsonl")):
            stat = fpath.stat()
            line_count = _count_lines(fpath)
            detected_format = _detect_format(fpath)
            results.append({
                "path": str(fpath),
                "name": fpath.stem,
                "size_bytes": stat.st_size,
                "size_human": _human_size(stat.st_size),
                "lines": line_count,
                "format": detected_format,
                "modified": datetime.fromtimestamp(
                    stat.st_mtime, tz=timezone.utc
                ).isoformat(),
            })
        return results

    # -- dataset stats ------------------------------------------------------

    def get_dataset_stats(self, file_path: Path) -> dict[str, Any]:
        """Compute detailed statistics for a single JSONL file."""
        if not file_path.exists():
            return {"error": "file_not_found", "path": str(file_path)}

        stat = file_path.stat()
        line_count = 0
        field_counts: dict[str, int] = {}
        categories: set[str] = set()
        formats_seen: set[str] = set()
        byte_hash = hashlib.sha256()

        with open(file_path, "r", encoding="utf-8", errors="replace") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                line_count += 1
                byte_hash.update(line.encode("utf-8"))
                try:
                    obj = json.loads(line)
                    for key in obj:
                        field_counts[key] = field_counts.get(key, 0) + 1
                    # Detect format from keys
                    if "chosen" in obj and "rejected" in obj:
                        formats_seen.add("dpo")
                    elif "conversations" in obj:
                        formats_seen.add("sharegpt")
                    elif "instruction" in obj and "output" in obj:
                        formats_seen.add("alpaca")
                    elif "messages" in obj:
                        formats_seen.add("chatml")
                    elif "prompt" in obj and "completion" in obj:
                        formats_seen.add("sft")
                    # Collect categories
                    cat = obj.get("category") or obj.get("metadata", {}).get("category")
                    if cat:
                        categories.add(str(cat))
                except json.JSONDecodeError:
                    continue

        return {
            "path": str(file_path),
            "size_bytes": stat.st_size,
            "size_human": _human_size(stat.st_size),
            "lines": line_count,
            "sha256": byte_hash.hexdigest(),
            "formats_detected": sorted(formats_seen),
            "fields": dict(sorted(field_counts.items(), key=lambda x: -x[1])),
            "categories": sorted(categories),
            "modified": datetime.fromtimestamp(
                stat.st_mtime, tz=timezone.utc
            ).isoformat(),
        }

    # -- merge datasets -----------------------------------------------------

    def merge_datasets(
        self, paths: list[Path], output: Path
    ) -> Path:
        """Merge multiple JSONL files into one, deduplicating by content hash."""
        seen_hashes: set[str] = set()
        output.parent.mkdir(parents=True, exist_ok=True)
        written = 0

        with open(output, "w", encoding="utf-8") as out_fh:
            for p in paths:
                if not p.exists():
                    continue
                with open(p, "r", encoding="utf-8", errors="replace") as in_fh:
                    for line in in_fh:
                        line = line.strip()
                        if not line:
                            continue
                        h = hashlib.md5(line.encode("utf-8")).hexdigest()
                        if h in seen_hashes:
                            continue
                        seen_hashes.add(h)
                        out_fh.write(line + "\n")
                        written += 1

        return output

    # -- split dataset ------------------------------------------------------

    def split_dataset(
        self,
        file_path: Path,
        train_ratio: float = 0.9,
    ) -> tuple[Path, Path]:
        """Split a JSONL file into train and test sets.

        Returns (train_path, test_path).
        """
        lines: list[str] = []
        with open(file_path, "r", encoding="utf-8", errors="replace") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    lines.append(line)

        random.shuffle(lines)
        split_idx = int(len(lines) * train_ratio)
        train_lines = lines[:split_idx]
        test_lines = lines[split_idx:]

        stem = file_path.stem
        parent = file_path.parent
        train_path = parent / f"{stem}_train.jsonl"
        test_path = parent / f"{stem}_test.jsonl"

        with open(train_path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(train_lines) + "\n")
        with open(test_path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(test_lines) + "\n")

        return train_path, test_path

    # -- filter dataset -----------------------------------------------------

    def filter_dataset(
        self,
        file_path: Path,
        predicate: Callable[[dict[str, Any]], bool],
        output: Path,
    ) -> Path:
        """Filter JSONL examples using a predicate function.

        Only examples where predicate(parsed_json) returns True are kept.
        """
        output.parent.mkdir(parents=True, exist_ok=True)
        kept = 0

        with (
            open(file_path, "r", encoding="utf-8", errors="replace") as in_fh,
            open(output, "w", encoding="utf-8") as out_fh,
        ):
            for line in in_fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if predicate(obj):
                    out_fh.write(line + "\n")
                    kept += 1

        return output

    # -- sample dataset -----------------------------------------------------

    def sample_dataset(
        self,
        file_path: Path,
        n: int,
        output: Path,
    ) -> Path:
        """Take a random sample of *n* examples from a JSONL file."""
        lines: list[str] = []
        with open(file_path, "r", encoding="utf-8", errors="replace") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    lines.append(line)

        sample_size = min(n, len(lines))
        sampled = random.sample(lines, sample_size)

        output.parent.mkdir(parents=True, exist_ok=True)
        with open(output, "w", encoding="utf-8") as fh:
            fh.write("\n".join(sampled) + "\n")

        return output


# ---------------------------------------------------------------------------
# Private Helpers
# ---------------------------------------------------------------------------

def _count_lines(path: Path) -> int:
    """Count non-empty lines in a file."""
    count = 0
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if line.strip():
                count += 1
    return count


def _detect_format(path: Path) -> str:
    """Peek at the first valid JSON line to guess the training format."""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)
                if "chosen" in obj and "rejected" in obj:
                    return "dpo"
                if "conversations" in obj:
                    return "sharegpt"
                if "instruction" in obj and "output" in obj:
                    return "alpaca"
                if "messages" in obj:
                    return "chatml"
                if "prompt" in obj and "completion" in obj:
                    return "sft"
                return "unknown"
    except Exception:
        return "unknown"
    return "unknown"


def _human_size(nbytes: int) -> str:
    """Convert byte count to human-readable string."""
    for unit in ("B", "KB", "MB", "GB"):
        if nbytes < 1024:
            return f"{nbytes:.1f} {unit}"
        nbytes /= 1024  # type: ignore[assignment]
    return f"{nbytes:.1f} TB"


def _size_category(n: int) -> str:
    """Map example count to HuggingFace size category tag."""
    if n < 1_000:
        return "n<1K"
    if n < 10_000:
        return "1K<n<10K"
    if n < 100_000:
        return "10K<n<100K"
    if n < 1_000_000:
        return "100K<n<1M"
    return "n>1M"
