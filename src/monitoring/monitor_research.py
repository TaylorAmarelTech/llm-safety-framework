""""""
NOTICE: This is a sanitized version for public release.
Actual test content and exploitation techniques have been removed.
This framework provides the infrastructure for safety testing.
Users must provide their own domain-specific test content.
"""



import sys
import json
import sqlite3
from pathlib import Path
from datetime import datetime
import time

# Force UTF-8
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def clear_screen():
    """Clear terminal screen"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def load_state():
    """Load current state"""
    state_file = Path('data/continuous_state.json')
    if state_file.exists():
        with open(state_file) as f:
            return json.load(f)
    return {}


def count_tests():
    """Count tests in database"""
    try:
        conn = sqlite3.connect('trafficking_tests.db')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM tests")
        count = cursor.fetchone()[0]
        conn.close()
        return count
    except:
        return 0


def get_log_tail(log_file, lines=20):
    """Get last N lines from log file"""
    try:
        with open(log_file, 'r', encoding='utf-8', errors='replace') as f:
            return f.readlines()[-lines:]
    except:
        return []


def display_status(watch_mode=False):
    """Display current status"""

    if watch_mode:
        clear_screen()

    state = load_state()
    test_count = count_tests()

    print("="*80)
    print("14-DAY AUTONOMOUS RESEARCH - LIVE STATUS")
    print("="*80)
    print()

    # Timeinfo
    if 'last_update' in state:
        last_update = state['last_update']
        elapsed_hours = state.get('elapsed_hours', 0)
        remaining_hours = state.get('remaining_hours', 0)

        print(f"Last Update: {last_update}")
        print(f"Elapsed: {elapsed_hours:.1f} hours ({elapsed_hours/24:.1f} days)")
        print(f"Remaining: {remaining_hours:.1f} hours ({remaining_hours/24:.1f} days)")
        print(f"Progress: {(elapsed_hours / 336 * 100):.1f}%")
    else:
        print("Status: Starting up...")

    print()

    # Progress bars
    if 'elapsed_hours' in state:
        progress_pct = min(100, state['elapsed_hours'] / 336 * 100)
        bar_width = 50
        filled = int(bar_width * progress_pct / 100)
        bar = '█' * filled + '░' * (bar_width - filled)
        print(f"Time:  [{bar}] {progress_pct:.1f}%")

    print()

    # Counters
    print(f"Tests in Database: {test_count:,}")
    print(f"Tests Generated: {state.get('tests_generated', 0)}")
    print(f"Analyses Completed: {state.get('analyses_completed', 0)}")
    print(f"Visualizations Created: {state.get('visualizations_created', 0)}")
    print(f"Errors Encountered: {state.get('errors_encountered', 0)}")
    print(f"System Restarts: {state.get('restarts', 0)}")

    print()

    # Recent activity
    print("="*80)
    print("RECENT ACTIVITY (last 20 lines)")
    print("="*80)

    for line in get_log_tail('continuous_research_14day.log'):
        print(line.rstrip())

    print()
    print("="*80)

    if watch_mode:
        print("Press Ctrl+C to stop monitoring")
        print("Refreshing every 30 seconds...")
    else:
        print(f"Run with --watch to monitor continuously")

    print("="*80)


def main():
    """Main entry point"""
    watch_mode = '--watch' in sys.argv

    if watch_mode:
        try:
            while True:
                display_status(watch_mode=True)
                time.sleep(30)  # Refresh every 30 seconds
        except KeyboardInterrupt:
            print("\n\nMonitoring stopped")
    else:
        display_status(watch_mode=False)


if __name__ == "__main__":
    main()
