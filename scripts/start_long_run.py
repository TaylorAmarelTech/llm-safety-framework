""""""
NOTICE: This is a sanitized version for public release.
Actual test content and exploitation techniques have been removed.
This framework provides the infrastructure for safety testing.
Users must provide their own domain-specific test content.
"""



import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent

print("=" * 80)
print("STARTING 10-HOUR AUTONOMOUS LEARNING RUN")
print("=" * 80)
print()
print("IMPORTANT: Keep this terminal window open!")
print("The run will stop if you close this window.")
print()
print("To monitor progress, open a NEW terminal and run:")
print("  cd trafficking_llm_benchmark")
print("  python monitor_autonomous.py --continuous 60")
print()
print("=" * 80)
print()
print("Starting...")
print()

# Start the autonomous run
cmd = [
    sys.executable,
    "scripts/run_autonomous_robust.py",
    "--iterations", "500",
    "--tests-per-iteration", "20",
    "--checkpoint-interval", "10"
]

try:
    # Run with output to console
    subprocess.run(cmd, cwd=PROJECT_ROOT)
except KeyboardInterrupt:
    print("\n\nInterrupted by user. Checkpoint should be saved.")
except Exception as e:
    print(f"\n\nError: {e}")

print("\n" + "=" * 80)
print("RUN COMPLETE OR STOPPED")
print("=" * 80)
print("\nCheck results in: data/autonomous_learning_10hr/")
