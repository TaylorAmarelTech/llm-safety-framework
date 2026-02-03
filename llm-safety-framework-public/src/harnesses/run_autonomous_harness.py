""""""
NOTICE: This is a sanitized version for public release.
Actual test content and exploitation techniques have been removed.
This framework provides the infrastructure for safety testing.
Users must provide their own domain-specific test content.
"""



import argparse
import asyncio
import os
import sys
from pathlib import Path

# Fix Windows encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from dotenv import load_dotenv

# Load environment variables
load_dotenv(PROJECT_ROOT / ".env")


async def main():
    parser = argparse.ArgumentParser(
        description="Run the autonomous self-evolving LLM safety benchmark",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                        # Run indefinitely with default settings
  %(prog)s --iterations 50        # Run 50 iterations
  %(prog)s --hours 4              # Run for 4 hours
  %(prog)s --simulate             # Simulation mode (no API calls)
  %(prog)s --tests-per-iter 200   # 200 tests per iteration
  %(prog)s --mutations 20         # 20 mutations per iteration
        """,
    )

    # Runtime limits
    parser.add_argument(
        "--iterations", "-n",
        type=int,
        default=None,
        help="Maximum iterations (default: unlimited)",
    )
    parser.add_argument(
        "--hours", "-H",
        type=float,
        default=None,
        help="Maximum runtime in hours (default: unlimited)",
    )

    # Configuration
    parser.add_argument(
        "--tests-per-iter",
        type=int,
        default=100,
        help="Tests to run per iteration (default: 100)",
    )
    parser.add_argument(
        "--mutations",
        type=int,
        default=10,
        help="Mutations per iteration (default: 10)",
    )
    parser.add_argument(
        "--models",
        type=str,
        default="mistral-large-latest",
        help="Comma-separated list of models to test",
    )

    # Modes
    parser.add_argument(
        "--simulate",
        action="store_true",
        help="Simulation mode (no actual API calls)",
    )
    parser.add_argument(
        "--no-evolution",
        action="store_true",
        help="Disable attack evolution",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume from last saved state",
    )

    # Output
    parser.add_argument(
        "--data-dir",
        type=str,
        default="data",
        help="Data directory (default: data)",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output",
    )

    args = parser.parse_args()

    # Print banner
    print("""
======================================================================
          AUTONOMOUS SELF-EVOLVING LLM SAFETY BENCHMARK
----------------------------------------------------------------------
  This harness continuously evolves attack strategies to test
  LLM guardrails against migrant worker exploitation scenarios.

  Purpose: DEFENSIVE SECURITY RESEARCH
======================================================================
    """)

    # Import harness components
    from src.harness.orchestrator import AutonomousOrchestrator, IterationConfig

    # Setup LLM provider
    llm_provider = None

    if not args.simulate:
        api_key = os.environ.get("MISTRAL_API_KEY")

        if not api_key:
            print("ERROR: MISTRAL_API_KEY not set")
            print("Set it in .env file or environment variable")
            print("Or use --simulate for simulation mode")
            sys.exit(1)

        try:
            from src.llm_engine.mistral_provider import MistralProvider
            llm_provider = MistralProvider(api_key=api_key)
            print(f"  LLM Provider: Mistral AI")
            print(f"  Models: {args.models}")
        except ImportError:
            print("Warning: MistralProvider not found, creating minimal provider")
            llm_provider = MinimalMistralProvider(api_key)

    else:
        print("  Mode: SIMULATION (no API calls)")

    # Create configuration
    config = IterationConfig(
        tests_per_iteration=args.tests_per_iter,
        models_to_test=args.models.split(","),
        evolution_enabled=not args.no_evolution,
        mutations_per_iteration=args.mutations,
    )

    print(f"\n  Configuration:")
    print(f"    Tests per iteration: {config.tests_per_iteration}")
    print(f"    Mutations per iteration: {config.mutations_per_iteration}")
    print(f"    Evolution: {'enabled' if config.evolution_enabled else 'disabled'}")

    if args.iterations:
        print(f"    Max iterations: {args.iterations}")
    if args.hours:
        print(f"    Max runtime: {args.hours} hours")

    # Create orchestrator
    orchestrator = AutonomousOrchestrator(
        config=config,
        data_dir=PROJECT_ROOT / args.data_dir,
        llm_provider=llm_provider,
    )

    # Run
    try:
        await orchestrator.run_continuous(
            max_iterations=args.iterations,
            max_hours=args.hours,
        )
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
    finally:
        print("\nHarness stopped.")


class MinimalMistralProvider:
    """Minimal Mistral provider for when full provider isn't available."""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.mistral.ai/v1"

    async def generate(
        self,
        prompt: str,
        system_prompt: str = "",
        temperature: float = 0.5,
        max_tokens: int = 2000,
        **kwargs,
    ) -> tuple[str, float, int]:
        """Generate a response from Mistral."""
        import httpx
        import time

        start = time.time()

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                f"{self.base_url}/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "mistral-large-latest",
                    "messages": messages,
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                },
            )

            response.raise_for_status()
            data = response.json()

            content = data["choices"][0]["message"]["content"]
            tokens = data.get("usage", {}).get("total_tokens", 0)
            latency = (time.time() - start) * 1000

            return content, latency, tokens


if __name__ == "__main__":
    asyncio.run(main())
