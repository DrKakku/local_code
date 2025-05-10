import click
import pkgutil
import problems
from runner import Runner
from utils import parse_input, prompt_for_args
from db import init_db, fetch_history
from rich.console import Console
from rich.table import Table

console = Console()
init_db()

@click.group()
def cli(): pass

@cli.command('list')
def _list():
    modules = [name for _, name, _ in pkgutil.iter_modules(problems.__path__)]
    console.print("Available problems:")
    for m in modules:
        console.print(f"- {m}")

@cli.command()
@click.argument('problem', required=False)
@click.option('--all', 'run_all', is_flag=True)
def run(problem, run_all):
    if run_all:
        for name in [n for _, n, _ in pkgutil.iter_modules(problems.__path__)]:
            console.print(f"\nRunning: {name}")
            Runner(name).run_tests()
    else:
        if not problem:
            console.print("Error: specify problem or --all")
            return
        Runner(problem).run_tests()

@cli.command()
@click.argument('problem')
def custom(problem):
    args = prompt_for_args()
    Runner(problem).run_tests([{"input": args, "output": None}])

@cli.command()
@click.option('--problem', '-p', default=None)
@click.option('--full', '-f', is_flag=True)
@click.option('--limit', '-l', type=int)
@click.option('--id', 'entry_id', type=int, help='Show specific entry by ID')
def history(problem, full, limit, entry_id):
    rows = fetch_history(problem, entry_id)
    if limit:
        rows = rows[:limit]
    table = Table(title="Submission History")
    table.add_column("ID")
    table.add_column("Problem")
    table.add_column("Case #")
    table.add_column("Status")
    table.add_column("Time (s)")
    table.add_column("Expected")
    table.add_column("Actual")
    table.add_column("Timestamp")
    table.add_column("Solution")
    for id_, prob, case_idx, status, duration, expected, actual, sol, ts in rows:
        sol_display = sol if full else sol.strip().splitlines()[0] + ' ...'
        table.add_row(str(id_), prob, str(case_idx), status, f"{duration:.4f}", expected, actual, ts, sol_display)
    console.print(table)

if __name__ == '__main__':
    cli()