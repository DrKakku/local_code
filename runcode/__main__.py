import click
import pkgutil
import problems
from runner import Runner
from utils import parse_input, prompt_for_args
from db import init_db, fetch_history
from problem_creator import main as create_problem
from rich.console import Console
from rich.table import Table

console = Console()
init_db()


@click.group()
def cli():
    pass


@cli.command("list")
def _list():
    for _, name, _ in pkgutil.iter_modules(problems.__path__):
        console.print(f"- {name}")


@cli.command()
@click.argument("problem", required=False)
@click.option("--all", "run_all", is_flag=True)
def run(problem, run_all):
    if run_all:
        for _, name, _ in pkgutil.iter_modules(problems.__path__):
            console.print(f"\nRunning: {name}")
            Runner(name).run_tests()
    else:
        if not problem:
            console.print("Specify a problem or --all")
            return
        Runner(problem).run_tests()


@cli.command()
@click.argument("problem")
def custom(problem):
    args = prompt_for_args()
    Runner(problem).run_tests([{"input": args, "output": None}])


@cli.command()
@click.option("--problem", "-p")
@click.option("--full", "-f", is_flag=True)
@click.option("--limit", "-l", type=int)
@click.option("--id", "entry_id", type=int)
def history(problem, full, limit, entry_id):
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


@cli.command()
def create():
    create_problem()


if __name__ == "__main__":
    cli()
