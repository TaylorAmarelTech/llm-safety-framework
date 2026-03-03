"""
Adapter for Microsoft's PyRIT (Python Risk Identification Toolkit).

Exposes PyRIT's prompt converters (encoding transformations) through
a unified interface. Converters transform prompts into adversarial
variants using techniques like ASCII art, Atbash cipher, Morse code, etc.
"""

from typing import Any, Dict, List


# Known converters to expose when PyRIT is available
KNOWN_CONVERTERS = [
    {"id": "ascii_art", "name": "ASCII Art", "description": "Convert text to ASCII art representation"},
    {"id": "atbash_cipher", "name": "Atbash Cipher", "description": "Encode using Atbash cipher (reverse alphabet)"},
    {"id": "morse_code", "name": "Morse Code", "description": "Convert text to Morse code"},
    {"id": "base64_encode", "name": "Base64 Encode", "description": "Encode text as Base64"},
    {"id": "caesar_cipher", "name": "Caesar Cipher", "description": "Shift letters by a fixed amount"},
    {"id": "leetspeak", "name": "Leetspeak", "description": "Convert to 1337speak character substitutions"},
    {"id": "unicode_confusable", "name": "Unicode Confusable", "description": "Replace characters with visually similar Unicode"},
    {"id": "rot13", "name": "ROT13", "description": "Apply ROT13 rotation cipher"},
]

CONVERTER_MAP = {
    "ascii_art": "AsciiArtConverter",
    "atbash_cipher": "AtbashCipherConverter",
    "morse_code": "MorseCodeConverter",
    "base64_encode": "Base64Converter",
    "caesar_cipher": "CaesarCipherConverter",
    "leetspeak": "LeetspeakConverter",
    "unicode_confusable": "UnicodeConfusableConverter",
    "rot13": "ROT13Converter",
}


class PyRITAdapter:
    """Adapter for PyRIT library."""

    @staticmethod
    def is_available() -> bool:
        try:
            import pyrit  # type: ignore  # noqa: F401
            return True
        except ImportError:
            return False

    @staticmethod
    def get_info() -> Dict[str, Any]:
        if not PyRITAdapter.is_available():
            return {"installed": False}
        import pyrit  # type: ignore
        version = getattr(pyrit, "__version__", "unknown")
        return {
            "installed": True,
            "version": version,
            "name": "pyrit",
            "description": "Microsoft Python Risk Identification Toolkit for AI",
            "converter_count": len(KNOWN_CONVERTERS),
        }

    @staticmethod
    def list_converters() -> List[Dict[str, Any]]:
        """List available PyRIT converters."""
        if not PyRITAdapter.is_available():
            return KNOWN_CONVERTERS  # Return metadata even if not installed
        return KNOWN_CONVERTERS

    @staticmethod
    async def convert(converter_id: str, prompts: List[str], **opts) -> List[str]:
        """Apply a PyRIT converter to prompts."""
        if not PyRITAdapter.is_available():
            return prompts
        class_name = CONVERTER_MAP.get(converter_id)
        if not class_name:
            return prompts
        try:
            from pyrit.prompt_converter import PromptConverter  # type: ignore
            import importlib
            mod = importlib.import_module("pyrit.prompt_converter")
            converter_cls = getattr(mod, class_name, None)
            if converter_cls is None:
                return prompts
            converter: PromptConverter = converter_cls(**opts)
            results = []
            for p in prompts:
                converted = await converter.convert_async(prompt=p)
                results.append(converted.output_text if hasattr(converted, "output_text") else str(converted))
            return results
        except Exception:
            return prompts
