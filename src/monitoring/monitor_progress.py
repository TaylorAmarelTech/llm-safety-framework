""""""
NOTICE: This is a sanitized version for public release.
Actual test content and exploitation techniques have been removed.
This framework provides the infrastructure for safety testing.
Users must provide their own domain-specific test content.
"""



import sys
import time
import argparse
import json
from pathlib import Path
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from autonomous_research_coordinator import AutonomousResearchCoordinator, ResearchPhase


def parse_args():
    parser = argparse.ArgumentParser(
        description="Monitor autonomous research progress"
    )
    parser.add_argument(
        "--watch",
        action="store_true",
        help="Continuously watch progress (update every 60s)"
    )
    parser.add_argument(
        "--checkpoint",
        type=str,
        help="Path to checkpoint file (default: most recent)"
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=60,
        help="Watch interval in seconds (default: 60)"
    )
    parser.add_argument(
        "--detailed",
        action="store_true",
        help="Show detailed task information"
    )
    return parser.parse_args()


def find_latest_checkpoint(project_root):
    """Find the most recent checkpoint file"""
    checkpoint_dir = project_root / 'data' / 'checkpoints'
    if not checkpoint_dir.exists():
        return None

    checkpoints = list(checkpoint_dir.glob('research_checkpoint_*.json'))
    if not checkpoints:
        default_checkpoint = checkpoint_dir / 'research_checkpoint.json'
        return default_checkpoint if default_checkpoint.exists() else None

    return max(checkpoints, key=lambda p: p.stat().st_mtime)


def display_progress(checkpoint_path, detailed=False):
    """Display current research progress"""
    if not checkpoint_path or not checkpoint_path.exists():
        print("No checkpoint found. Research may not have started yet.")
        return

    try:
        with open(checkpoint_path) as f:
            checkpoint = json.load(f)
    except Exception as e:
        print(f"ERROR: Could not read checkpoint: {e}")
        return

    # Extract stats
    tasks = checkpoint.get('tasks', [])
    total = len(tasks)
    completed = sum(1 for t in tasks if t.get('status') == 'completed')
    failed = sum(1 for t in tasks if t.get('status') == 'failed')
    in_progress = sum(1 for t in tasks if t.get('status') == 'in_progress')
    pending = total - completed - failed - in_progress

    # Calculate progress percentage
    progress_pct = (completed / total * 100) if total > 0 else 0

    # Display header
    print("\n" + "="*80)
    print("AUTONOMOUS RESEARCH PROGRESS")
    print("="*80)
    print(f"Checkpoint: {checkpoint_path.name}")
    print(f"Last Updated: {checkpoint.get('timestamp', 'Unknown')}")

    # Progress bar
    bar_width = 50
    filled = int(bar_width * progress_pct / 100)
    bar = '█' * filled + '░' * (bar_width - filled)
    print(f"\nProgress: [{bar}] {progress_pct:.1f}%")

    # Task counts
    print(f"\nTask Status:")
    print(f"  Total Tasks:     {total:4d}")
    print(f"  Completed:       {completed:4d} ({completed/total*100:5.1f}%)")
    print(f"  In Progress:     {in_progress:4d}")
    print(f"  Failed:          {failed:4d}")
    print(f"  Pending:         {pending:4d}")

    # Current task
    current_task = checkpoint.get('current_task')
    if current_task:
        print(f"\nCurrent Task:")
        print(f"  ID: {current_task.get('task_id')}")
        print(f"  Name: {current_task.get('name')}")
        print(f"  Phase: {current_task.get('phase')}")
        print(f"  Priority: {current_task.get('priority')}")

    # Phase breakdown
    phase_stats = {}
    for task in tasks:
        phase = task.get('phase', 'unknown')
        status = task.get('status', 'unknown')
        if phase not in phase_stats:
            phase_stats[phase] = {'total': 0, 'completed': 0, 'failed': 0}
        phase_stats[phase]['total'] += 1
        if status == 'completed':
            phase_stats[phase]['completed'] += 1
        elif status == 'failed':
            phase_stats[phase]['failed'] += 1

    print(f"\nProgress by Phase:")
    for phase in [
        'SETUP', 'TEST_GENERATION', 'FEATURE_SPACE_ANALYSIS',
        'BOUNDARY_PROBING', 'ADVANCED_GENERATION', 'MULTI_LANGUAGE',
        'COMPREHENSIVE_TESTING', 'VISUALIZATION', 'DOCUMENTATION'
    ]:
        if phase in phase_stats:
            stats = phase_stats[phase]
            pct = stats['completed'] / stats['total'] * 100 if stats['total'] > 0 else 0
            status_str = f"{stats['completed']}/{stats['total']}"
            print(f"  {phase:30s}: {status_str:10s} ({pct:5.1f}%)")

    # Recent failures
    if failed > 0:
        failed_tasks = [t for t in tasks if t.get('status') == 'failed']
        print(f"\nRecent Failures:")
        for task in failed_tasks[-5:]:  # Show last 5 failures
            print(f"  - {task.get('name')} (retries: {task.get('retry_count', 0)})")

    # Detailed view
    if detailed:
        print(f"\nAll Tasks:")
        for i, task in enumerate(tasks, 1):
            status_symbol = {
                'completed': '✓',
                'failed': '✗',
                'in_progress': '⋯',
                'pending': '○'
            }.get(task.get('status'), '?')
            print(f"  {i:3d}. [{status_symbol}] {task.get('name')[:60]}")

    # Estimates
    if pending > 0 and completed > 0:
        start_time = checkpoint.get('start_time')
        if start_time:
            try:
                start_dt = datetime.fromisoformat(start_time)
                elapsed = (datetime.now() - start_dt).total_seconds() / 3600  # hours
                avg_hours_per_task = elapsed / completed
                remaining_hours = avg_hours_per_task * pending
                completion_time = datetime.now() + timedelta(hours=remaining_hours)

                print(f"\nEstimates:")
                print(f"  Elapsed Time: {elapsed:.1f} hours")
                print(f"  Avg per Task: {avg_hours_per_task*60:.1f} minutes")
                print(f"  Est. Remaining: {remaining_hours:.1f} hours")
                print(f"  Est. Completion: {completion_time.strftime('%Y-%m-%d %H:%M')}")
            except:
                pass

    print("="*80 + "\n")


def main():
    args = parse_args()

    # Find project root
    project_root = Path(__file__).parent.parent.parent

    # Find checkpoint
    if args.checkpoint:
        checkpoint_path = Path(args.checkpoint)
    else:
        checkpoint_path = find_latest_checkpoint(project_root)

    if args.watch:
        print(f"Watching progress (updating every {args.interval}s)...")
        print("Press Ctrl+C to stop\n")
        try:
            while True:
                display_progress(checkpoint_path, detailed=args.detailed)
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print("\nMonitoring stopped")
    else:
        display_progress(checkpoint_path, detailed=args.detailed)


if __name__ == "__main__":
    from datetime import timedelta
    main()
