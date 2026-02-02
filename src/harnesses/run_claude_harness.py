""""""
NOTICE: This is a sanitized version for public release.
Actual test content and exploitation techniques have been removed.
This framework provides the infrastructure for safety testing.
Users must provide their own domain-specific test content.
"""



import argparse
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

# Fix Windows encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

PROJECT_ROOT = Path(__file__).parent.parent


def get_iteration_prompt(iteration: int) -> str:
    """Generate the prompt for a specific iteration."""
    return f'''Read AUTONOMOUS_IMPROVEMENT_PROMPT.md and IMPROVEMENT_LOG.md first.

CRITICAL GUARDRAILS - NEVER VIOLATE:
1. NEVER delete any original files - only add new files or modify existing ones
2. NEVER modify any .db, .sqlite, or database files directly
3. NEVER expose, log, or hardcode API keys or secrets
4. NEVER run pip install or modify dependencies without documenting
5. NEVER create actual exploitation content or harmful instructions
6. NEVER delete or overwrite IMPROVEMENT_LOG.md or reports
7. ALWAYS create backups before major refactoring (copy file to .bak)
8. ALWAYS run existing tests before and after changes if pytest is available
9. ALWAYS document every change in IMPROVEMENT_LOG.md with timestamp
10. ALWAYS maintain defensive security research framing

SCOPE LIMITS:
- Only work within the trafficking_llm_benchmark directory
- Only modify Python files (.py), markdown files (.md), and config files (.json, .yaml)
- Stop after 15 file modifications and report progress
- If unsure about a change, document the question instead of making the change

CURRENT TASK - Iteration {iteration}:
1. Read current state from IMPROVEMENT_LOG.md
2. Check the Priority Queue for next task
3. Implement the highest priority improvement
4. Run syntax check on modified files
5. Update IMPROVEMENT_LOG.md with your changes
6. If reports were affected, regenerate them

Start by reading current state, then work systematically. Document all changes.'''


def run_claude_iteration(
    iteration: int,
    budget: float = 15.0,
    model: str = "opus",
    skip_permissions: bool = True,
) -> tuple[bool, str]:
    """
    Run a single Claude Code iteration.

    Args:
        iteration: Iteration number
        budget: Max budget in USD
        model: Model to use (opus, sonnet, haiku)
        skip_permissions: Skip permission prompts

    Returns:
        Tuple of (success, output)
    """
    prompt = get_iteration_prompt(iteration)

    # Build command
    cmd = ["claude"]

    if skip_permissions:
        cmd.append("--dangerously-skip-permissions")

    cmd.extend([
        "--model", model,
        "--max-budget-usd", str(budget),
        "-p", prompt,
    ])

    print(f"\n{'='*70}")
    print(f"CLAUDE CODE HARNESS - ITERATION {iteration}")
    print(f"{'='*70}")
    print(f"  Model: {model}")
    print(f"  Budget: ${budget}")
    print(f"  Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*70}\n")

    try:
        # Run from project directory
        result = subprocess.run(
            cmd,
            cwd=str(PROJECT_ROOT),
            capture_output=True,
            text=True,
            timeout=1800,  # 30 minute timeout
        )

        output = result.stdout + result.stderr
        success = result.returncode == 0

        if success:
            print("Iteration completed successfully")
        else:
            print(f"Iteration failed with return code: {result.returncode}")

        return success, output

    except subprocess.TimeoutExpired:
        print("Iteration timed out after 30 minutes")
        return False, "Timeout"
    except FileNotFoundError:
        print("ERROR: 'claude' command not found. Is Claude Code CLI installed?")
        print("Install with: npm install -g @anthropic-ai/claude-code")
        return False, "Claude CLI not found"
    except Exception as e:
        print(f"Error running iteration: {e}")
        return False, str(e)


def log_iteration_result(iteration: int, success: bool, output: str):
    """Log the result of an iteration."""
    log_dir = PROJECT_ROOT / "data" / "harness_logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"iteration_{iteration:03d}_{timestamp}.log"

    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"Iteration: {iteration}\n")
        f.write(f"Success: {success}\n")
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"{'='*70}\n")
        f.write(output)

    print(f"Log saved to: {log_file}")


def run_continuous(
    max_iterations: int | None = None,
    budget_per_iteration: float = 15.0,
    model: str = "opus",
    delay_between: int = 30,
):
    """
    Run continuous improvement loop.

    Args:
        max_iterations: Max iterations (None = unlimited)
        budget_per_iteration: Budget per iteration
        model: Model to use
        delay_between: Seconds to wait between iterations
    """
    iteration = 1
    total_spent = 0.0
    successes = 0
    failures = 0

    print(f"\n{'='*70}")
    print("STARTING CONTINUOUS IMPROVEMENT HARNESS")
    print(f"{'='*70}")
    print(f"  Max iterations: {max_iterations or 'unlimited'}")
    print(f"  Budget per iteration: ${budget_per_iteration}")
    print(f"  Model: {model}")
    print(f"  Press Ctrl+C to stop")
    print(f"{'='*70}\n")

    try:
        while max_iterations is None or iteration <= max_iterations:
            success, output = run_claude_iteration(
                iteration,
                budget=budget_per_iteration,
                model=model,
            )

            log_iteration_result(iteration, success, output)

            if success:
                successes += 1
            else:
                failures += 1

            total_spent += budget_per_iteration  # Approximate

            print(f"\n  Progress: {successes} successes, {failures} failures")
            print(f"  Estimated spend: ~${total_spent:.2f}")

            if max_iterations is None or iteration < max_iterations:
                print(f"\n  Waiting {delay_between}s before next iteration...")
                time.sleep(delay_between)

            iteration += 1

    except KeyboardInterrupt:
        print("\n\nStopped by user")

    print(f"\n{'='*70}")
    print("HARNESS SUMMARY")
    print(f"{'='*70}")
    print(f"  Iterations run: {iteration - 1}")
    print(f"  Successes: {successes}")
    print(f"  Failures: {failures}")
    print(f"  Estimated total spend: ~${total_spent:.2f}")


def main():
    parser = argparse.ArgumentParser(
        description="Run Claude Code autonomous improvement harness",
    )

    parser.add_argument(
        "--iterations", "-n",
        type=int,
        default=1,
        help="Number of iterations to run (default: 1)",
    )
    parser.add_argument(
        "--continuous", "-c",
        action="store_true",
        help="Run continuously until stopped",
    )
    parser.add_argument(
        "--budget", "-b",
        type=float,
        default=15.0,
        help="Budget per iteration in USD (default: 15)",
    )
    parser.add_argument(
        "--model", "-m",
        type=str,
        default="opus",
        choices=["opus", "sonnet", "haiku"],
        help="Model to use (default: opus)",
    )
    parser.add_argument(
        "--delay",
        type=int,
        default=30,
        help="Seconds between iterations (default: 30)",
    )
    parser.add_argument(
        "--allow-permissions",
        action="store_true",
        help="Don't skip permission prompts (safer but requires interaction)",
    )

    args = parser.parse_args()

    if args.continuous:
        run_continuous(
            max_iterations=None,
            budget_per_iteration=args.budget,
            model=args.model,
            delay_between=args.delay,
        )
    elif args.iterations > 1:
        run_continuous(
            max_iterations=args.iterations,
            budget_per_iteration=args.budget,
            model=args.model,
            delay_between=args.delay,
        )
    else:
        # Single iteration
        success, output = run_claude_iteration(
            iteration=1,
            budget=args.budget,
            model=args.model,
            skip_permissions=not args.allow_permissions,
        )
        log_iteration_result(1, success, output)


if __name__ == "__main__":
    main()
