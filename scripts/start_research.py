""""""
NOTICE: This is a sanitized version for public release.
Actual test content and exploitation techniques have been removed.
This framework provides the infrastructure for safety testing.
Users must provide their own domain-specific test content.
"""



import sys
import os
import argparse
import json
from pathlib import Path
from datetime import datetime, timedelta

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from autonomous_research_coordinator import (
    AutonomousResearchCoordinator,
    ResearchPhase,
    TaskPriority
)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Launch autonomous research system for multi-day execution"
    )
    parser.add_argument(
        "--days",
        type=int,
        default=3,
        choices=[2, 3, 4, 5],
        help="Duration of autonomous research (2-5 days)"
    )
    parser.add_argument(
        "--skip-migration",
        action="store_true",
        help="Skip v2.0 structure migration (use if already migrated)"
    )
    parser.add_argument(
        "--checkpoint-interval",
        type=int,
        default=30,
        help="Checkpoint interval in minutes (default: 30)"
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=3,
        help="Maximum retries per failed task (default: 3)"
    )
    parser.add_argument(
        "--background",
        action="store_true",
        help="Run in background (log to file)"
    )
    parser.add_argument(
        "--phases",
        nargs="+",
        choices=[
            "setup", "generation", "feature_analysis", "boundary_probing",
            "advanced_generation", "multilingual", "testing", "visualization", "documentation"
        ],
        help="Specific phases to run (default: all)"
    )
    return parser.parse_args()


def display_research_plan(coordinator, duration_days):
    """Display the research plan before starting"""
    print("\n" + "="*80)
    print(f"AUTONOMOUS RESEARCH PLAN - {duration_days} DAY EXECUTION")
    print("="*80)

    print(f"\nResearch Duration: {duration_days} days ({duration_days * 24} hours)")
    print(f"Total Tasks: {len(coordinator.tasks)}")
    print(f"Checkpoint Interval: {coordinator.checkpoint_interval_minutes} minutes")
    print(f"Max Retries per Task: {coordinator.max_retries}")

    # Count tasks by phase
    phase_counts = {}
    for task in coordinator.tasks:
        phase = task.phase
        phase_counts[phase] = phase_counts.get(phase, 0) + 1

    print("\nTasks by Phase:")
    for phase, count in sorted(phase_counts.items(), key=lambda x: list(ResearchPhase).index(x[0])):
        print(f"  {phase.value:30s}: {count:3d} tasks")

    # Count by priority
    priority_counts = {}
    for task in coordinator.tasks:
        priority = task.priority
        priority_counts[priority] = priority_counts.get(priority, 0) + 1

    print("\nTasks by Priority:")
    for priority in [TaskPriority.CRITICAL, TaskPriority.HIGH, TaskPriority.MEDIUM, TaskPriority.LOW]:
        count = priority_counts.get(priority, 0)
        print(f"  {priority.value:10s}: {count:3d} tasks")

    # Estimated outputs
    print("\nExpected Outputs:")
    if duration_days >= 3:
        print(f"  New Tests: 500-700")
        print(f"  Feature Space Analysis: Complete")
        print(f"  Boundary Probes: 1,000+")
        print(f"  Visualizations: 10+ interactive HTML files")
        print(f"  Documentation: Research report + methodology")
    if duration_days >= 5:
        print(f"  Multi-language Tests: 200+")
        print(f"  Cross-model Testing: Optional")
        print(f"  Publication Package: GitLab-ready")

    # Estimated cost
    electricity_cost = duration_days * 24 * 0.01  # $0.01/hour for 100W
    print(f"\nEstimated Cost:")
    print(f"  Electricity: ${electricity_cost:.2f}")
    print(f"  API Calls: $0.00 (using Claude Code CLI)")
    print(f"  Total: ${electricity_cost:.2f}")

    print("\n" + "="*80)
    print("\nPress Ctrl+C at any time to pause (checkpoint will be saved)")
    print("Resume later with: python scripts/autonomous/resume_research.py")
    print("="*80 + "\n")


def main():
    args = parse_args()

    print("\n" + "="*80)
    print("AUTONOMOUS RESEARCH SYSTEM")
    print("LLM Trafficking Detection Benchmark - Multi-Day Execution")
    print("="*80)

    # Initialize coordinator
    print("\nInitializing autonomous research coordinator...")
    coordinator = AutonomousResearchCoordinator(
        checkpoint_interval_minutes=args.checkpoint_interval,
        max_retries=args.max_retries
    )

    # Initialize research plan
    print(f"Creating {args.days}-day research plan...")
    coordinator.initialize_research_plan(
        duration_days=args.days,
        skip_migration=args.skip_migration
    )

    # Filter to specific phases if requested
    if args.phases:
        print(f"\nFiltering to phases: {', '.join(args.phases)}")
        phase_enum_map = {
            "setup": ResearchPhase.SETUP,
            "generation": ResearchPhase.TEST_GENERATION,
            "feature_analysis": ResearchPhase.FEATURE_SPACE_ANALYSIS,
            "boundary_probing": ResearchPhase.BOUNDARY_PROBING,
            "advanced_generation": ResearchPhase.ADVANCED_GENERATION,
            "multilingual": ResearchPhase.MULTI_LANGUAGE,
            "testing": ResearchPhase.COMPREHENSIVE_TESTING,
            "visualization": ResearchPhase.VISUALIZATION,
            "documentation": ResearchPhase.DOCUMENTATION
        }
        selected_phases = [phase_enum_map[p] for p in args.phases]
        coordinator.tasks = [t for t in coordinator.tasks if t.phase in selected_phases]

    # Display plan
    display_research_plan(coordinator, args.days)

    # Confirmation
    response = input("\nStart autonomous research? [y/N]: ")
    if response.lower() != 'y':
        print("Research cancelled.")
        return

    # Calculate deadline
    max_duration_hours = args.days * 24

    # Start research
    print(f"\nStarting autonomous research at {datetime.now()}")
    print(f"Expected completion: {datetime.now() + timedelta(hours=max_duration_hours)}")
    print("\nMonitor progress with: python scripts/autonomous/monitor_progress.py\n")

    try:
        # Execute autonomous research
        summary = coordinator.execute_autonomous_research(
            max_duration_hours=max_duration_hours
        )

        # Display summary
        print("\n" + "="*80)
        print("AUTONOMOUS RESEARCH COMPLETE")
        print("="*80)
        print(f"\nCompleted: {summary['completed_tasks']}/{summary['total_tasks']} tasks")
        print(f"Duration: {summary['total_duration_hours']:.1f} hours")
        print(f"Success Rate: {summary['success_rate']:.1%}")

        if summary['failed_tasks']:
            print(f"\nFailed Tasks ({len(summary['failed_tasks'])}):")
            for task_id in summary['failed_tasks'][:10]:  # Show first 10
                print(f"  - {task_id}")

        print(f"\nCheckpoint saved to: {coordinator.checkpoint_file}")
        print(f"Full summary: {coordinator.project_root / 'data' / 'results' / 'research_summary.json'}")

        # Save detailed summary
        summary_file = coordinator.project_root / 'data' / 'results' / 'research_summary.json'
        summary_file.parent.mkdir(parents=True, exist_ok=True)
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2, default=str)

        print("\n" + "="*80)
        print("Next Steps:")
        print("  1. Review results: python scripts/analyze/analyze_results.py")
        print("  2. Generate visualizations: python scripts/visualize/generate_visualizations.py")
        print("  3. Create report: python scripts/visualize/build_dashboard.py")
        print("="*80 + "\n")

    except KeyboardInterrupt:
        print("\n\nResearch paused by user (Ctrl+C)")
        print(f"Checkpoint saved to: {coordinator.checkpoint_file}")
        print("\nResume with: python scripts/autonomous/resume_research.py")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nERROR: Research failed with exception: {e}")
        print(f"Checkpoint saved to: {coordinator.checkpoint_file}")
        print("\nCheck logs and resume with: python scripts/autonomous/resume_research.py")
        sys.exit(1)


if __name__ == "__main__":
    main()
