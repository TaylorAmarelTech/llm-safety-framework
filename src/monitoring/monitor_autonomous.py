""""""
NOTICE: This is a sanitized version for public release.
Actual test content and exploitation techniques have been removed.
This framework provides the infrastructure for safety testing.
Users must provide their own domain-specific test content.
"""



import os
import json
from pathlib import Path
from datetime import datetime
import time

PROJECT_ROOT = Path(__file__).parent
OUTPUT_DIR = PROJECT_ROOT / "data" / "autonomous_learning_10hr"


def find_latest_checkpoint():
    """Find the most recent checkpoint file."""
    if not OUTPUT_DIR.exists():
        return None

    checkpoints = list(OUTPUT_DIR.glob("checkpoint_*.json"))
    if not checkpoints:
        return None

    # Sort by modification time, newest first
    checkpoints.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return checkpoints[0]


def format_duration(seconds):
    """Format seconds into human-readable duration."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours}h {minutes}m {secs}s"


def display_progress():
    """Display current progress."""
    checkpoint = find_latest_checkpoint()

    if not checkpoint:
        print("=" * 70)
        print("NO CHECKPOINT FOUND YET")
        print("=" * 70)
        print("The autonomous learning system may still be starting up.")
        print("Wait a few minutes and try again.")
        return

    # Load checkpoint
    with open(checkpoint, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Calculate elapsed time
    start_time = data.get("start_time")
    if start_time:
        start_dt = datetime.fromisoformat(start_time)
        elapsed = (datetime.now() - start_dt).total_seconds()
    else:
        elapsed = 0

    # Extract metrics
    iteration = data.get("iteration", 0)
    metrics = data.get("metrics", {})
    total_tests = metrics.get("total_tests", 0)
    harmful = metrics.get("harmful_responses", 0)
    refusals = metrics.get("refusals", 0)
    patterns = len(data.get("patterns", {}))

    # Calculate rates
    harm_rate = (harmful / total_tests * 100) if total_tests > 0 else 0
    refusal_rate = (refusals / total_tests * 100) if total_tests > 0 else 0
    tests_per_hour = (total_tests / elapsed * 3600) if elapsed > 0 else 0

    # Display
    print("=" * 70)
    print("AUTONOMOUS LEARNING PROGRESS")
    print("=" * 70)
    print(f"Session: {data.get('session_id', 'unknown')}")
    print(f"Checkpoint: {checkpoint.name}")
    print(f"Last Updated: {datetime.fromtimestamp(checkpoint.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    print("TIME")
    print("-" * 70)
    print(f"Elapsed: {format_duration(elapsed)}")
    print(f"Iteration: {iteration}")
    print()
    print("METRICS")
    print("-" * 70)
    print(f"Total Tests: {total_tests}")
    print(f"Harmful Responses: {harmful} ({harm_rate:.1f}%)")
    print(f"Refusals: {refusals} ({refusal_rate:.1f}%)")
    print(f"Tests/Hour: {tests_per_hour:.1f}")
    print()
    print("LEARNING")
    print("-" * 70)
    print(f"Patterns Discovered: {patterns}")
    print(f"Successful Prompts: {len(data.get('successful_prompts', []))}")
    print(f"Failed Prompts: {len(data.get('failed_prompts', []))}")
    print()

    # Show recent patterns
    recent_patterns = list(data.get("patterns", {}).items())[-5:]
    if recent_patterns:
        print("RECENT PATTERNS DISCOVERED")
        print("-" * 70)
        for pattern_id, pattern_data in recent_patterns:
            effectiveness = pattern_data.get("effectiveness", 0)
            uses = pattern_data.get("times_used", 0)
            print(f"  {pattern_id}: {effectiveness*100:.1f}% effective ({uses} uses)")

    print()
    print("=" * 70)

    # Estimate completion
    target_iterations = 500
    if iteration > 0 and elapsed > 0:
        avg_time_per_iteration = elapsed / iteration
        remaining_iterations = target_iterations - iteration
        est_remaining = remaining_iterations * avg_time_per_iteration
        print(f"Estimated Time Remaining: {format_duration(est_remaining)}")
        print(f"Estimated Completion: {(datetime.now().timestamp() + est_remaining)}")

    print("=" * 70)


def monitor_continuously(interval=60):
    """Monitor progress continuously."""
    print(f"Monitoring autonomous learning run (updates every {interval}s)")
    print("Press Ctrl+C to stop monitoring (does NOT stop the run)\n")

    try:
        while True:
            display_progress()
            print(f"\nNext update in {interval} seconds...")
            time.sleep(interval)
            print("\n" * 2)
    except KeyboardInterrupt:
        print("\n\nMonitoring stopped. The autonomous run continues in background.")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--continuous":
        interval = int(sys.argv[2]) if len(sys.argv) > 2 else 60
        monitor_continuously(interval)
    else:
        display_progress()
        print()
        print("TIP: Run with --continuous to monitor in real-time")
        print("     python monitor_autonomous.py --continuous [interval_seconds]")
