"""
Output Filter Evasion — Companion Decoders

Each decoder reverses the encoding that its corresponding output_evasion
mutator instructed the LLM to apply.  Use ``auto_decode()`` to dispatch
automatically based on the ``metadata`` dict stored in a MutationResult.

Usage:
    from src.prompt_injection.output_decoders import auto_decode

    decoded = auto_decode(llm_response, mutation_result.metadata)
"""

from __future__ import annotations

import base64
import json
import re
from typing import Any


class OutputDecoder:
    """Static methods for decoding each output-evasion strategy."""

    # ------------------------------------------------------------------
    # Family 1 — Symbol Substitution
    # ------------------------------------------------------------------

    @staticmethod
    def decode_symbol_replace(text: str, mapping: dict[str, str]) -> str:
        """Reverse a symbol-replacement mapping.

        *mapping* is ``{original_char: replacement_string}``.  We replace
        every occurrence of the replacement string back to the original char.
        """
        result = text
        # Sort by longest replacement first to avoid partial matches
        for orig, repl in sorted(mapping.items(), key=lambda kv: -len(kv[1])):
            result = result.replace(repl, orig)
        return result

    @staticmethod
    def decode_delimiter(text: str, delimiter: str) -> str:
        """Split on *delimiter* and rejoin with spaces."""
        return " ".join(
            part.strip() for part in text.split(delimiter) if part.strip()
        )

    @staticmethod
    def decode_char_spread(text: str, spread: int, noise: str = "*") -> str:
        """Extract every *spread*-th character (real chars), skip noise.

        The encoding places ``spread - 1`` noise chars between each real char.
        So the real chars are at indices 0, spread, 2*spread, ...
        """
        if spread < 1:
            return text
        return text[::spread]

    # ------------------------------------------------------------------
    # Family 2 — Polyglot / Multilingual Interleave
    # ------------------------------------------------------------------

    @staticmethod
    def decode_polyglot(
        text: str,
        target_lang: str,
        lang_sequence: list[str],
    ) -> str:
        """Extract words at positions whose language matches *target_lang*.

        The LLM was told to cycle through *lang_sequence*; we extract words
        whose position modulo ``len(lang_sequence)`` corresponds to
        *target_lang*.
        """
        try:
            target_idx = lang_sequence.index(target_lang)
        except ValueError:
            return text  # Can't decode, return as-is
        words = text.split()
        cycle = len(lang_sequence)
        return " ".join(
            w for i, w in enumerate(words) if i % cycle == target_idx
        )

    @staticmethod
    def decode_language_raster(text: str, target_row: int) -> str:
        """Extract the target row from a grid-formatted response."""
        lines = [ln.strip() for ln in text.strip().splitlines() if ln.strip()]
        if target_row < len(lines):
            return lines[target_row]
        return text

    @staticmethod
    def decode_translation_sandwich(
        text: str, offset: int, step: int
    ) -> str:
        """Extract every *step*-th line starting at *offset*."""
        lines = [ln.strip() for ln in text.strip().splitlines() if ln.strip()]
        return " ".join(lines[offset::step])

    # ------------------------------------------------------------------
    # Family 3 — Steganographic
    # ------------------------------------------------------------------

    @staticmethod
    def decode_first_letter_steg(text: str) -> str:
        """Extract the first letter of each word."""
        words = text.split()
        return "".join(w[0] for w in words if w)

    @staticmethod
    def decode_nth_word(text: str, n: int, offset: int = 0) -> str:
        """Extract every *n*-th word starting from *offset*."""
        words = text.split()
        if n < 1:
            return text
        return " ".join(words[offset::n])

    @staticmethod
    def decode_paragraph_initial(text: str) -> str:
        """Extract the first word of each sentence."""
        sentences = re.split(r"[.!?]\s+|\n+", text.strip())
        first_words = []
        for s in sentences:
            s = s.strip()
            if s:
                first_word = s.split()[0] if s.split() else ""
                if first_word:
                    first_words.append(first_word)
        return " ".join(first_words)

    # ------------------------------------------------------------------
    # Family 4 — Numeric / Cipher
    # ------------------------------------------------------------------

    @staticmethod
    def decode_a1z26(
        text: str,
        letter_sep: str = " ",
        word_sep: str = "-",
    ) -> str:
        """Decode A1Z26 cipher (1=A, 2=B, ..., 26=Z).

        Default format: numbers separated by spaces, words by dashes.
        Also handles comma/semicolon variants.
        """
        words = text.strip().split(word_sep)
        decoded_words = []
        for word in words:
            word = word.strip()
            if not word:
                continue
            nums = re.findall(r"\d+", word)
            letters = []
            for n in nums:
                val = int(n)
                if 1 <= val <= 26:
                    letters.append(chr(val + 64))  # 1->A, 26->Z
            decoded_words.append("".join(letters))
        return " ".join(decoded_words)

    @staticmethod
    def decode_substitution_cipher(
        text: str, cipher_map: dict[str, str]
    ) -> str:
        """Apply inverse of the substitution cipher.

        *cipher_map* is the **inverse** map: ``{cipher_letter: plain_letter}``.
        """
        result = []
        for ch in text:
            upper = ch.upper()
            if upper in cipher_map:
                decoded = cipher_map[upper]
                result.append(decoded.lower() if ch.islower() else decoded)
            else:
                result.append(ch)
        return "".join(result)

    @staticmethod
    def decode_coordinates(
        text: str, grid: list[list[str]]
    ) -> str:
        """Decode (row,col) coordinate pairs back to characters."""
        pairs = re.findall(r"\((\d+)\s*,\s*(\d+)\)", text)
        result = []
        for r_str, c_str in pairs:
            r, c = int(r_str), int(c_str)
            if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
                result.append(grid[r][c])
        # Handle word separators (" / " in the encoding scheme)
        decoded = "".join(result)
        return decoded

    # ------------------------------------------------------------------
    # Family 5 — Format Confusion
    # ------------------------------------------------------------------

    @staticmethod
    def decode_multicolumn(col1: str, col2: str) -> str:
        """Interleave two columns back into the original string."""
        result = []
        for i in range(max(len(col1), len(col2))):
            if i < len(col1):
                result.append(col1[i])
            if i < len(col2):
                result.append(col2[i])
        return "".join(result)

    @staticmethod
    def decode_nested_format(text: str, layers: list[str]) -> str:
        """Unwrap nested format layers in reverse order.

        *layers* is the list of formats applied (in order). We reverse them
        and strip each layer off.
        """
        current = text.strip()
        for layer in reversed(layers):
            if layer == "base64":
                try:
                    current = base64.b64decode(current).decode("utf-8", errors="replace")
                except Exception:
                    pass  # Can't decode, leave as-is
            elif layer == "json":
                try:
                    parsed = json.loads(current)
                    if isinstance(parsed, dict) and "data" in parsed:
                        current = str(parsed["data"])
                    elif isinstance(parsed, str):
                        current = parsed
                except (json.JSONDecodeError, TypeError):
                    pass
            elif layer == "xml":
                match = re.search(r"<data>(.*?)</data>", current, re.DOTALL)
                if match:
                    current = match.group(1).strip()
        return current

    # ------------------------------------------------------------------
    # Family 6 — Historical Ciphers
    # ------------------------------------------------------------------

    @staticmethod
    def decode_caesar(text: str, shift: int) -> str:
        """Reverse Caesar cipher by shifting each letter BACK by *shift*.

        Non-alpha characters are preserved unchanged.  Handles wraparound
        (e.g. A shifted back by 3 yields X).
        """
        result = []
        for ch in text:
            if ch.isalpha():
                base = ord("A") if ch.isupper() else ord("a")
                result.append(chr((ord(ch) - base - shift) % 26 + base))
            else:
                result.append(ch)
        return "".join(result)

    @staticmethod
    def decode_atbash(text: str) -> str:
        """Atbash cipher (self-inverse).  A<->Z, B<->Y, C<->X, ...

        Preserves case and non-alpha characters.
        """
        result = []
        for ch in text:
            if ch.isalpha():
                if ch.isupper():
                    result.append(chr(ord("Z") - (ord(ch) - ord("A"))))
                else:
                    result.append(chr(ord("z") - (ord(ch) - ord("a"))))
            else:
                result.append(ch)
        return "".join(result)

    @staticmethod
    def decode_vigenere(text: str, keyword: str) -> str:
        """Reverse Vigenere cipher.

        For each letter in *text*, subtract the corresponding key letter's
        position (A=0, B=1, ..., Z=25).  The keyword repeats cyclically.
        Non-alpha characters are preserved; key position only advances on
        alpha characters.
        """
        if not keyword:
            return text
        keyword_upper = keyword.upper()
        key_len = len(keyword_upper)
        result = []
        key_idx = 0
        for ch in text:
            if ch.isalpha():
                shift = ord(keyword_upper[key_idx % key_len]) - ord("A")
                base = ord("A") if ch.isupper() else ord("a")
                result.append(chr((ord(ch) - base - shift) % 26 + base))
                key_idx += 1
            else:
                result.append(ch)
        return "".join(result)

    @staticmethod
    def decode_rail_fence(text: str, rails: int) -> str:
        """Reverse rail fence cipher.

        Given the concatenated rows of a rail-fence zigzag, reconstruct the
        original plaintext.
        """
        if rails < 2 or not text:
            return text

        n = len(text)
        # Compute the length of each rail
        rail_lengths = [0] * rails
        rail = 0
        direction = 1
        for _ in range(n):
            rail_lengths[rail] += 1
            if rail == 0:
                direction = 1
            elif rail == rails - 1:
                direction = -1
            rail += direction

        # Split the ciphertext into rail segments
        rail_strings: list[list[str]] = []
        idx = 0
        for length in rail_lengths:
            rail_strings.append(list(text[idx: idx + length]))
            idx += length

        # Read off in zigzag order
        rail_indices = [0] * rails
        result = []
        rail = 0
        direction = 1
        for _ in range(n):
            ri = rail_indices[rail]
            if ri < len(rail_strings[rail]):
                result.append(rail_strings[rail][ri])
                rail_indices[rail] += 1
            if rail == 0:
                direction = 1
            elif rail == rails - 1:
                direction = -1
            rail += direction

        return "".join(result)

    @staticmethod
    def decode_enigma_simple(
        text: str, consonant_shift: int = 2, vowel_shift: int = 3
    ) -> str:
        """Reverse vowel/consonant-specific shifts.

        The encoder shifts consonants forward by *consonant_shift* and vowels
        by *vowel_shift*.  To decode we must determine whether the *original*
        character was a vowel or consonant — not the encoded one.  We try both
        shifts and pick the one whose result matches its expected type.
        """
        vowels = set("AEIOUaeiou")
        result = []
        for ch in text:
            if ch.isalpha():
                base = ord("A") if ch.isupper() else ord("a")
                as_cons = chr((ord(ch) - base - consonant_shift) % 26 + base)
                as_vowel = chr((ord(ch) - base - vowel_shift) % 26 + base)
                if as_vowel in vowels:
                    result.append(as_vowel)
                else:
                    result.append(as_cons)
            else:
                result.append(ch)
        return "".join(result)

    # ------------------------------------------------------------------
    # Family 7 — Technical Formats
    # ------------------------------------------------------------------

    @staticmethod
    def decode_nato(text: str) -> str:
        """Decode NATO phonetic alphabet back to letters.

        Words like "Alpha Bravo Charlie" become "ABC".  "BREAK" is treated
        as a space separator.
        """
        nato_map: dict[str, str] = {
            "ALFA": "A", "ALPHA": "A", "BRAVO": "B", "CHARLIE": "C",
            "DELTA": "D", "ECHO": "E", "FOXTROT": "F", "GOLF": "G",
            "HOTEL": "H", "INDIA": "I", "JULIET": "J", "JULIETT": "J",
            "KILO": "K", "LIMA": "L", "MIKE": "M", "NOVEMBER": "N",
            "OSCAR": "O", "PAPA": "P", "QUEBEC": "Q", "ROMEO": "R",
            "SIERRA": "S", "TANGO": "T", "UNIFORM": "U", "VICTOR": "V",
            "WHISKEY": "W", "XRAY": "X", "X-RAY": "X", "YANKEE": "Y",
            "ZULU": "Z",
        }
        result = []
        for token in text.split():
            upper = token.strip(".,;:!?").upper()
            if upper == "BREAK":
                result.append(" ")
            elif upper in nato_map:
                result.append(nato_map[upper])
            # Skip unrecognized tokens
        return "".join(result)

    @staticmethod
    def decode_braille(text: str) -> str:
        """Decode Unicode Braille characters (U+2801 .. U+283F) to ASCII.

        Uses the standard Braille mapping for letters a-z, digits 0-9,
        and common punctuation.  Unrecognized characters pass through.
        """
        braille_map: dict[str, str] = {
            "\u2801": "a", "\u2803": "b", "\u2809": "c", "\u2819": "d",
            "\u2811": "e", "\u280b": "f", "\u281b": "g", "\u2813": "h",
            "\u280a": "i", "\u281a": "j", "\u2805": "k", "\u2807": "l",
            "\u280d": "m", "\u281d": "n", "\u2815": "o", "\u280f": "p",
            "\u281f": "q", "\u2817": "r", "\u280e": "s", "\u281e": "t",
            "\u2825": "u", "\u2827": "v", "\u283a": "w", "\u282d": "x",
            "\u283d": "y", "\u2835": "z",
            # Number indicator (⠼) followed by a-j => 1-0
            "\u283c": "#NUM",  # number indicator — handled below
            # Space
            "\u2800": " ",
        }
        # Letter-to-digit mapping when preceded by number indicator
        letter_digit: dict[str, str] = {
            "a": "1", "b": "2", "c": "3", "d": "4", "e": "5",
            "f": "6", "g": "7", "h": "8", "i": "9", "j": "0",
        }
        result = []
        num_mode = False
        for ch in text:
            mapped = braille_map.get(ch)
            if mapped == "#NUM":
                num_mode = True
                continue
            if mapped is not None:
                if num_mode and mapped in letter_digit:
                    result.append(letter_digit[mapped])
                else:
                    result.append(mapped)
                    if mapped == " ":
                        num_mode = False
            else:
                # Pass through non-Braille characters (newlines, spaces, etc.)
                result.append(ch)
                if ch in (" ", "\n"):
                    num_mode = False
        return "".join(result)

    @staticmethod
    def decode_morse_output(text: str) -> str:
        """Decode Morse code to text.

        Letters are separated by spaces, words by " / ".
        Example: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.." -> "HELLO WORLD"
        """
        morse_map: dict[str, str] = {
            ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
            "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
            "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
            ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
            "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
            "--..": "Z",
            "-----": "0", ".----": "1", "..---": "2", "...--": "3",
            "....-": "4", ".....": "5", "-....": "6", "--...": "7",
            "---..": "8", "----.": "9",
            ".-.-.-": ".", "--..--": ",", "..--..": "?", ".----.": "'",
            "-.-.--": "!", "-..-.": "/", "-.--.": "(", "-.--.-": ")",
            ".-...": "&", "---...": ":", "-.-.-.": ";", "-...-": "=",
            ".-.-.": "+", "-....-": "-", "..--.-": "_", ".-..-.": '"',
            "...-..-": "$", ".--.-.": "@",
        }
        words = text.strip().split(" / ")
        decoded_words = []
        for word in words:
            letters = word.strip().split()
            decoded_letters = []
            for code in letters:
                code = code.strip()
                if code in morse_map:
                    decoded_letters.append(morse_map[code])
            decoded_words.append("".join(decoded_letters))
        return " ".join(decoded_words)

    @staticmethod
    def decode_tap_code_output(text: str) -> str:
        """Decode tap code (row, col) pairs to letters.

        Uses a 5x5 grid where K is merged with C:
        Row 1: A B C D E
        Row 2: F G H I J
        Row 3: L M N O P
        Row 4: Q R S T U
        Row 5: V W X Y Z

        Pairs can be formatted as (row,col) separated by spaces or
        concatenated.  Words are separated by " / ".
        """
        grid = [
            ["A", "B", "C", "D", "E"],
            ["F", "G", "H", "I", "J"],
            ["L", "M", "N", "O", "P"],
            ["Q", "R", "S", "T", "U"],
            ["V", "W", "X", "Y", "Z"],
        ]
        words = text.strip().split("/")
        decoded_words = []
        for word in words:
            word = word.strip()
            pairs = re.findall(r"\((\d+)\s*,\s*(\d+)\)", word)
            decoded_letters = []
            for r_str, c_str in pairs:
                r, c = int(r_str) - 1, int(c_str) - 1  # 1-indexed to 0-indexed
                if 0 <= r < 5 and 0 <= c < 5:
                    decoded_letters.append(grid[r][c])
            decoded_words.append("".join(decoded_letters))
        return " ".join(decoded_words)

    @staticmethod
    def decode_dna(text: str) -> str:
        """Decode DNA doublet/triplet codes to letters.

        Primary mapping (doublets): AA=A, AT=B, AG=C, AC=D, TA=E, TT=F,
        TG=G, TC=H, GA=I, GT=J, GG=K, GC=L, CA=M, CT=N, CG=O, CC=P.
        Extended mapping (triplets): TAA=Q, TAT=R, TAG=S, TAC=T, TTA=U,
        TTT=V, TTG=W, TTC=X, TGA=Y, TGT=Z.

        Codons separated by spaces; words separated by " -- ".
        """
        doublet_map: dict[str, str] = {
            "AA": "A", "AT": "B", "AG": "C", "AC": "D",
            "TA": "E", "TT": "F", "TG": "G", "TC": "H",
            "GA": "I", "GT": "J", "GG": "K", "GC": "L",
            "CA": "M", "CT": "N", "CG": "O", "CC": "P",
        }
        triplet_map: dict[str, str] = {
            "TAA": "Q", "TAT": "R", "TAG": "S", "TAC": "T",
            "TTA": "U", "TTT": "V", "TTG": "W", "TTC": "X",
            "TGA": "Y", "TGT": "Z",
        }
        words = text.strip().split("--")
        decoded_words = []
        for word in words:
            codons = word.strip().split()
            decoded_letters = []
            for codon in codons:
                codon = codon.strip().upper()
                if codon in triplet_map:
                    decoded_letters.append(triplet_map[codon])
                elif codon in doublet_map:
                    decoded_letters.append(doublet_map[codon])
                # Skip unrecognized codons
            decoded_words.append("".join(decoded_letters))
        return " ".join(decoded_words)

    # ------------------------------------------------------------------
    # Family 8 — Narrative / Misdirection
    # ------------------------------------------------------------------

    @staticmethod
    def decode_list_initials(text: str) -> str:
        """Extract the first letter of each non-empty line.

        Strips leading numbers, bullets (*, -), and whitespace before
        extracting the initial letter.  Returns an uppercase string.
        Useful for recipe ingredients, playlist songs, weather cities,
        driving directions, etc.
        """
        result = []
        for line in text.strip().splitlines():
            line = line.strip()
            if not line:
                continue
            # Strip leading numbering (e.g. "1.", "1)", "12.")
            line = re.sub(r"^\d+[.)]\s*", "", line)
            # Strip leading bullets (*, -, +, >)
            line = re.sub(r"^[-*+>]\s*", "", line)
            line = line.strip()
            if line:
                result.append(line[0].upper())
        return "".join(result)

    @staticmethod
    def decode_dialogue_caps(text: str) -> str:
        """Extract ALL CAPS words (2+ letters, all uppercase) from text.

        Joins extracted words with spaces.
        """
        caps_words = re.findall(r"\b([A-Z]{2,})\b", text)
        return " ".join(caps_words)

    @staticmethod
    def decode_comments(text: str, comment_prefix: str = "#") -> str:
        """Extract lines starting with *comment_prefix*, strip the prefix, join.

        Useful for extracting hidden messages in code comments.
        """
        result = []
        for line in text.strip().splitlines():
            stripped = line.strip()
            if stripped.startswith(comment_prefix):
                content = stripped[len(comment_prefix):].strip()
                if content:
                    result.append(content)
        return " ".join(result)

    @staticmethod
    def decode_footnotes(text: str) -> str:
        """Extract text after footnote markers like [1], [2], ^1, ^2.

        Joins all footnote text with spaces.
        """
        # Match lines or inline markers: [N] or ^N followed by text
        footnote_pattern = re.compile(
            r"(?:^|\n)\s*(?:\[(\d+)\]|\^(\d+))\s*[:\-]?\s*(.+)",
        )
        matches = footnote_pattern.findall(text)
        result = []
        for m in matches:
            # m is a tuple (bracket_num, caret_num, text)
            footnote_text = m[2].strip()
            if footnote_text:
                result.append(footnote_text)
        return " ".join(result)

    @staticmethod
    def decode_json_messages(text: str) -> str:
        """Parse JSON and extract all ``"message"`` field values recursively.

        Joins all found message values with spaces.
        """

        def _extract_messages(obj: Any) -> list[str]:
            messages: list[str] = []
            if isinstance(obj, dict):
                for key, val in obj.items():
                    if key == "message" and isinstance(val, str):
                        messages.append(val)
                    else:
                        messages.extend(_extract_messages(val))
            elif isinstance(obj, list):
                for item in obj:
                    messages.extend(_extract_messages(item))
            return messages

        # Try to find JSON in the text (may be embedded in other text)
        # First try the whole text
        for candidate in [text.strip()]:
            try:
                parsed = json.loads(candidate)
                msgs = _extract_messages(parsed)
                if msgs:
                    return " ".join(msgs)
            except (json.JSONDecodeError, TypeError):
                pass

        # Try to find JSON object or array within the text
        for match in re.finditer(r"[\[{]", text):
            start = match.start()
            try:
                parsed = json.loads(text[start:])
                msgs = _extract_messages(parsed)
                if msgs:
                    return " ".join(msgs)
            except (json.JSONDecodeError, TypeError):
                continue

        return text

    @staticmethod
    def decode_mad_libs_key(text: str) -> str:
        """Extract text after a ``KEY:`` or ``Key:`` marker.

        Returns everything after the first KEY: marker up to the end of
        the text (or the next section marker).
        """
        match = re.search(r"(?:^|\n)\s*[Kk][Ee][Yy]\s*:\s*(.+)", text, re.DOTALL)
        if match:
            return match.group(1).strip()
        return text

    # ------------------------------------------------------------------
    # Family 9 — Word Order
    # ------------------------------------------------------------------

    @staticmethod
    def decode_outside_in(text: str) -> str:
        """Reverse outside-in word ordering.

        The encoded text has words placed at positions:
        [1st, last, 2nd, second-to-last, 3rd, ...].
        Reconstruct the original linear order.
        """
        words = text.split()
        n = len(words)
        if n <= 1:
            return text

        # The encoding placed original word i at a specific position.
        # Reverse: read pairs (front, back) and place them in order.
        original = [""] * n
        left = 0
        right = n - 1
        i = 0
        while i < n:
            original[left] = words[i]
            i += 1
            left += 1
            if i < n and left <= right:
                original[right] = words[i]
                i += 1
                right -= 1
        return " ".join(original)

    @staticmethod
    def decode_even_odd(text: str) -> str:
        """Given ``"odd_words --- even_words"``, interleave them back.

        Splits on ``---``, then weaves words from the odd group (positions
        0, 2, 4, ...) and even group (positions 1, 3, 5, ...) back together.
        """
        parts = text.split("---")
        if len(parts) < 2:
            return text
        odd_words = parts[0].strip().split()
        even_words = parts[1].strip().split()
        result = []
        max_len = max(len(odd_words), len(even_words))
        for i in range(max_len):
            if i < len(odd_words):
                result.append(odd_words[i])
            if i < len(even_words):
                result.append(even_words[i])
        return " ".join(result)

    @staticmethod
    def decode_reverse_sentences(text: str) -> str:
        """Reverse the order of sentences.

        Splits on sentence boundaries (``. ! ?`` followed by space or
        newline), reverses the order, and rejoins.
        """
        # Split while keeping the delimiters
        parts = re.split(r"([.!?])(\s+|\n+)", text.strip())
        # Reassemble into complete sentences
        sentences: list[str] = []
        current = ""
        for part in parts:
            current += part
            if re.match(r"[.!?]", part):
                continue
            if re.match(r"\s+|\n+", part) and current.strip():
                sentences.append(current)
                current = ""
        if current.strip():
            sentences.append(current)
        sentences.reverse()
        return "".join(sentences)

    # ------------------------------------------------------------------
    # Family 14 — Unicode Visual Transforms
    # ------------------------------------------------------------------

    @staticmethod
    def decode_upside_down(text: str) -> str:
        """Reverse string and map upside-down Unicode chars back to ASCII."""
        _REV = {
            '\u0250': 'a', '\u0254': 'c', '\u01DD': 'e',
            '\u025F': 'f', '\u0253': 'g', '\u0265': 'h', '\u0131': 'i', '\u027E': 'j',
            '\u029E': 'k', '\u026F': 'm',
            '\u0279': 'r', '\u0287': 't',
            '\u028C': 'v', '\u028D': 'w', '\u028E': 'y',
            '\u2200': 'A', '\u15FA': 'B', '\u2183': 'C', '\u15E1': 'D', '\u018E': 'E',
            '\u2132': 'F', '\u2141': 'G', '\u017F': 'J',
            '\u22CA': 'K', '\u2142': 'L', '\u0500': 'P',
            '\u038C': 'Q', '\u1D1A': 'R', '\u22A5': 'T', '\u2229': 'U',
            '\u039B': 'V', '\u2144': 'Y',
            '\u21C2': '1', '\u218A': '2', '\u218B': '3', '\u3123': '4',
            '\u078E': '5', '\u3125': '7',
            '\u02D9': '.', '\u2018': ',', '\u00BF': '?', '\u00A1': '!', '\u201E': '"',
        }
        return "".join(_REV.get(ch, ch) for ch in text[::-1])

    @staticmethod
    def decode_mirror(text: str) -> str:
        """Reverse string and map mirrored Unicode chars back to ASCII."""
        _REV = {
            '\u0252': 'a', '\u2184': 'c', '\u0258': 'e',
            '\u214E': 'f', '\u01E5': 'g', '\u04BB': 'h', '\u0244': 'j',
            '\u029E': 'k', '\u0438': 'n',
            '\u044F': 'r', '\u0455': 's', '\u0442': 't', '\u04AF': 'y',
            '\u2200': 'A', '\u15FA': 'B', '\u2183': 'C', '\u15E1': 'D',
            '\u042D': 'E', '\u2132': 'F', '\u2141': 'G', '\u017F': 'J',
            '\u22CA': 'K', '\u2143': 'L', '\u0418': 'N', '\u0500': 'P',
            '\u038C': 'Q', '\u042F': 'R', '\u0405': 'S', '\u01B8': 'Z',
            ')': '(', '(': ')', ']': '[', '[': ']', '}': '{', '{': '}',
            '>': '<', '<': '>', '\\': '/', '/': '\\',
        }
        return "".join(_REV.get(ch, ch) for ch in text[::-1])

    @staticmethod
    def decode_fullwidth(text: str) -> str:
        """Convert fullwidth Unicode chars back to ASCII."""
        result = []
        for ch in text:
            cp = ord(ch)
            if 0xFF01 <= cp <= 0xFF5E:
                result.append(chr(cp - 0xFEE0))
            elif cp == 0x3000:  # ideographic space
                result.append(' ')
            else:
                result.append(ch)
        return "".join(result)

    @staticmethod
    def decode_small_caps(text: str) -> str:
        """Convert Unicode small caps back to lowercase ASCII."""
        _REV = {
            '\u1D00': 'a', '\u0299': 'b', '\u1D04': 'c', '\u1D05': 'd',
            '\u1D07': 'e', '\uA730': 'f', '\u0262': 'g', '\u029C': 'h',
            '\u026A': 'i', '\u1D0A': 'j', '\u1D0B': 'k', '\u029F': 'l',
            '\u1D0D': 'm', '\u0274': 'n', '\u1D0F': 'o', '\u1D18': 'p',
            '\u0280': 'r', '\u0455': 's', '\u1D1B': 't',
            '\u1D1C': 'u', '\u1D20': 'v', '\u1D21': 'w',
            '\u028F': 'y', '\u1D22': 'z',
        }
        return "".join(_REV.get(ch, ch) for ch in text)

    @staticmethod
    def decode_circled(text: str) -> str:
        """Convert Unicode circled letters/digits back to ASCII."""
        result = []
        for ch in text:
            cp = ord(ch)
            if 0x24B6 <= cp <= 0x24CF:  # Ⓐ-Ⓩ uppercase
                result.append(chr(cp - 0x24B6 + ord('A')))
            elif 0x24D0 <= cp <= 0x24E9:  # ⓐ-ⓩ lowercase
                result.append(chr(cp - 0x24D0 + ord('a')))
            elif 0x2460 <= cp <= 0x2468:  # ①-⑨
                result.append(chr(cp - 0x2460 + ord('1')))
            elif cp == 0x24EA:  # ⓪
                result.append('0')
            else:
                result.append(ch)
        return "".join(result)

    @staticmethod
    def decode_math_bold(text: str) -> str:
        """Convert Unicode Mathematical Bold back to ASCII."""
        result = []
        for ch in text:
            cp = ord(ch)
            if 0x1D400 <= cp <= 0x1D419:  # 𝐀-𝐙
                result.append(chr(cp - 0x1D400 + ord('A')))
            elif 0x1D41A <= cp <= 0x1D433:  # 𝐚-𝐳
                result.append(chr(cp - 0x1D41A + ord('a')))
            elif 0x1D7CE <= cp <= 0x1D7D7:  # 𝟎-𝟗
                result.append(chr(cp - 0x1D7CE + ord('0')))
            else:
                result.append(ch)
        return "".join(result)

    @staticmethod
    def decode_fraktur(text: str) -> str:
        """Convert Unicode Fraktur back to ASCII."""
        _EXCEPTIONS_REV = {
            '\u212D': 'C', '\u210C': 'H', '\u2111': 'I', '\u211C': 'R', '\u2128': 'Z',
        }
        result = []
        for ch in text:
            if ch in _EXCEPTIONS_REV:
                result.append(_EXCEPTIONS_REV[ch])
                continue
            cp = ord(ch)
            if 0x1D504 <= cp <= 0x1D51B:  # 𝔄-𝔛 (uppercase, skipping exceptions)
                result.append(chr(cp - 0x1D504 + ord('A')))
            elif 0x1D51E <= cp <= 0x1D537:  # 𝔞-𝔷
                result.append(chr(cp - 0x1D51E + ord('a')))
            else:
                result.append(ch)
        return "".join(result)

    @staticmethod
    def decode_monospace(text: str) -> str:
        """Convert Unicode Mathematical Monospace back to ASCII."""
        result = []
        for ch in text:
            cp = ord(ch)
            if 0x1D670 <= cp <= 0x1D689:  # 𝙰-𝚉
                result.append(chr(cp - 0x1D670 + ord('A')))
            elif 0x1D68A <= cp <= 0x1D6A3:  # 𝚊-𝚣
                result.append(chr(cp - 0x1D68A + ord('a')))
            elif 0x1D7F6 <= cp <= 0x1D7FF:  # 𝟶-𝟿
                result.append(chr(cp - 0x1D7F6 + ord('0')))
            else:
                result.append(ch)
        return "".join(result)

    # ------------------------------------------------------------------
    # Family 15 — Byte-Level Encoding
    # ------------------------------------------------------------------

    @staticmethod
    def decode_binary_output(text: str) -> str:
        """Decode binary-encoded text (8-bit groups separated by spaces, words by newlines)."""
        words = text.strip().split('\n')
        decoded_words = []
        for word_line in words:
            bits = word_line.strip().split()
            chars = []
            for b in bits:
                b = b.strip()
                if b and all(c in '01' for c in b):
                    try:
                        chars.append(chr(int(b, 2)))
                    except ValueError:
                        pass
            if chars:
                decoded_words.append("".join(chars))
        return " ".join(decoded_words)

    @staticmethod
    def decode_octal_output(text: str) -> str:
        """Decode octal-encoded text (3-digit groups, words separated by /)."""
        words = text.strip().split('/')
        decoded_words = []
        for word_part in words:
            codes = word_part.strip().split()
            chars = []
            for c in codes:
                c = c.strip()
                if c:
                    try:
                        chars.append(chr(int(c, 8)))
                    except ValueError:
                        pass
            if chars:
                decoded_words.append("".join(chars))
        return " ".join(decoded_words)

    @staticmethod
    def decode_ascii_decimal(text: str) -> str:
        """Decode decimal ASCII codes (numbers separated by spaces, words by /)."""
        words = text.strip().split('/')
        decoded_words = []
        for word_part in words:
            codes = word_part.strip().split()
            chars = []
            for c in codes:
                c = c.strip()
                if c:
                    try:
                        chars.append(chr(int(c)))
                    except ValueError:
                        pass
            if chars:
                decoded_words.append("".join(chars))
        return " ".join(decoded_words)

    @staticmethod
    def decode_url_encode(text: str) -> str:
        """Decode percent-encoded URL text."""
        import urllib.parse
        return urllib.parse.unquote(text)

    @staticmethod
    def decode_html_entities(text: str) -> str:
        """Decode HTML character entities."""
        import html
        return html.unescape(text)

    @staticmethod
    def decode_unicode_escape(text: str) -> str:
        """Decode \\uXXXX escape sequences."""
        return re.sub(
            r'\\u([0-9a-fA-F]{4})',
            lambda m: chr(int(m.group(1), 16)),
            text,
        )

    # ------------------------------------------------------------------
    # Family 16 — Visual Layout
    # ------------------------------------------------------------------

    @staticmethod
    def decode_vertical(text: str) -> str:
        """Decode vertical text (one char per line, blank lines between words)."""
        blocks = text.strip().split('\n\n')
        words = []
        for block in blocks:
            chars = [line.strip() for line in block.strip().split('\n') if line.strip()]
            if chars:
                words.append("".join(chars))
        return " ".join(words)

    @staticmethod
    def decode_diagonal(text: str) -> str:
        """Decode diagonal text (strip leading whitespace from each line)."""
        lines = text.strip().split('\n')
        chars = []
        for line in lines:
            stripped = line.lstrip()
            if stripped == '/':
                chars.append(' ')
            elif stripped:
                chars.append(stripped[0] if len(stripped) == 1 else stripped)
        return "".join(chars)

    @staticmethod
    def decode_rtl_override(text: str) -> str:
        """Decode RTL-overridden text by stripping markers and reversing."""
        # Strip RTL Override (U+202E), Pop Directional (U+202C), RTL Mark (U+200F)
        cleaned = text.replace('\u202E', '').replace('\u202C', '').replace('\u200F', '')
        # Reverse each line
        lines = cleaned.split('\n')
        return '\n'.join(line[::-1] for line in lines)

    @staticmethod
    def decode_boustrophedon(text: str) -> str:
        """Decode boustrophedon text by reversing even-indexed lines (0-based)."""
        lines = text.strip().split('\n')
        result = []
        for i, line in enumerate(lines):
            if i % 2 == 1:  # Even lines in 1-based = odd in 0-based
                result.append(line[::-1])
            else:
                result.append(line)
        return '\n'.join(result)

    @staticmethod
    def decode_column_cipher(text: str, columns: int = 5) -> str:
        """Decode columnar transposition cipher."""
        col_strings = [c.strip() for c in text.split('|')]
        if not col_strings:
            return text
        max_len = max(len(c) for c in col_strings) if col_strings else 0
        # Pad shorter columns
        padded = [c.ljust(max_len) for c in col_strings]
        # Read row by row
        result = []
        for row in range(max_len):
            for col_str in padded:
                if row < len(col_str):
                    result.append(col_str[row])
        return "".join(result).rstrip()

    # ------------------------------------------------------------------
    # Family 17 — Language Games
    # ------------------------------------------------------------------

    @staticmethod
    def decode_pig_latin_output(text: str) -> str:
        """Heuristic Pig Latin decoder."""
        words = text.split()
        result = []
        for word in words:
            # Strip punctuation
            match = re.match(r'^([a-zA-Z]+)(.*)', word)
            if not match:
                result.append(word)
                continue
            letters, punct = match.groups()
            low = letters.lower()
            if low.endswith('way') and low[0] in 'aeiou':
                result.append(letters[:-3] + punct)
            elif low.endswith('ay') and len(low) > 2:
                # Find consonant cluster before 'ay'
                core = letters[:-2]  # Remove 'ay'
                # Try cluster lengths 1, 2, 3
                for cl in range(1, min(4, len(core))):
                    candidate = core[len(core)-cl:] + core[:len(core)-cl]
                    result.append(candidate + punct)
                    break
                else:
                    result.append(word)
            else:
                result.append(word)
        return " ".join(result)

    @staticmethod
    def decode_backwards_words(text: str) -> str:
        """Reverse each word individually."""
        return " ".join(word[::-1] for word in text.split())

    @staticmethod
    def decode_backwards_sentences(text: str) -> str:
        """Reverse word order within each sentence."""
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        result = []
        for sent in sentences:
            words = sent.split()
            result.append(" ".join(reversed(words)))
        return " ".join(result)

    # ------------------------------------------------------------------
    # Family 18 — Data Serialization
    # ------------------------------------------------------------------

    @staticmethod
    def decode_csv(text: str) -> str:
        """Extract cell values from CSV text."""
        import csv
        import io
        reader = csv.reader(io.StringIO(text.strip()))
        rows = list(reader)
        if len(rows) <= 1:
            return text
        # Skip header row, join all cell values
        values = []
        for row in rows[1:]:
            values.extend(cell.strip() for cell in row if cell.strip())
        return " ".join(values)

    @staticmethod
    def decode_xml(text: str) -> str:
        """Extract text content from XML leaf elements."""
        # Remove XML declaration
        text_clean = re.sub(r'<\?xml[^?]*\?>', '', text)
        # Extract text between tags (leaf elements)
        texts = re.findall(r'>([^<]+)<', text_clean)
        return " ".join(t.strip() for t in texts if t.strip())

    @staticmethod
    def decode_toml(text: str) -> str:
        """Extract string values from TOML-formatted text."""
        values = re.findall(r'=\s*"([^"]*)"', text)
        return " ".join(values)

    @staticmethod
    def decode_ini(text: str) -> str:
        """Extract values from INI-formatted text."""
        values = []
        for line in text.strip().split('\n'):
            line = line.strip()
            if line.startswith('[') or line.startswith(';') or not line:
                continue
            match = re.match(r'[^=]+=\s*(.*)', line)
            if match:
                values.append(match.group(1).strip())
        return " ".join(values)

    @staticmethod
    def decode_jsonlines(text: str) -> str:
        """Extract 'text' fields from JSON Lines."""
        values = []
        for line in text.strip().split('\n'):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                if isinstance(obj, dict):
                    values.append(obj.get('text', obj.get('content', str(obj))))
            except json.JSONDecodeError:
                pass
        return " ".join(str(v) for v in values)

    # ------------------------------------------------------------------
    # Family 19 — Numeric Systems
    # ------------------------------------------------------------------

    @staticmethod
    def decode_roman_positions(text: str) -> str:
        """Decode Roman numeral alphabet positions back to letters."""
        def roman_to_int(s: str) -> int:
            values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
            total = 0
            prev = 0
            for ch in reversed(s.upper()):
                val = values.get(ch, 0)
                if val < prev:
                    total -= val
                else:
                    total += val
                prev = val
            return total

        words = text.strip().split('/')
        decoded_words = []
        for word_part in words:
            numerals = word_part.strip().split()
            chars = []
            for num in numerals:
                num = num.strip()
                if num:
                    pos = roman_to_int(num)
                    if 1 <= pos <= 26:
                        chars.append(chr(pos - 1 + ord('A')))
            if chars:
                decoded_words.append("".join(chars))
        return " ".join(decoded_words)

    @staticmethod
    def decode_base32(text: str) -> str:
        """Decode Base32-encoded text."""
        # Clean up: remove spaces/newlines, ensure proper padding
        clean = text.strip().replace(' ', '').replace('\n', '')
        # Add padding if needed
        pad = len(clean) % 8
        if pad:
            clean += '=' * (8 - pad)
        try:
            return base64.b32decode(clean, casefold=True).decode('utf-8', errors='replace')
        except Exception:
            return text

    @staticmethod
    def decode_phone_keypad(text: str) -> str:
        """Decode phone keypad (digit*count) pairs."""
        _KEYPAD = {
            '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL',
            '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ',
        }
        words = text.strip().split('/')
        decoded_words = []
        for word_part in words:
            pairs = re.findall(r'(\d)\*(\d)', word_part)
            chars = []
            for digit, count in pairs:
                letters = _KEYPAD.get(digit, '')
                idx = int(count) - 1
                if 0 <= idx < len(letters):
                    chars.append(letters[idx])
            if chars:
                decoded_words.append("".join(chars))
        return " ".join(decoded_words)

    @staticmethod
    def decode_number_words(text: str) -> str:
        """Decode English number words to ASCII characters."""
        _ONES = {
            'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
            'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
            'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
            'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18,
            'nineteen': 19,
        }
        _TENS = {
            'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
            'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
        }

        def words_to_int(s: str) -> int:
            s = s.strip().lower().replace('-', ' ')
            parts = s.split()
            total = 0
            i = 0
            while i < len(parts):
                word = parts[i]
                if word in _ONES:
                    total += _ONES[word]
                elif word in _TENS:
                    total += _TENS[word]
                elif word == 'hundred':
                    total *= 100 if total > 0 else 100
                i += 1
            return total

        # Split by semicolons for words, commas for chars
        words = text.strip().split(';')
        decoded_words = []
        for word_part in words:
            chars = word_part.strip().split(',')
            decoded_chars = []
            for char_desc in chars:
                char_desc = char_desc.strip()
                if char_desc:
                    try:
                        code = words_to_int(char_desc)
                        if 32 <= code <= 126:
                            decoded_chars.append(chr(code))
                    except (ValueError, KeyError):
                        pass
            if decoded_chars:
                decoded_words.append("".join(decoded_chars))
        return " ".join(decoded_words)

    # ------------------------------------------------------------------
    # Family 20 — Artistic / Signal
    # ------------------------------------------------------------------

    @staticmethod
    def decode_semaphore(text: str) -> str:
        """Decode flag semaphore position descriptions."""
        _REV = {
            'L:7 R:6': 'A', 'L:8 R:6': 'B', 'L:9 R:6': 'C', 'L:12 R:6': 'D',
            'L:6 R:3': 'E', 'L:6 R:2': 'F', 'L:6 R:1': 'G', 'L:8 R:7': 'H',
            'L:9 R:7': 'I', 'L:12 R:3': 'J', 'L:7 R:12': 'K', 'L:7 R:9': 'L',
            'L:7 R:8': 'M', 'L:7 R:7': 'N', 'L:8 R:9': 'O', 'L:8 R:12': 'P',
            'L:8 R:3': 'Q', 'L:8 R:2': 'R', 'L:8 R:1': 'S', 'L:9 R:12': 'T',
            'L:9 R:3': 'U', 'L:12 R:1': 'V', 'L:3 R:2': 'W', 'L:3 R:1': 'X',
            'L:9 R:2': 'Y', 'L:3 R:6': 'Z',
        }
        words = text.strip().split('//')
        decoded_words = []
        for word_part in words:
            letters = word_part.strip().split('|')
            chars = []
            for letter_desc in letters:
                letter_desc = letter_desc.strip()
                ch = _REV.get(letter_desc)
                if ch:
                    chars.append(ch)
            if chars:
                decoded_words.append("".join(chars))
        return " ".join(decoded_words)

    @staticmethod
    def decode_letter_names(text: str) -> str:
        """Decode English letter names back to single characters."""
        _REV = {
            'ay': 'a', 'bee': 'b', 'cee': 'c', 'dee': 'd', 'ee': 'e',
            'ef': 'f', 'gee': 'g', 'aitch': 'h', 'eye': 'i', 'jay': 'j',
            'kay': 'k', 'el': 'l', 'em': 'm', 'en': 'n', 'oh': 'o',
            'pee': 'p', 'cue': 'q', 'ar': 'r', 'ess': 's', 'tee': 't',
            'you': 'u', 'vee': 'v', 'double-you': 'w', 'ex': 'x',
            'why': 'y', 'zee': 'z',
        }
        words = text.strip().split('|')
        decoded_words = []
        for word_part in words:
            names = word_part.strip().split()
            chars = []
            for name in names:
                name = name.strip().lower()
                ch = _REV.get(name)
                if ch:
                    chars.append(ch)
            if chars:
                decoded_words.append("".join(chars))
        return " ".join(decoded_words)

    # ------------------------------------------------------------------
    # Family 21 — Chunking & Signal Embedding
    # ------------------------------------------------------------------

    @staticmethod
    def decode_numbered_chunks(text: str) -> str:
        """Strip [N] prefixes and concatenate chunks in order."""
        chunks = re.findall(r'\[(\d+)\]\s*(.*?)(?=\[\d+\]|\Z)', text, re.DOTALL)
        if not chunks:
            return text
        sorted_chunks = sorted(chunks, key=lambda x: int(x[0]))
        return " ".join(chunk.strip() for _, chunk in sorted_chunks)

    @staticmethod
    def decode_alternating_case(text: str) -> str:
        """Normalize alternating case to standard lowercase."""
        return text.lower()

    @staticmethod
    def decode_paragraph_reverse(text: str) -> str:
        """Reverse paragraph order (split on [PN] markers or double newlines)."""
        # Try [PN] markers first
        parts = re.split(r'\[P\d+\]\s*', text.strip())
        parts = [p.strip() for p in parts if p.strip()]
        if len(parts) > 1:
            return "\n\n".join(reversed(parts))
        # Fall back to double-newline split
        parts = text.strip().split('\n\n')
        parts = [p.strip() for p in parts if p.strip()]
        return "\n\n".join(reversed(parts))

    @staticmethod
    def decode_interleaved_decoy(text: str) -> str:
        """Extract odd-numbered sentences (real content)."""
        # Try numbered format: (1) text (2) text ...
        numbered = re.findall(r'\((\d+)\)\s*(.*?)(?=\(\d+\)|\Z)', text, re.DOTALL)
        if numbered:
            return " ".join(
                sent.strip() for num, sent in numbered
                if int(num) % 2 == 1 and sent.strip()
            )
        # Fall back: split on sentence boundaries, take odd ones
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        return " ".join(s for i, s in enumerate(sentences) if i % 2 == 0)

    @staticmethod
    def decode_whitespace_binary(text: str) -> str:
        """Decode hidden message from single/double space patterns."""
        # Find all inter-word spaces (sequences of spaces)
        spaces = re.findall(r' +', text)
        bits = []
        for sp in spaces:
            if len(sp) >= 2:
                bits.append('1')
            else:
                bits.append('0')
        # Group into bytes
        chars = []
        for i in range(0, len(bits) - 7, 8):
            byte = "".join(bits[i:i+8])
            try:
                ch = chr(int(byte, 2))
                if 32 <= ord(ch) <= 126:
                    chars.append(ch)
            except ValueError:
                pass
        return "".join(chars)


# ---------------------------------------------------------------------------
# Auto-dispatch decoder
# ---------------------------------------------------------------------------

_DECODER_DISPATCH: dict[str, str | None] = {
    # Family 1 — Symbol Substitution
    "symbol_replace": "decode_symbol_replace",
    "delimiter": "decode_delimiter",
    "char_spread": "decode_char_spread",
    # Family 2 — Polyglot / Multilingual Interleave
    "polyglot": "decode_polyglot",
    "language_raster": "decode_language_raster",
    "translation_sandwich": "decode_translation_sandwich",
    # Family 3 — Steganographic
    "first_letter_steg": "decode_first_letter_steg",
    "nth_word": "decode_nth_word",
    "paragraph_initial": "decode_paragraph_initial",
    # Family 4 — Numeric / Cipher
    "a1z26": "decode_a1z26",
    "substitution_cipher": "decode_substitution_cipher",
    "coordinates": "decode_coordinates",
    # Family 5 — Format Confusion
    "multicolumn": "decode_multicolumn",
    "nested_format": "decode_nested_format",
    # Family 6 — Historical Ciphers
    "caesar": "decode_caesar",
    "atbash": "decode_atbash",
    "vigenere": "decode_vigenere",
    "rail_fence": "decode_rail_fence",
    "enigma_simple": "decode_enigma_simple",
    # Family 7 — Technical Formats
    "nato": "decode_nato",
    "braille": "decode_braille",
    "morse_output": "decode_morse_output",
    "tap_code": "decode_tap_code_output",
    "dna": "decode_dna",
    # Family 8 — Narrative / Misdirection
    "list_initials": "decode_list_initials",
    "dialogue_caps": "decode_dialogue_caps",
    "comments": "decode_comments",
    "footnotes": "decode_footnotes",
    "json_messages": "decode_json_messages",
    "mad_libs_key": "decode_mad_libs_key",
    # Family 9 — Word Order
    "outside_in": "decode_outside_in",
    "even_odd": "decode_even_odd",
    "reverse_sentences": "decode_reverse_sentences",
    # Family 14 — Unicode Visual Transforms
    "upside_down": "decode_upside_down",
    "mirror": "decode_mirror",
    "fullwidth": "decode_fullwidth",
    "small_caps": "decode_small_caps",
    "circled": "decode_circled",
    "math_bold": "decode_math_bold",
    "fraktur": "decode_fraktur",
    "monospace": "decode_monospace",
    # Family 15 — Byte-Level Encoding
    "binary_output": "decode_binary_output",
    "octal_output": "decode_octal_output",
    "ascii_decimal": "decode_ascii_decimal",
    "url_encode": "decode_url_encode",
    "html_entities": "decode_html_entities",
    "unicode_escape": "decode_unicode_escape",
    # Family 16 — Visual Layout
    "vertical": "decode_vertical",
    "diagonal": "decode_diagonal",
    "rtl_override": "decode_rtl_override",
    "boustrophedon": "decode_boustrophedon",
    "column_cipher": "decode_column_cipher",
    # Family 17 — Language Games
    "pig_latin_output": "decode_pig_latin_output",
    "backwards_words": "decode_backwards_words",
    "backwards_sentences": "decode_backwards_sentences",
    "ipa": None,  # Pass-through — IPA is human-readable
    # Family 18 — Data Serialization
    "csv_format": "decode_csv",
    "xml_format": "decode_xml",
    "toml_format": "decode_toml",
    "ini_format": "decode_ini",
    "jsonlines": "decode_jsonlines",
    # Family 19 — Numeric Systems
    "roman_positions": "decode_roman_positions",
    "base32": "decode_base32",
    "phone_keypad": "decode_phone_keypad",
    "number_words": "decode_number_words",
    # Family 20 — Artistic / Signal
    "ascii_art": None,  # Pass-through — human-readable
    "semaphore": "decode_semaphore",
    "letter_names": "decode_letter_names",
    # Family 21 — Chunking & Signal
    "numbered_chunks": "decode_numbered_chunks",
    "alternating_case": "decode_alternating_case",
    "paragraph_reverse": "decode_paragraph_reverse",
    "interleaved_decoy": "decode_interleaved_decoy",
    "whitespace_binary": "decode_whitespace_binary",
    # Pass-through — no decoding needed (output is already readable)
    "cognitive_reframe": None,  # No decoding needed — output is readable
    "code_format": None,  # No decoding needed — extract from code
    "opposite": None,  # Semantic reversal, can't auto-decode
    "socratic": None,  # Heuristic only
    "emoji": None,  # Best-effort
    "crossword": None,  # Answers inline
    "error_extract": None,  # Heuristic extraction
    "pigpen": None,  # Description-based
    "spiral": None,  # Complex spatial decoding
    "word_position_key": None,  # Key provided in output
    # Family 22 — Scenario Framing (all pass-through)
    "scenario_frame": None,  # Output is plain text in a fictional scenario
}


def auto_decode(llm_output: str, metadata: dict[str, Any]) -> str:
    """Dispatch to the correct decoder based on MutationResult.metadata.

    Expects ``metadata["decoder"]`` to name the decoder.  Additional keys
    in *metadata* are passed as keyword arguments to the decoder method.

    Returns the decoded string, or the original *llm_output* unchanged if
    no valid decoder is found or if the decoder is a pass-through (None).
    """
    decoder_name = metadata.get("decoder")
    if not decoder_name or decoder_name not in _DECODER_DISPATCH:
        return llm_output

    method_name = _DECODER_DISPATCH[decoder_name]

    # Pass-through decoders: return original text unchanged
    if method_name is None:
        return llm_output

    method = getattr(OutputDecoder, method_name)

    # Build kwargs from metadata, skipping keys that aren't decoder params
    skip_keys = {
        "decoder", "variant", "seed", "decoy_langs",
        "consonant_shift", "vowel_shift", "era", "frame", "style",
        "language", "base", "section_marker", "comment_prefix",
        "pattern", "columns",
    }
    kwargs: dict[str, Any] = {
        k: v for k, v in metadata.items() if k not in skip_keys
    }

    # Special cases where the first positional arg is the llm_output
    if decoder_name == "multicolumn":
        # multicolumn expects (col1, col2) — try to parse from LLM output
        lines = llm_output.strip().splitlines()
        col1, col2 = "", ""
        for line in lines:
            line = line.strip()
            if line.upper().startswith("COLUMN_A:") or line.upper().startswith("PART_1"):
                col1 = line.split(":", 1)[-1].strip()
            elif line.upper().startswith("COLUMN_B:") or line.upper().startswith("PART_2"):
                col2 = line.split(":", 1)[-1].strip()
        return OutputDecoder.decode_multicolumn(col1, col2)

    if decoder_name == "substitution_cipher":
        # Use the inverse_map for decoding
        inverse = metadata.get("inverse_map", metadata.get("cipher_map", {}))
        return OutputDecoder.decode_substitution_cipher(llm_output, inverse)

    # Decoders that need specific metadata keys re-added as kwargs
    if decoder_name == "enigma_simple":
        kw: dict[str, Any] = {}
        if "consonant_shift" in metadata:
            kw["consonant_shift"] = metadata["consonant_shift"]
        if "vowel_shift" in metadata:
            kw["vowel_shift"] = metadata["vowel_shift"]
        try:
            return method(llm_output, **kw)
        except TypeError:
            return method(llm_output)

    if decoder_name == "comments" and "comment_prefix" in metadata:
        return method(llm_output, comment_prefix=metadata["comment_prefix"])

    if decoder_name == "column_cipher" and "columns" in metadata:
        return method(llm_output, columns=metadata["columns"])

    # General dispatch: pass text + relevant kwargs
    try:
        return method(llm_output, **kwargs)
    except TypeError:
        # Fallback: just pass the text
        return method(llm_output)
