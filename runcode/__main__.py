import pkgutil

import click
from rich.console import Console

import problems
from utilites.db import init_db
from utilites.helpers import _run_custom_tests, _fetch_and_display_history
from utilites.helpers import choose_problem
from utilites.problem_creator import main as create_problem
from utilites.runner import Runner
from utilites.summary_helpers import (
    get_problem_details,
    format_value,
    get_additional_variables,
    create_summary_panel,
    create_summary_table,
    update_totals_in_table,
    add_problem_row_in_summary_table,
)
from utilites.utils import safe_command

import statistics
from rich.table import Table
import inspect

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
@click.option("--all", "-a", "run_all", is_flag=True)
@click.option(
    "--select",
    "-s",
    "pre_selected",
    default=None,
    help="Comma-separated problem numbers to run",
)
@click.option(
    "--table", "as_table", is_flag=True, help="Display summary in a tabular format"
)
def run(problem, run_all, pre_selected, as_table):
    try:
        if run_all:
            summary = []
            for _, name, _ in pkgutil.iter_modules(problems.__path__):
                problem_module = __import__(f"problems.{name}", fromlist=[""])
                problem_class = getattr(problem_module, "Problem", None)
                if not problem_class:
                    continue
                user_impl = hasattr(
                    problem_class, "user_solution"
                ) and "NotImplementedError" not in inspect.getsource(
                    problem_class.user_solution
                )
                ref_impl = hasattr(
                    problem_class, "reference_solution"
                ) and "NotImplementedError" not in inspect.getsource(
                    problem_class.reference_solution
                )
                if not (user_impl or ref_impl):
                    continue

                console.print(f"\nRunning: {name}")
                runner = Runner(name)
                results = runner.run_tests(return_results=True)
                if not results:
                    continue
                # Use analytics from the first result (all have the same analytics)
                analytics = results[0]
                summary.append(
                    {
                        "problem": name,
                        "total": analytics["total"],
                        "passed": analytics["passed"],
                        "failed": analytics["failed"],
                        "avg_time": analytics["avg_time"],
                        "min_time": analytics["min_time"],
                        "max_time": analytics["max_time"],
                        "pass_rate": analytics["pass_rate"],
                        "failed_indices": analytics["failed_indices"],
                    }
                )

            if as_table:
                table = Table(title="Run Summary", border_style="blue")
                table.add_column("Problem", style="cyan")
                table.add_column("Total", justify="right")
                table.add_column("Passed", justify="right", style="green")
                table.add_column("Failed", justify="right", style="red")
                table.add_column("Avg Time (ms)", justify="right")
                table.add_column("Min Time (ms)", justify="right")
                table.add_column("Max Time (ms)", justify="right")
                table.add_column("Pass Rate (%)", justify="right")
                table.add_column("Failed Indices", style="yellow")

                for row in summary:
                    print(row)
                    table.add_row(
                        row["problem"],
                        str(row["total"]),
                        str(row["passed"]),
                        str(row["failed"]),
                        f"{row['avg_time']:.4f}",
                        f"{row.get('min_time', 0.0):.4f}",
                        f"{row.get('max_time', 0.0):.4f}",
                        f"{row.get('pass_rate', 0.0):.2f}",
                        ", ".join(str(idx) for idx in row.get("failed_indices", []))
                        if row.get("failed_indices")
                        else "-",
                    )
                console.print(table)
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
@click.option(
    "--select",
    "-s",
    "pre_selected",
    default=None,
    help="Comma-separated problem numbers to run custom tests",
)
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
@click.option(
    "--select",
    "-s",
    "pre_selected",
    default=None,
    help="Comma-separated problem numbers to view history",
)
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


@safe_command
@cli.command()
@click.option(
    "--all", "-a", "view_all", is_flag=True, help="View summary of all problems"
)
@click.option(
    "--select",
    "-s",
    "pre_selected",
    default=None,
    help="Comma-separated problem numbers to view summary",
)
@click.option(
    "--table", "as_table", is_flag=True, help="Display summary in a tabular format"
)
@click.argument("problem", required=False)
def summary(problem: str, view_all: bool, pre_selected: str, as_table: bool) -> None:
    """
    View a summary of all problems, including descriptions, test cases, and solution status.
    """
    try:
        if view_all:
            problems_to_view = [
                name for _, name, _ in pkgutil.iter_modules(problems.__path__)
            ]
            as_table = True  # Force table format for --all
        elif pre_selected:
            problems_to_view = choose_problem(pre_selected)
        elif not problem:
            problems_to_view = choose_problem()
        else:
            problems_to_view = [problem]

        if as_table:
            table = create_summary_table()

        for prob in problems_to_view:
            problem_module = __import__(f"problems.{prob}", fromlist=[""])
            problem_class = getattr(problem_module, "Problem", None)

            if not problem_class:
                console.print(
                    f"[bold red]Problem class not found in: {prob}[/bold red]"
                )
                continue

            (
                title,
                description,
                test_case_count,
                user_solution_implemented,
                reference_solution,
            ) = get_problem_details(problem_class)
            additional_vars = get_additional_variables(problem_class)

            if as_table:
                add_problem_row_in_summary_table(table, problem_class)
            else:
                panel = create_summary_panel(
                    prob,
                    title,
                    description,
                    test_case_count,
                    user_solution_implemented,
                    reference_solution,
                    additional_vars,
                )
                console.print(panel)

        if as_table:
            console.print(table)

    except Exception as e:
        console.print(f"[bold red]An error occurred:[/bold red] {e}")


if __name__ == "__main__":
    cli()
