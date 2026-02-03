""""""
NOTICE: This is a sanitized version for public release.
Actual test content and exploitation techniques have been removed.
This framework provides the infrastructure for safety testing.
Users must provide their own domain-specific test content.
"""



import json
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, List
import subprocess
import sys


def get_file_count(directory: str, pattern: str = "*.json") -> int:
    """Count files matching pattern in directory"""
    path = Path(directory)
    if not path.exists():
        return 0
    return len(list(path.glob(pattern)))


def get_file_size_mb(file_path: str) -> float:
    """Get file size in MB"""
    path = Path(file_path)
    if not path.exists():
        return 0
    return path.stat().st_size / (1024 * 1024)


def get_latest_consolidation_stats() -> Dict:
    """Get stats from latest consolidation"""
    summary_file = Path("consolidation_summary.json")
    if not summary_file.exists():
        return {}

    with open(summary_file, 'r') as f:
        return json.load(f)


def monitor_testing_progress():
    """Monitor continuous testing progress"""

    print(f"\n{'='*80}")
    print(f"CONTINUOUS TESTING MONITOR - Started {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*80}\n")

    iteration = 0

    while True:
        iteration += 1

        print(f"\n{'='*80}")
        print(f"STATUS UPDATE #{iteration} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*80}\n")

        # Check generation progress
        print("📊 GENERATION PROGRESS:")
        scaled_test_count = get_file_count("data/scaled_tests")
        print(f"  Total test files: {scaled_test_count:,}")

        # Check testing progress
        print("\n🔥 TESTING PROGRESS:")
        testing_count = get_file_count("data/massive_testing")
        continuous_count = get_file_count("data/continuous_testing")
        scaled_results_count = get_file_count("reports/scaled")

        print(f"  Massive testing results: {testing_count:,} files")
        print(f"  Continuous testing results: {continuous_count:,} files")
        print(f"  Scaled results: {scaled_results_count:,} files")

        # Check consolidation stats
        print("\n📈 LATEST CONSOLIDATION:")
        stats = get_latest_consolidation_stats()
        if stats:
            print(f"  Total conversations: {stats.get('total_conversations', 0):,}")
            print(f"  With responses: {stats.get('conversations_with_full_responses', 0):,}")
            print(f"  Untested: {stats.get('conversations_prompts_only', 0):,}")
            print(f"  Harmful bypasses: {stats.get('harmful_bypassed', 0):,}")
            print(f"  Harm rate: {stats.get('harm_rate', 0):.2f}%")
            print(f"  Last updated: {stats.get('consolidation_timestamp', 'Unknown')}")
        else:
            print("  No consolidation data available")

        # Check disk usage
        print("\n💾 DISK USAGE:")
        all_convs_size = get_file_size_mb("all_conversations.json")
        print(f"  all_conversations.json: {all_convs_size:.1f} MB")

        # Recommendations
        print("\n💡 RECOMMENDATIONS:")
        if stats and stats.get('conversations_prompts_only', 0) > 1000:
            print(f"  ⚠️  {stats['conversations_prompts_only']:,} untested prompts - keep testing!")

        if iteration % 10 == 0:
            print("  🔄 Running consolidation (every 10 iterations)...")
            try:
                subprocess.run(["python", "consolidate_all_data.py"],
                             capture_output=True, timeout=300)
                print("  ✅ Consolidation complete")
            except Exception as e:
                print(f"  ❌ Consolidation failed: {e}")

        if iteration % 50 == 0:
            print("  🏆 Extracting top examples (every 50 iterations)...")
            try:
                subprocess.run(["python", "extract_top_examples.py", "--top", "500"],
                             capture_output=True, timeout=300)
                print("  ✅ Top examples extracted")
            except Exception as e:
                print(f"  ❌ Extraction failed: {e}")

        print(f"\n{'='*80}")
        print(f"Next update in 5 minutes...")
        print(f"{'='*80}\n")

        # Sleep for 5 minutes
        time.sleep(300)


if __name__ == '__main__':
    try:
        monitor_testing_progress()
    except KeyboardInterrupt:
        print("\n\n🛑 Monitor stopped by user")
        sys.exit(0)
