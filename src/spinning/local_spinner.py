"""
Local spinning operations: spintax, regex, character padding.

No external API calls required.
"""

import re
import random
from typing import List, Dict


class LocalSpinner:
    """Handles spintax expansion, regex replacement, and character padding."""

    @staticmethod
    def expand_spintax(template: str, count: int = 10) -> List[str]:
        """
        Expand a spintax template into multiple unique prompts.

        Syntax: {option1|option2|option3} with nesting support.
        """
        pattern = r'\{([^{}]+)\}'
        results = []
        seen = set()
        max_attempts = count * 10

        for _ in range(max_attempts):
            if len(results) >= count:
                break
            text = template
            while re.search(pattern, text):
                def _pick(match: re.Match) -> str:
                    options = match.group(1).split('|')
                    return random.choice(options)
                text = re.sub(pattern, _pick, text)
            if text not in seen:
                seen.add(text)
                results.append(text)

        return results

    @staticmethod
    def regex_replace(prompts: List[str], patterns: List[Dict[str, str]]) -> List[str]:
        """
        Apply regex find-replace patterns to a list of prompts.

        Each pattern dict has 'find' and 'replace' keys.
        """
        results = []
        for prompt in prompts:
            modified = prompt
            for pattern in patterns:
                find = pattern.get("find", "")
                replace = pattern.get("replace", "")
                if find:
                    modified = re.sub(find, replace, modified)
            results.append(modified)
        return results

    @staticmethod
    def char_padding(
        prompts: List[str],
        padding_chars: str = " ",
        padding_count: int = 0,
        trailing_chars: str = "",
        insert_zero_width: bool = False,
    ) -> List[str]:
        """
        Apply character padding and trailing to prompts.

        Options:
        - padding_chars/count: prepend characters
        - trailing_chars: append characters
        - insert_zero_width: insert zero-width spaces between chars
        """
        results = []
        for prompt in prompts:
            modified = prompt
            if padding_count > 0:
                modified = (padding_chars * padding_count) + modified
            if trailing_chars:
                modified = modified + trailing_chars
            if insert_zero_width:
                modified = '\u200b'.join(modified)
            results.append(modified)
        return results

    @staticmethod
    def count_spintax_combinations(template: str) -> int:
        """Count the total number of unique combinations in a spintax template."""
        pattern = r'\{([^{}]+)\}'
        total = 1
        for match in re.finditer(pattern, template):
            options = match.group(1).split('|')
            total *= len(options)
        return total
