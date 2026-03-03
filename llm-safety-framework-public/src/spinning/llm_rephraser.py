"""
LLM-based prompt rephrasing.

Uses configured API endpoints to generate prompt variations.
"""

from typing import List, Dict, Any, Optional

from ..api_client import UnifiedAPIClient


class LLMRephraser:
    """Rephrase prompts using an LLM endpoint."""

    def __init__(self, endpoint: Dict[str, Any], model_id: str):
        self.client = UnifiedAPIClient(endpoint)
        self.model_id = model_id

    async def rephrase(
        self,
        prompt: str,
        instructions: str = "Rephrase this prompt while preserving the original intent and meaning.",
        count: int = 3,
        temperature: float = 0.9,
        max_tokens: int = 1024,
    ) -> List[str]:
        """
        Generate multiple rephrased variations of a prompt.

        Returns a list of rephrased prompts.
        """
        variations = []
        for _ in range(count):
            rephrase_prompt = (
                f"{instructions}\n\n"
                f"Original prompt:\n{prompt}\n\n"
                f"Rephrased version:"
            )
            try:
                rephrased = await self.client.chat(
                    model_id=self.model_id,
                    messages=[{"role": "user", "content": rephrase_prompt}],
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                variations.append(rephrased.strip())
            except Exception as e:
                variations.append(f"[Error: {str(e)}]")
        return variations

    async def rephrase_batch(
        self,
        prompts: List[str],
        instructions: str = "Rephrase this prompt while preserving the original intent and meaning.",
        count_per_prompt: int = 3,
        temperature: float = 0.9,
        max_tokens: int = 1024,
    ) -> List[Dict[str, Any]]:
        """
        Rephrase multiple prompts, returning original + variations for each.
        """
        results = []
        for prompt in prompts:
            variations = await self.rephrase(
                prompt, instructions, count_per_prompt, temperature, max_tokens,
            )
            results.append({"original": prompt, "variations": variations})
        return results
