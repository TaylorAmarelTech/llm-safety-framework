"""
Pipeline orchestrator.

Coordinates all spinning modules and builds the active pipeline
from prompt sets + spin jobs.
"""

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Any, Optional

from .storage import SpinStorage


class PipelineManager:
    """Orchestrates the spinning pipeline."""

    def __init__(self, data_dir: str = "data", pipeline_dir: str = "data/pipeline"):
        self.data_dir = Path(data_dir)
        self.storage = SpinStorage(pipeline_dir)

    def build(
        self,
        prompt_set_ids: Optional[List[str]] = None,
        include_spun: bool = True,
        deduplicate: bool = True,
    ) -> Dict[str, Any]:
        """
        Build the active pipeline from prompt sets and spin jobs.

        Args:
            prompt_set_ids: Specific set IDs to include (None = all enabled)
            include_spun: Include spun prompts from spin jobs
            deduplicate: Remove duplicate prompts

        Returns:
            Pipeline summary with total counts and sources.
        """
        all_prompts: List[Dict[str, Any]] = []
        sources: List[Dict[str, Any]] = []

        # Load default prompt sets
        prompts_file = self.data_dir / "sample_test_prompts.json"
        if prompts_file.exists():
            with open(prompts_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            config = self.storage.get_pipeline_config()
            disabled = config.get("disabled_sets", [])

            for suite_name, suite_prompts in data.get("test_suites", {}).items():
                if prompt_set_ids and suite_name not in prompt_set_ids:
                    continue
                if suite_name in disabled:
                    continue
                for p in suite_prompts:
                    all_prompts.append({
                        "text": p.get("prompt", ""),
                        "source": f"set:{suite_name}",
                        "metadata": p,
                    })
                sources.append({"type": "set", "id": suite_name, "count": len(suite_prompts)})

        # Load imported prompt sets
        imported_dir = self.storage.prompt_sets_dir
        if imported_dir.exists():
            for f in imported_dir.glob("*.json"):
                if prompt_set_ids and f.stem not in prompt_set_ids:
                    continue
                try:
                    with open(f, 'r', encoding='utf-8') as fh:
                        data = json.load(fh)
                    prompts = data if isinstance(data, list) else data.get("prompts", [])
                    for p in prompts:
                        text = p if isinstance(p, str) else p.get("prompt", p.get("text", ""))
                        all_prompts.append({
                            "text": text,
                            "source": f"imported:{f.stem}",
                            "metadata": p if isinstance(p, dict) else {},
                        })
                    sources.append({"type": "imported", "id": f.stem, "count": len(prompts)})
                except Exception:
                    continue

        # Load spun prompts
        if include_spun:
            spun_prompts = self.storage.get_all_spun_prompts()
            if spun_prompts:
                # Group by source for summary
                spun_sources: Dict[str, int] = {}
                for p in spun_prompts:
                    src = p["source"]
                    spun_sources[src] = spun_sources.get(src, 0) + 1
                    all_prompts.append(p)
                for src, count in spun_sources.items():
                    job_id = src.replace("spun:", "")
                    sources.append({"type": "spun", "id": job_id, "count": count})

        # Deduplicate
        if deduplicate:
            seen = set()
            deduped = []
            for p in all_prompts:
                text = p["text"].strip().lower()
                if text not in seen:
                    seen.add(text)
                    deduped.append(p)
            all_prompts = deduped

        # Save
        pipeline_data = {
            "built_at": datetime.now(tz=timezone.utc).isoformat(),
            "sources": sources,
            "total": len(all_prompts),
            "prompts": all_prompts,
        }
        self.storage.save_active_pipeline(pipeline_data)

        return {
            "total": len(all_prompts),
            "sources": sources,
            "deduplicated": deduplicate,
        }

    def get_status(self) -> Optional[Dict[str, Any]]:
        """Get current pipeline status without full prompt list."""
        data = self.storage.load_active_pipeline()
        if not data:
            return None
        return {
            "built_at": data.get("built_at"),
            "total": data.get("total", 0),
            "sources": data.get("sources", []),
        }

    def get_prompts(self, limit: int = 100, offset: int = 0) -> Dict[str, Any]:
        """Get prompts from the active pipeline with pagination."""
        data = self.storage.load_active_pipeline()
        if not data:
            return {"prompts": [], "total": 0}

        prompts = data.get("prompts", [])
        return {
            "prompts": prompts[offset:offset + limit],
            "total": len(prompts),
        }

    def get_all_prompts(self) -> List[Dict[str, Any]]:
        """Get all prompts from the active pipeline."""
        data = self.storage.load_active_pipeline()
        if not data:
            return []
        return data.get("prompts", [])
