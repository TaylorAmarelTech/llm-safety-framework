"""
LLM Safety Framework - Command Line Interface

Provides CLI commands for:
- Running safety tests
- Managing configurations
- Starting the web server
- Generating test cases
- Viewing results
"""

import os
import sys
import json
from pathlib import Path
from typing import Optional, List
from datetime import datetime

import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

# Initialize Typer app and Rich console
app = typer.Typer(
    name="llm-safety",
    help="LLM Safety Testing Framework - Test LLM guardrails against exploitation scenarios",
    add_completion=False,
)
console = Console()


# =============================================================================
# Server Commands
# =============================================================================

@app.command()
def serve(
    host: str = typer.Option("0.0.0.0", "--host", "-h", help="Host to bind to"),
    port: int = typer.Option(8080, "--port", "-p", help="Port to bind to"),
    reload: bool = typer.Option(False, "--reload", "-r", help="Enable auto-reload for development"),
    workers: int = typer.Option(1, "--workers", "-w", help="Number of worker processes"),
):
    """Start the web dashboard server."""
    import uvicorn

    console.print(Panel.fit(
        f"[bold green]Starting LLM Safety Framework[/bold green]\n"
        f"Dashboard: http://{host}:{port}\n"
        f"API Docs: http://{host}:{port}/api/docs",
        title="LLM Safety Framework",
    ))

    uvicorn.run(
        "src.web.app:app",
        host=host,
        port=port,
        reload=reload,
        workers=workers if not reload else 1,
    )


@app.command()
def api(
    host: str = typer.Option("0.0.0.0", "--host", "-h", help="Host to bind to"),
    port: int = typer.Option(8000, "--port", "-p", help="Port to bind to"),
    reload: bool = typer.Option(False, "--reload", "-r", help="Enable auto-reload"),
):
    """Start the standalone API server (no web UI)."""
    import uvicorn

    console.print(Panel.fit(
        f"[bold blue]Starting API Server[/bold blue]\n"
        f"API: http://{host}:{port}\n"
        f"Docs: http://{host}:{port}/docs",
        title="LLM Safety API",
    ))

    uvicorn.run(
        "src.api:app",
        host=host,
        port=port,
        reload=reload,
    )


# =============================================================================
# Test Commands
# =============================================================================

@app.command()
def test(
    categories: Optional[List[str]] = typer.Option(None, "--category", "-c", help="Test categories to run"),
    corridors: Optional[List[str]] = typer.Option(None, "--corridor", help="Migration corridors to test"),
    models: Optional[List[str]] = typer.Option(None, "--model", "-m", help="Models to test against"),
    batch_size: int = typer.Option(10, "--batch-size", "-b", help="Number of tests per batch"),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="Output file for results"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Show what would be tested without running"),
):
    """Run safety tests against configured models."""
    console.print("[bold]LLM Safety Test Runner[/bold]\n")

    if dry_run:
        console.print("[yellow]Dry run mode - no tests will be executed[/yellow]\n")

    # Display configuration
    table = Table(title="Test Configuration")
    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Categories", ", ".join(categories) if categories else "All")
    table.add_row("Corridors", ", ".join(corridors) if corridors else "All")
    table.add_row("Models", ", ".join(models) if models else "From config")
    table.add_row("Batch Size", str(batch_size))
    table.add_row("Output", str(output) if output else "Console")

    console.print(table)

    if dry_run:
        return

    console.print("\n[yellow]Test execution: Use 'llm-safety serve' to run tests via web UI[/yellow]")


@app.command()
def generate(
    count: int = typer.Option(100, "--count", "-n", help="Number of test cases to generate"),
    category: Optional[str] = typer.Option(None, "--category", "-c", help="Specific category to generate"),
    corridor: Optional[str] = typer.Option(None, "--corridor", help="Specific corridor to generate for"),
    output: Path = typer.Option(Path("data/generated_tests.json"), "--output", "-o", help="Output file"),
    all_categories: bool = typer.Option(False, "--all", help="Generate for all categories"),
):
    """Generate new test cases."""
    console.print("[bold]Test Case Generator[/bold]\n")

    table = Table(title="Generation Settings")
    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")
    table.add_row("Count", str(count))
    table.add_row("Category", category if category else "All" if all_categories else "Default")
    table.add_row("Corridor", corridor if corridor else "All")
    table.add_row("Output", str(output))
    console.print(table)

    # Ensure output directory exists
    output.parent.mkdir(parents=True, exist_ok=True)

    console.print(f"\n[green]Output will be saved to: {output}[/green]")


# =============================================================================
# Configuration Commands
# =============================================================================

@app.command()
def config(
    show: bool = typer.Option(False, "--show", "-s", help="Show current configuration"),
    provider: Optional[str] = typer.Option(None, "--provider", "-p", help="Provider for API key operations"),
    api_key: Optional[str] = typer.Option(None, "--api-key", "-k", help="Set API key for provider"),
):
    """Manage framework configuration."""
    if show:
        console.print("[bold]Current Configuration[/bold]\n")

        # Show environment variables
        table = Table(title="API Keys Status")
        table.add_column("Provider", style="cyan")
        table.add_column("Variable", style="dim")
        table.add_column("Status", style="green")

        providers = [
            ("OpenAI", "OPENAI_API_KEY"),
            ("Anthropic", "ANTHROPIC_API_KEY"),
            ("Mistral", "MISTRAL_API_KEY"),
            ("Together", "TOGETHER_API_KEY"),
        ]

        for name, var in providers:
            value = os.environ.get(var)
            if value:
                status = f"[green]Set[/green] (***{value[-4:]})"
            else:
                status = "[yellow]Not set[/yellow]"
            table.add_row(name, var, status)

        console.print(table)

        # Show other settings
        settings_table = Table(title="Framework Settings")
        settings_table.add_column("Setting", style="cyan")
        settings_table.add_column("Value", style="green")
        settings_table.add_row("LOG_LEVEL", os.environ.get("LOG_LEVEL", "INFO"))
        settings_table.add_row("DATA_DIR", os.environ.get("DATA_DIR", "data"))
        console.print(settings_table)
        return

    if provider and api_key:
        env_var = f"{provider.upper()}_API_KEY"
        console.print(f"[yellow]To set {env_var}, add to your .env file:[/yellow]")
        console.print(f"  {env_var}={api_key[:8]}...")
        return

    console.print("Use --show to view configuration")
    console.print("Use --provider and --api-key to configure API keys")


# =============================================================================
# Data Commands
# =============================================================================

@app.command(name="import")
def import_data(
    file: Path = typer.Argument(..., help="File to import (JSON)"),
    data_type: str = typer.Option("prompts", "--type", "-t", help="Data type: prompts, cases, docs"),
    merge: bool = typer.Option(True, "--merge/--replace", help="Merge with existing or replace"),
):
    """Import data from JSON files."""
    if not file.exists():
        console.print(f"[red]Error: File not found: {file}[/red]")
        raise typer.Exit(1)

    console.print(f"[bold]Importing {data_type} from {file}[/bold]\n")

    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if data_type == "prompts":
        count = len(data.get("test_suites", {}).values())
        console.print(f"[green]Found {count} test suites to import[/green]")
    elif data_type == "cases":
        count = len(data.get("cases", []))
        console.print(f"[green]Found {count} cases to import[/green]")
    elif data_type == "docs":
        count = len(data.get("documents", []))
        console.print(f"[green]Found {count} documents to import[/green]")

    console.print(f"Mode: {'Merge' if merge else 'Replace'}")


@app.command(name="export")
def export_data(
    output: Path = typer.Argument(..., help="Output file path"),
    data_type: str = typer.Option("prompts", "--type", "-t", help="Data type: prompts, cases, results"),
    format: str = typer.Option("json", "--format", "-f", help="Output format: json, csv"),
):
    """Export data to file."""
    console.print(f"[bold]Exporting {data_type} to {output}[/bold]\n")
    console.print(f"Format: {format}")

    output.parent.mkdir(parents=True, exist_ok=True)
    console.print(f"[green]Export would be saved to: {output}[/green]")


# =============================================================================
# Info Commands
# =============================================================================

@app.command()
def info():
    """Show framework information and status."""
    console.print(Panel.fit(
        "[bold]LLM Safety Testing Framework[/bold]\n\n"
        "A modular framework for testing LLM safety systems against\n"
        "adversarial prompts related to human trafficking and labor exploitation.\n\n"
        "[cyan]Version:[/cyan] 1.0.0\n"
        "[cyan]Python:[/cyan] 3.11+\n"
        "[cyan]License:[/cyan] MIT",
        title="About",
    ))

    # Check dependencies
    console.print("\n[bold]Dependency Status[/bold]\n")

    deps = [
        ("fastapi", "API Server"),
        ("uvicorn", "ASGI Server"),
        ("pydantic", "Data Validation"),
        ("sqlalchemy", "Database ORM"),
        ("openai", "OpenAI Provider"),
        ("anthropic", "Anthropic Provider"),
        ("mistralai", "Mistral Provider"),
        ("rich", "Terminal UI"),
        ("typer", "CLI Framework"),
    ]

    table = Table()
    table.add_column("Package", style="cyan")
    table.add_column("Purpose")
    table.add_column("Status")

    for package, purpose in deps:
        try:
            __import__(package)
            status = "[green]Installed[/green]"
        except ImportError:
            status = "[red]Missing[/red]"
        table.add_row(package, purpose, status)

    console.print(table)


@app.command()
def stats(
    data_dir: Path = typer.Option(Path("data"), "--data-dir", "-d", help="Data directory"),
):
    """Show statistics about available test data."""
    console.print("[bold]Test Data Statistics[/bold]\n")

    prompts_file = data_dir / "sample_test_prompts.json"

    if prompts_file.exists():
        with open(prompts_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        total = sum(len(s) for s in data.get("test_suites", {}).values())

        table = Table(title="Test Prompts by Suite")
        table.add_column("Suite", style="cyan")
        table.add_column("Count", style="green", justify="right")

        for suite, prompts in data.get("test_suites", {}).items():
            table.add_row(suite, str(len(prompts)))

        table.add_row("[bold]Total[/bold]", f"[bold]{total}[/bold]")
        console.print(table)
    else:
        console.print(f"[yellow]No test prompts found at {prompts_file}[/yellow]")

    # Check for database
    db_file = data_dir / "trafficking_tests.db"
    if db_file.exists():
        console.print(f"\n[green]Database found: {db_file}[/green]")
        console.print(f"Size: {db_file.stat().st_size / 1024 / 1024:.2f} MB")


# =============================================================================
# Main Entry Point
# =============================================================================

def main():
    """Main entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
