"""
Custom user-defined augmentation.

Simple text transformations: prefix, suffix, find/replace.
"""

from typing import List, Dict


class CustomAugmenter:
    """Apply user-defined text transformations to prompts."""

    @staticmethod
    def augment(
        prompts: List[str],
        prefix: str = "",
        suffix: str = "",
        find_replace: List[Dict[str, str]] = None,
    ) -> List[str]:
        """
        Apply custom augmentation to a list of prompts.

        Args:
            prompts: Source prompts
            prefix: Text to prepend
            suffix: Text to append
            find_replace: List of {"find": "...", "replace": "..."} dicts
        """
        if find_replace is None:
            find_replace = []

        results = []
        for prompt in prompts:
            modified = prompt
            for fr in find_replace:
                find = fr.get("find", "")
                replace = fr.get("replace", "")
                if find:
                    modified = modified.replace(find, replace)
            if prefix:
                modified = prefix + modified
            if suffix:
                modified = modified + suffix
            results.append(modified)
        return results
