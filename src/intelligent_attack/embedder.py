"""
Embedding generation via API endpoints or local models.

Supports any configured endpoint (OpenAI, Mistral, etc.)
plus optional local sentence-transformers.
"""

from typing import List, Dict, Any, Optional

import httpx


class Embedder:
    """Generate embeddings from various sources."""

    # Known embedding models per provider
    PROVIDER_MODELS = {
        "openai": [
            {"id": "text-embedding-3-small", "dimensions": 1536},
            {"id": "text-embedding-3-large", "dimensions": 3072},
        ],
        "mistral": [
            {"id": "mistral-embed", "dimensions": 1024},
        ],
    }

    @staticmethod
    def get_sources(endpoints: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """List available embedding sources from configured endpoints."""
        sources = []

        for ep in endpoints:
            if not ep.get("enabled") or not ep.get("api_key"):
                continue

            provider = ep.get("provider_type", "")
            if provider in Embedder.PROVIDER_MODELS:
                for model in Embedder.PROVIDER_MODELS[provider]:
                    sources.append({
                        "id": f"{ep['id']}/{model['id']}",
                        "endpoint_id": ep["id"],
                        "name": f"{ep['name']} {model['id']}",
                        "dimensions": model["dimensions"],
                        "type": "api",
                    })
            elif provider in ("openrouter", "together"):
                sources.append({
                    "id": f"{ep['id']}/default-embed",
                    "endpoint_id": ep["id"],
                    "name": f"{ep['name']} Embeddings",
                    "dimensions": None,
                    "type": "api",
                })

        # Check for local sentence-transformers
        try:
            import sentence_transformers  # noqa: F401
            sources.append({
                "id": "local/all-MiniLM-L6-v2",
                "endpoint_id": None,
                "name": "Local: all-MiniLM-L6-v2",
                "dimensions": 384,
                "type": "local",
            })
            sources.append({
                "id": "local/all-mpnet-base-v2",
                "endpoint_id": None,
                "name": "Local: all-mpnet-base-v2",
                "dimensions": 768,
                "type": "local",
            })
        except ImportError:
            pass

        return sources

    @staticmethod
    async def embed_local(
        texts: List[str], model_name: str = "all-MiniLM-L6-v2"
    ) -> Dict[str, Any]:
        """Generate embeddings using local sentence-transformers."""
        from sentence_transformers import SentenceTransformer

        model = SentenceTransformer(model_name)
        embeddings = model.encode(texts).tolist()
        return {
            "embeddings": embeddings,
            "dimensions": len(embeddings[0]) if embeddings else 0,
            "source": f"local/{model_name}",
        }

    @staticmethod
    async def embed_api(
        texts: List[str],
        endpoint: Dict[str, Any],
        model_id: Optional[str] = None,
        timeout: float = 60.0,
    ) -> Dict[str, Any]:
        """Generate embeddings using an API endpoint."""
        headers = {"Content-Type": "application/json"}
        auth_header = endpoint.get("auth_header", "Authorization")
        auth_prefix = endpoint.get("auth_prefix", "Bearer")
        api_key = endpoint.get("api_key", "")

        if auth_prefix:
            headers[auth_header] = f"{auth_prefix} {api_key}"
        else:
            headers[auth_header] = api_key
        for k, v in endpoint.get("extra_headers", {}).items():
            headers[k] = v

        # Determine embedding model
        if not model_id:
            provider = endpoint.get("provider_type", "")
            if provider == "openai":
                model_id = "text-embedding-3-small"
            elif provider == "mistral":
                model_id = "mistral-embed"
            else:
                model_id = "text-embedding-3-small"

        url = f"{endpoint['base_url']}/embeddings"

        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.post(url, headers=headers, json={
                "model": model_id,
                "input": texts,
            })
            data = response.json()

        embeddings = [item["embedding"] for item in data.get("data", [])]
        return {
            "embeddings": embeddings,
            "dimensions": len(embeddings[0]) if embeddings else 0,
            "source": f"{endpoint['id']}/{model_id}",
        }

    @staticmethod
    def auto_select_endpoint(
        endpoints: List[Dict[str, Any]],
    ) -> Optional[str]:
        """Auto-select the best embedding endpoint. Prefers OpenAI, then Mistral."""
        selected = None
        for ep in endpoints:
            if ep.get("enabled") and ep.get("api_key"):
                if ep["provider_type"] == "openai":
                    return ep["id"]
                elif ep["provider_type"] == "mistral" and not selected:
                    selected = ep["id"]
        return selected
