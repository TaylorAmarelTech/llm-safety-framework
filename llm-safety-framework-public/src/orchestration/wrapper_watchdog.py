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
import psutil
from pathlib import Path
from datetime import datetime, timedelta

# Force UTF-8
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - WATCHDOG - %(message)s',
    handlers=[
        logging.FileHandler('watchdog.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


class Watchdog:
    """System watchdog that monitors and restarts supervisor"""

    def __init__(self, duration_days=14):
        self.duration_days = duration_days
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(days=duration_days)
        self.supervisor_restarts = 0

    def should_continue(self):
        """Check if we should continue running"""
        return datetime.now() < self.end_time

    def check_system_resources(self):
        """Monitor system resources"""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('.')

            logger.info(f"System Resources:")
            logger.info(f"  CPU: {cpu_percent}%")
            logger.info(f"  Memory: {memory.percent}% used ({memory.available / (1024**3):.1f} GB free)")
            logger.info(f"  Disk: {disk.percent}% used ({disk.free / (1024**3):.1f} GB free)")

            # Check for critical conditions
            if memory.percent > 95:
                logger.warning("⚠ Memory usage critical!")
            if disk.percent > 95:
                logger.warning("⚠ Disk usage critical!")

        except Exception as e:
            logger.warning(f"Could not check system resources: {e}")

    def run_supervisor(self):
        """Run the supervisor wrapper"""
        logger.info("="*80)
        logger.info(f"WATCHDOG STARTED - 14-DAY AUTONOMOUS RESEARCH")
        logger.info(f"Start: {self.start_time}")
        logger.info(f"End: {self.end_time}")
        logger.info("="*80)

        while self.should_continue():
            try:
                self.supervisor_restarts += 1
                elapsed_hours = (datetime.now() - self.start_time).total_seconds() / 3600
                remaining_hours = (self.end_time - datetime.now()).total_seconds() / 3600

                logger.info(f"\n{'='*80}")
                logger.info(f"Starting Supervisor (restart #{self.supervisor_restarts})")
                logger.info(f"Elapsed: {elapsed_hours:.1f}h / Remaining: {remaining_hours:.1f}h")
                logger.info(f"{'='*80}\n")

                # Check system resources
                self.check_system_resources()

                # Run supervisor
                process = subprocess.Popen(
                    [sys.executable, 'wrapper_supervisor.py'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    encoding='utf-8',
                    errors='replace'
                )

                # Monitor supervisor
                last_health_check = datetime.now()

                while process.poll() is None:
                    # Read output
                    line = process.stdout.readline()
                    if line:
                        print(line, end='')
                        sys.stdout.flush()

                    # Periodic health check
                    if (datetime.now() - last_health_check).total_seconds() > 3600:
                        self.check_system_resources()
                        last_health_check = datetime.now()

                    # Check if we should stop
                    if not self.should_continue():
                        logger.info("Duration complete, stopping supervisor...")
                        process.terminate()
                        break

                # Get remaining output
                for line in process.stdout:
                    print(line, end='')

                return_code = process.wait()

                if return_code == 0:
                    logger.info("Supervisor completed successfully")
                    if self.should_continue():
                        logger.info("But duration not complete, restarting...")
                    else:
                        logger.info("Research duration complete!")
                        break
                else:
                    logger.warning(f"Supervisor exited with code {return_code}")

            except KeyboardInterrupt:
                logger.info("\nWatchdog stopped by user")
                if process:
                    process.terminate()
                break

            except Exception as e:
                logger.error(f"Error in watchdog: {e}")

            # Wait before restart
            if self.should_continue():
                delay = 30
                logger.info(f"Restarting supervisor in {delay} seconds...")
                time.sleep(delay)

        # Final summary
        logger.info(f"\n{'='*80}")
        logger.info("WATCHDOG FINISHED")
        logger.info(f"Total time: {(datetime.now() - self.start_time).total_seconds() / 3600:.1f} hours")
        logger.info(f"Supervisor restarts: {self.supervisor_restarts}")
        logger.info(f"{'='*80}\n")


if __name__ == "__main__":
    watchdog = Watchdog(duration_days=14)
    watchdog.run_supervisor()
