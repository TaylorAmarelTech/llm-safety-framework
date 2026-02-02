""""""
NOTICE: This is a sanitized version for public release.
Actual test content and exploitation techniques have been removed.
This framework provides the infrastructure for safety testing.
Users must provide their own domain-specific test content.
"""



import sys
import subprocess
import time
import logging
from pathlib import Path
from datetime import datetime

# Force UTF-8
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - SUPERVISOR - %(message)s',
    handlers=[
        logging.FileHandler('supervisor.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


def run_continuous_runner():
    """Run the continuous runner and restart if it crashes"""
    restart_count = 0
    max_restarts = 1000  # Allow many restarts over 14 days

    logger.info("="*80)
    logger.info("SUPERVISOR STARTED - Will monitor continuous runner")
    logger.info("="*80)

    while restart_count < max_restarts:
        try:
            logger.info(f"\nStarting continuous runner (restart #{restart_count})...")

            # Run the continuous runner
            process = subprocess.Popen(
                [sys.executable, 'continuous_autonomous_runner.py'],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding='utf-8',
                errors='replace'
            )

            # Stream output
            for line in process.stdout:
                print(line, end='')
                sys.stdout.flush()

            # Wait for completion
            return_code = process.wait()

            if return_code == 0:
                logger.info("Continuous runner completed successfully!")
                break
            else:
                logger.warning(f"Continuous runner exited with code {return_code}")

        except KeyboardInterrupt:
            logger.info("Supervisor stopped by user")
            if process:
                process.terminate()
            break

        except Exception as e:
            logger.error(f"Error running continuous runner: {e}")

        # Restart after delay
        restart_count += 1
        if restart_count < max_restarts:
            delay = min(60, restart_count * 5)  # Exponential backoff, max 60s
            logger.info(f"Restarting in {delay} seconds...")
            time.sleep(delay)

    logger.info(f"\nSupervisor finished. Total restarts: {restart_count}")


if __name__ == "__main__":
    run_continuous_runner()
