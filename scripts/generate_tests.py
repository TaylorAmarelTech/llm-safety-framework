#!/usr/bin/env python3
"""
Test Generation Script

Generates test cases using all available generators and saves to JSON/database.

Usage:
    python scripts/generate_tests.py
    python scripts/generate_tests.py --generator historical_precedent --count 100
    python scripts/generate_tests.py --all --count 50
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.generators import (
    GENERATOR_REGISTRY,
    list_generators,
    generate_all,
)


def main():
    parser = argparse.ArgumentParser(description='Generate test cases')
    parser.add_argument(
        '--generator', '-g',
        type=str,
        choices=list(GENERATOR_REGISTRY.keys()),
        help='Specific generator to use'
    )
    parser.add_argument(
        '--all', '-a',
        action='store_true',
        help='Use all generators'
    )
    parser.add_argument(
        '--count', '-c',
        type=int,
        default=10,
        help='Number of tests to generate (per generator if --all)'
    )
    parser.add_argument(
        '--output', '-o',
        type=Path,
        default=None,
        help='Output file path (default: data/generated_tests_TIMESTAMP.json)'
    )
    parser.add_argument(
        '--format', '-f',
        choices=['json', 'jsonl'],
        default='json',
        help='Output format'
    )

    args = parser.parse_args()

    print("=" * 70)
    print("  LLM Safety Framework - Test Generator")
    print("=" * 70)
    print()

    tests = []

    if args.all:
        print(f"[*] Generating {args.count} tests per generator...")
        print(f"[*] Generators: {', '.join(list_generators())}")
        print()

        for name in GENERATOR_REGISTRY.keys():
            print(f"  - {name}...")
            generator = GENERATOR_REGISTRY[name]()
            batch = generator.generate_batch(args.count)
            tests.extend(batch)
            print(f"    Generated {len(batch)} tests")

    elif args.generator:
        print(f"[*] Using generator: {args.generator}")
        print(f"[*] Generating {args.count} tests...")
        print()

        generator = GENERATOR_REGISTRY[args.generator]()
        tests = generator.generate_batch(args.count)
        print(f"  Generated {len(tests)} tests")

    else:
        print("[!] Please specify --generator or --all")
        print()
        print("Available generators:")
        for name in list_generators():
            print(f"  - {name}")
        return

    # Determine output path
    if args.output:
        output_path = args.output
    else:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_dir = Path(__file__).parent.parent / 'data' / 'generated'
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f'generated_tests_{timestamp}.json'

    # Convert dataclass objects to dicts for JSON serialization
    def to_serializable(obj):
        if hasattr(obj, '__dataclass_fields__'):
            return {k: to_serializable(v) for k, v in obj.__dict__.items()}
        elif isinstance(obj, list):
            return [to_serializable(item) for item in obj]
        elif isinstance(obj, dict):
            return {k: to_serializable(v) for k, v in obj.items()}
        else:
            return obj

    serializable_tests = [to_serializable(t) for t in tests]

    # Save tests
    print()
    print(f"[*] Saving to: {output_path}")

    output_data = {
        'metadata': {
            'generated_at': datetime.now().isoformat(),
            'total_tests': len(tests),
            'generators_used': [args.generator] if args.generator else list_generators(),
        },
        'tests': serializable_tests
    }

    if args.format == 'jsonl':
        with open(output_path, 'w', encoding='utf-8') as f:
            for test in tests:
                f.write(json.dumps(test, ensure_ascii=False) + '\n')
    else:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

    print()
    print("=" * 70)
    print("  Generation Complete")
    print("=" * 70)
    print(f"  Total tests: {len(tests):,}")
    print(f"  Output: {output_path}")
    print()

    # Show sample
    if serializable_tests:
        print("Sample test:")
        sample = serializable_tests[0]
        print(f"  ID: {sample.get('id', 'N/A')}")
        print(f"  Category: {sample.get('category', 'N/A')}")
        prompt = sample.get('prompt', '')
        print(f"  Prompt preview: {prompt[:100]}...")


if __name__ == '__main__':
    main()
