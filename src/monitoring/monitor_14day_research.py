""""""
NOTICE: This is a sanitized version for public release.
Actual test content and exploitation techniques have been removed.
This framework provides the infrastructure for safety testing.
Users must provide their own domain-specific test content.
"""



import json
import time
import os
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional, Dict


class ResearchMonitor:
    """Monitor for 14-day autonomous research"""

    def __init__(self, workspace_dir: str = "."):
        self.workspace = Path(workspace_dir)
        self.checkpoints_dir = self.workspace / "data" / "checkpoints"
        self.log_file = self.workspace / "14day_research.log"

    def get_latest_checkpoint(self) -> Optional[Dict]:
        """Get the most recent checkpoint"""
        if not self.checkpoints_dir.exists():
            return None

        checkpoints = sorted(self.checkpoints_dir.glob("checkpoint_*.json"))
        if not checkpoints:
            return None

        latest = checkpoints[-1]
        with open(latest, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_log_tail(self, lines: int = 20) -> list:
        """Get last N lines of log file"""
        if not self.log_file.exists():
            return []

        with open(self.log_file, 'r', encoding='utf-8', errors='ignore') as f:
            return f.readlines()[-lines:]

    def display_status(self):
        """Display current research status"""
        checkpoint = self.get_latest_checkpoint()

        if not checkpoint:
            print("❌ No checkpoint found. Research may not have started yet.")
            return

        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')

        print("="*80)
        print("  14-DAY AUTONOMOUS RESEARCH - LIVE MONITOR")
        print("="*80)

        # Timing information
        timestamp = datetime.fromisoformat(checkpoint['timestamp'])
        current_day = checkpoint.get('current_day', 0)
        elapsed_days = current_day
        remaining_days = 14 - current_day

        print(f"\n⏱️  TIMING:")
        print(f"   Last Update: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"   Current Day: {current_day}/14")
        print(f"   Days Elapsed: {elapsed_days}")
        print(f"   Days Remaining: {remaining_days}")

        # Statistics
        stats = checkpoint.get('statistics', {})
        tests_generated = stats.get('tests_generated', 0)
        tests_target = stats.get('tests_target', 2500)
        probes_generated = stats.get('probes_generated', 0)
        probes_target = stats.get('probes_target', 2000)
        visualizations = stats.get('visualizations_created', 0)
        viz_target = stats.get('visualizations_target', 20)
        analyses = stats.get('analyses_completed', 0)

        print(f"\n📊 DELIVERABLES:")
        print(f"   Tests Generated:     {tests_generated:,}/{tests_target:,} ({tests_generated/tests_target*100:.1f}%)")
        self._print_progress_bar(tests_generated, tests_target)

        print(f"\n   Boundary Probes:     {probes_generated:,}/{probes_target:,} ({probes_generated/probes_target*100:.1f}%)")
        self._print_progress_bar(probes_generated, probes_target)

        print(f"\n   Visualizations:      {visualizations}/{viz_target} ({visualizations/viz_target*100:.1f}%)")
        self._print_progress_bar(visualizations, viz_target)

        print(f"\n   Analyses Completed:  {analyses}")

        # Task progress
        tasks = checkpoint.get('tasks', [])
        completed = len([t for t in tasks if t['status'] == 'completed'])
        failed = len([t for t in tasks if t['status'] == 'failed'])
        in_progress = len([t for t in tasks if t['status'] == 'in_progress'])
        pending = len([t for t in tasks if t['status'] == 'pending'])
        total = len(tasks)

        print(f"\n📋 TASKS:")
        print(f"   Total:        {total}")
        print(f"   Completed:    {completed} ({completed/total*100:.1f}%)")
        print(f"   In Progress:  {in_progress}")
        print(f"   Pending:      {pending}")
        print(f"   Failed:       {failed}")

        if total > 0:
            print(f"\n   Overall Progress: ", end="")
            self._print_progress_bar(completed, total)

        # Current phase
        if in_progress > 0:
            current_tasks = [t for t in tasks if t['status'] == 'in_progress']
            if current_tasks:
                task = current_tasks[0]
                print(f"\n🏃 CURRENT TASK:")
                print(f"   {task['name']}")
                print(f"   Phase: {task['phase']}")
                if task.get('started_at'):
                    started = datetime.fromisoformat(task['started_at'])
                    duration = datetime.now() - started
                    print(f"   Running for: {duration.total_seconds()/3600:.1f} hours")

        # Failures
        if failed > 0:
            failed_tasks = [t for t in tasks if t['status'] == 'failed'][:5]
            print(f"\n⚠️  FAILED TASKS ({failed}):")
            for task in failed_tasks:
                print(f"   • {task['name']}")
                if task.get('error_message'):
                    print(f"     Error: {task['error_message'][:60]}")

        # Recent log entries
        print(f"\n📝 RECENT LOG:")
        log_lines = self.get_log_tail(10)
        for line in log_lines:
            print(f"   {line.rstrip()}")

        print("\n" + "="*80)
        print("Press Ctrl+C to exit monitor")
        print("="*80)

    def _print_progress_bar(self, current: int, total: int, width: int = 40):
        """Print a text-based progress bar"""
        if total == 0:
            percent = 0
        else:
            percent = current / total

        filled = int(width * percent)
        bar = '█' * filled + '░' * (width - filled)
        print(f"   [{bar}] {percent*100:.1f}%")

    def watch(self, interval_seconds: int = 30):
        """Watch research progress in real-time"""
        print("Starting monitor... (Press Ctrl+C to exit)\n")

        try:
            while True:
                self.display_status()
                time.sleep(interval_seconds)

        except KeyboardInterrupt:
            print("\n\n✅ Monitor stopped.")


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description="Monitor 14-day autonomous research")
    parser.add_argument('--interval', type=int, default=30,
                       help='Update interval in seconds (default: 30)')
    parser.add_argument('--once', action='store_true',
                       help='Show status once and exit')

    args = parser.parse_args()

    monitor = ResearchMonitor()

    if args.once:
        monitor.display_status()
    else:
        monitor.watch(args.interval)


if __name__ == '__main__':
    main()
