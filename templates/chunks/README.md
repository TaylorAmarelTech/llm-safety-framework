# Template Chunks

Large template files have been split into smaller chunks for GitHub compatibility.

## Files Included

| Original File | Chunks | Total Size |
|--------------|--------|------------|
| `all_conversations.json` | 3 parts | ~57 MB |
| `all_tests_consolidated_20260129_211032.json` | 3 parts | ~57 MB |
| `template_massive_complete_20260129_082517.json` | 12 parts | ~474 MB |
| `template_massive_complete_20260129_083101.json` | 22 parts | ~944 MB |

## Reassembly

Run the reassembly script to combine chunks back into original files:

```bash
python scripts/reassemble_templates.py
```

Or manually in Python:

```python
import json
import glob

def reassemble(pattern, output_file):
    """Reassemble chunked JSON files."""
    chunks = sorted(glob.glob(pattern))
    combined = []

    for chunk_file in chunks:
        with open(chunk_file, 'r') as f:
            data = json.load(f)
            if isinstance(data, list):
                combined.extend(data)
            elif isinstance(data, dict):
                combined.append(data)

    with open(output_file, 'w') as f:
        json.dump(combined, f, indent=2)

    print(f"Created {output_file} with {len(combined)} items")

# Example usage
reassemble(
    "templates/chunks/all_conversations_part*.json",
    "templates/all_conversations.json"
)
```

## Test Data Statistics

- **Total test cases**: 1,500,000+ prompts
- **Categories**: 6 attack generators
- **Corridors**: 26 migration routes
- **ILO Indicators**: All 11 covered
