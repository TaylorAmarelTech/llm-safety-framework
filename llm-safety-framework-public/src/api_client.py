"""
Unified API client for all LLM providers.

Handles OpenAI-compatible (OpenAI, Mistral, Together, OpenRouter, custom)
and Anthropic format endpoints through a single interface.
"""

from typing import List, Dict, Any, Optional

import httpx


class UnifiedAPIClient:
    """
    Unified client for calling LLM endpoints.

    Supports:
    - OpenAI-compatible: OpenAI, Mistral, Together, OpenRouter, custom
    - Anthropic: Different body structure and auth header
    """

    def __init__(self, endpoint: Dict[str, Any], timeout: float = 60.0):
        self.endpoint = endpoint
        self.timeout = timeout

    def _build_headers(self) -> Dict[str, str]:
        """Build request headers from endpoint config."""
        headers = {"Content-Type": "application/json"}
        ep = self.endpoint

        auth_header = ep.get("auth_header", "Authorization")
        auth_prefix = ep.get("auth_prefix", "Bearer")
        api_key = (ep.get("api_key") or "").strip()

        if auth_prefix:
            headers[auth_header] = f"{auth_prefix} {api_key}"
        else:
            headers[auth_header] = api_key

        for k, v in ep.get("extra_headers", {}).items():
            headers[k] = v

        return headers

    async def chat(
        self,
        model_id: str,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 1024,
        system_prompt: Optional[str] = None,
        top_p: Optional[float] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
    ) -> str:
        """
        Send a chat completion request to the endpoint.

        Returns the response text content.
        """
        ep = self.endpoint
        request_format = ep.get("request_format", "openai")
        headers = self._build_headers()

        if request_format == "anthropic":
            return await self._chat_anthropic(
                headers, model_id, messages, temperature, max_tokens,
                system_prompt,
            )
        else:
            return await self._chat_openai(
                headers, model_id, messages, temperature, max_tokens,
                system_prompt, top_p, frequency_penalty, presence_penalty,
            )

    async def _chat_openai(
        self,
        headers: Dict[str, str],
        model_id: str,
        messages: List[Dict[str, str]],
        temperature: float,
        max_tokens: int,
        system_prompt: Optional[str],
        top_p: Optional[float],
        frequency_penalty: Optional[float],
        presence_penalty: Optional[float],
    ) -> str:
        """OpenAI-compatible chat completion."""
        ep = self.endpoint
        url = f"{ep['base_url']}/chat/completions"

        all_messages = list(messages)
        if system_prompt:
            all_messages.insert(0, {"role": "system", "content": system_prompt})

        body: Dict[str, Any] = {
            "model": model_id,
            "messages": all_messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }

        if top_p is not None:
            body["top_p"] = top_p
        if frequency_penalty is not None:
            body["frequency_penalty"] = frequency_penalty
        if presence_penalty is not None:
            body["presence_penalty"] = presence_penalty

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(url, headers=headers, json=body)
            response.raise_for_status()
            data = response.json()

        return (
            data.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "")
        )

    async def _chat_anthropic(
        self,
        headers: Dict[str, str],
        model_id: str,
        messages: List[Dict[str, str]],
        temperature: float,
        max_tokens: int,
        system_prompt: Optional[str],
    ) -> str:
        """Anthropic chat completion."""
        ep = self.endpoint
        url = f"{ep['base_url']}/v1/messages"

        body: Dict[str, Any] = {
            "model": model_id,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }

        if system_prompt:
            body["system"] = system_prompt

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(url, headers=headers, json=body)
            response.raise_for_status()
            data = response.json()

        content = data.get("content", [])
        if content and isinstance(content, list):
            return content[0].get("text", "")
        return ""

    async def embeddings(
        self,
        model_id: str,
        texts: List[str],
    ) -> List[List[float]]:
        """Generate embeddings for a list of texts."""
        ep = self.endpoint
        url = f"{ep['base_url']}/embeddings"
        headers = self._build_headers()

        body = {
            "model": model_id,
            "input": texts,
        }

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(url, headers=headers, json=body)
            response.raise_for_status()
            data = response.json()

        return [item["embedding"] for item in data.get("data", [])]

    def preview_request(
        self,
        model_id: str = "example-model",
    ) -> Dict[str, Any]:
        """Generate a preview of what the API call would look like."""
        ep = self.endpoint
        headers = {}

        if ep.get("auth_prefix"):
            headers[ep["auth_header"]] = f"{ep['auth_prefix']} <API_KEY>"
        else:
            headers[ep["auth_header"]] = "<API_KEY>"
        headers["Content-Type"] = "application/json"
        for k, v in ep.get("extra_headers", {}).items():
            headers[k] = v

        request_format = ep.get("request_format", "openai")

        if request_format == "anthropic":
            url = f"{ep['base_url']}/v1/messages"
            body = {
                "model": model_id,
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": "<prompt>"}],
            }
        else:
            url = f"{ep['base_url']}/chat/completions"
            body = {
                "model": model_id,
                "max_tokens": 1024,
                "temperature": 0.7,
                "messages": [{"role": "user", "content": "<prompt>"}],
            }

        return {
            "method": "POST",
            "url": url,
            "headers": headers,
            "body": body,
        }
