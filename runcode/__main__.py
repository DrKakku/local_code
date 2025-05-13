import click
import pkgutil
from rich.console import Console
from utilites.utils import safe_command
from utilites.runner import Runner
from utilites.db import init_db
from utilites.problem_creator import main as create_problem
from utilites.helpers import choose_problem, _run_custom_tests, _fetch_and_display_history
import problems

console = Console()

init_db()

@click.group()
def cli():
    """Run LeetCode-style problems offline."""
    pass

@safe_command
@cli.command("list")
def _list():
    for _, name, _ in pkgutil.iter_modules(problems.__path__):
        console.print(f"- {name}")

@safe_command
@cli.command()
@click.argument("problem", required=False)
@click.option("--all", "run_all", is_flag=True)
@click.option("--select","-s", "pre_selected", default=None, help="Comma-separated problem numbers to run")
def run(problem, run_all, pre_selected):
    try:
        if run_all:
            for _, name, _ in pkgutil.iter_modules(problems.__path__):
                console.print(f"\nRunning: {name}")
                Runner(name).run_tests()
            return

        # Extract nested conditional expression
        if pre_selected:
            problems_to_run = choose_problem(pre_selected)
        elif not problem:
            problems_to_run = choose_problem()
        else:
            problems_to_run = [problem]

        for prob in problems_to_run:
            console.print(f"\nRunning: {prob}")
            Runner(prob).run_tests()
    except Exception as e:
        console.print(f"[bold red]An error occurred:[/bold red] {e}")

@safe_command
@cli.command()
@click.argument("problem", required=False)
@click.option("--select","-s", "pre_selected", default=None, help="Comma-separated problem numbers to run custom tests")
def custom(problem, pre_selected):
    try:
        # Extract nested conditional expression
        if pre_selected:
            problems_to_run = choose_problem(pre_selected)
        elif not problem:
            problems_to_run = choose_problem()
        else:
            problems_to_run = [problem]

        for prob in problems_to_run:
            console.print(f"\nRunning custom tests for: {prob}")
            _run_custom_tests(prob)
    except Exception as e:
        console.print(f"[bold red]An error occurred:[/bold red] {e}")

@safe_command
@cli.command()
@click.option("--problem", "-p", default=None)
@click.option("--full", "-f", is_flag=True)
@click.option("--limit", "-l", type=int)
@click.option("--id", "entry_id", type=int)
@click.option("--select","-s", "pre_selected", default=None, help="Comma-separated problem numbers to view history")
def history(problem, full, limit, entry_id, pre_selected):
    try:
        # Extract nested conditional expression
        if pre_selected:
            problems_to_view = choose_problem(pre_selected)
        elif not problem:
            problems_to_view = choose_problem()
        else:
            problems_to_view = [problem]

        for prob in problems_to_view:
            console.print(f"\nHistory for: {prob}")
            _fetch_and_display_history(prob, full, limit, entry_id)
    except Exception as e:
        console.print(f"[bold red]An error occurred:[/bold red] {e}")

@safe_command
@cli.command()
def create():
    create_problem()

if __name__ == "__main__":
    cli()