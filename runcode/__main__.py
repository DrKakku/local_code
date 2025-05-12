import click
import pkgutil
import problems
from utils import safe_command
from runner import Runner
from utils import parse_input, prompt_for_args
from db import init_db, fetch_history
from problem_creator import main as create_problem
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import ast



console = Console()
init_db()

def choose_problem():
    modules = [name for _, name, _ in pkgutil.iter_modules(problems.__path__)]
    if not modules:
        console.print("[red]No problems available![/red]")
        raise SystemExit
    console.print("📚 Pick a problem:")
    for i, m in enumerate(modules, 1):
        console.print(f"  {i}. {m}")
    try:
        choice = int(Prompt.ask(f"Enter number [1-{len(modules)}]")) - 1
        if choice < 0 or choice >= len(modules):
            raise ValueError
        return modules[choice]
    except ValueError:
        console.print("[red]Invalid selection, aborting.[/red]")
        raise SystemExit


@click.group()
def cli():
    pass

@safe_command
@cli.command("list")
def _list():
    for _, name, _ in pkgutil.iter_modules(problems.__path__):
        console.print(f"- {name}")

@safe_command
@cli.command()
@click.argument('problem', required=False)
@click.option('--all', 'run_all', is_flag=True)
def run(problem, run_all):
    """
    Run tests for a problem, or all problems. If no problem specified, prompt user to choose one interactively.
    """
    try:
        # Run all problems
        if run_all:
            for _, name, _ in pkgutil.iter_modules(problems.__path__):
                console.print(f"\nRunning: {name}")
                Runner(name).run_tests()
            return

        # Prompt user if no problem specified
        if not problem:
            problem = choose_problem()
        Runner(problem).run_tests()

    except Exception as e:
        console.print(f"[bold red]An error occurred:[/bold red] {e}")

@safe_command
@cli.command()
@click.argument("problem", required=False)
def custom(problem):
    """
        Run custom test cases for a problem, optionally with expected output.
        """
    # 1) Choose problem if none specified
    if not problem:
        problem = choose_problem()

    # 2) Ask for the function inputs
    args = prompt_for_args()

    # 3) Optionally prompt for expected output
    expected = None
    if Prompt.ask("Provide expected output?", choices=["y", "n"], default="n") == "y":
        out_raw = Prompt.ask("Enter expected output (Python literal)")
        try:
            expected = ast.literal_eval(out_raw)
        except Exception as e:
            console.print(f"[red]Invalid output literal: {e}[/red]")
            return

    # 4) Build the test case and run it
    custom_tests = [{"input": args, "output": expected}]
    Runner(problem).run_tests(custom_tests)

@safe_command
@cli.command()
@click.option("--problem", "-p", default=None)
@click.option("--full", "-f", is_flag=True)
@click.option("--limit", "-l", type=int)
@click.option("--id", "entry_id", type=int)
def history(problem, full, limit, entry_id):
    if entry_id is None and problem is None:
        problem = choose_problem()
    rows = fetch_history(problem, entry_id)
    if limit:
        rows = rows[:limit]
    table = Table(title="History")
    cols = ["ID", "Prob", "Case", "Status", "Time", "Exp", "Act", "TimeStamp", "Sol"]
    for col in cols:
        table.add_column(col)
    for r in rows:
        id_, prob, idx, st, dur, exp, act, sol, ts = r
        sol_disp = sol if full else sol.splitlines()[0] + " ..."
        table.add_row(
            str(id_), prob, str(idx), st, f"{dur:.4f}", exp, act, ts, sol_disp
        )
    console.print(table)

@safe_command
@cli.command()
def create():
    create_problem()


if __name__ == "__main__":
    cli()
