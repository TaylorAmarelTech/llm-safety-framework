#!/usr/bin/env python3
"""
Reassemble Template Files

Combines chunked JSON files back into their original large files.
Run this after cloning the repository to reconstruct the full test datasets.

Usage:
    python scripts/reassemble_templates.py
"""

import json
import glob
import os
from pathlib import Path


def reassemble_json_chunks(pattern: str, output_file: str) -> int:
    """
    Reassemble chunked JSON files into a single file.

    Args:
        pattern: Glob pattern to match chunk files (e.g., "chunks/file_part*.json")
        output_file: Path to the output file

    Returns:
        Number of items in the reassembled file
    """
    chunks = sorted(glob.glob(pattern))

    if not chunks:
        print(f"No chunks found matching: {pattern}")
        return 0

    print(f"Found {len(chunks)} chunks for {os.path.basename(output_file)}")

    combined = []
    for i, chunk_file in enumerate(chunks, 1):
        print(f"  Loading chunk {i}/{len(chunks)}: {os.path.basename(chunk_file)}")
        with open(chunk_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, list):
            combined.extend(data)
        elif isinstance(data, dict):
            if combined and isinstance(combined[0], tuple):
                # Dict was split as items
                combined.extend(data.items())
            else:
                combined.append(data)

    # Write combined file
    print(f"  Writing {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(combined, f, indent=2)

    size_mb = os.path.getsize(output_file) / (1024 * 1024)
    print(f"  Created {output_file} ({size_mb:.1f} MB, {len(combined):,} items)")

    return len(combined)


def main():
    """Reassemble all chunked template files."""
    # Change to project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    os.chdir(project_root)

    chunks_dir = "templates/chunks"
    output_dir = "templates"

    if not os.path.exists(chunks_dir):
        print(f"Chunks directory not found: {chunks_dir}")
        return

    # Find unique base names from chunk files
    chunk_files = glob.glob(f"{chunks_dir}/*_part*.json")
    base_names = set()

    for f in chunk_files:
        # Extract base name (everything before _partNNN.json)
        basename = os.path.basename(f)
        parts = basename.rsplit('_part', 1)
        if len(parts) == 2:
            base_names.add(parts[0])

    print(f"Found {len(base_names)} files to reassemble:\n")

    total_items = 0
    for base_name in sorted(base_names):
        pattern = f"{chunks_dir}/{base_name}_part*.json"
        output_file = f"{output_dir}/{base_name}.json"

        items = reassemble_json_chunks(pattern, output_file)
        total_items += items
        print()

    print(f"Reassembly complete!")
    print(f"Total items across all files: {total_items:,}")


if __name__ == "__main__":
    main()
