import click
import pkgutil
import problems
from runner import Runner
from utils import parse_input
from db import init_db

# initialize database on startup
init_db()

@click.group()
def cli():
    """LeetCode Offline Tester CLI"""
    pass

@cli.command(name='list')
def _list():
    """List available problems"""
    modules = [name for _, name, _ in pkgutil.iter_modules(problems.__path__)]
    click.echo("Available problems:")
    for m in modules:
        click.echo(f"- {m}")

@cli.command()
@click.argument('problem', required=False)
@click.option('--all', 'run_all', is_flag=True, help='Run all problems')
def run(problem, run_all):
    """Run tests for a problem, or all problems"""
    if run_all:
        modules = [name for _, name, _ in pkgutil.iter_modules(problems.__path__)]
        for name in modules:
            click.echo(f"\nRunning: {name}")
            Runner(name).run_tests()
    else:
        if not problem:
            click.echo("Error: specify a problem or use --all")
            return
        Runner(problem).run_tests()

@cli.command()
@click.argument('problem')
def custom(problem):
    """Run custom test cases for a problem"""
    sig = click.prompt("Enter input signature, e.g. [1,2,3], 6")
    args = parse_input(sig)
    custom_tests = [{"input": args, "output": None}]
    Runner(problem).run_tests(custom_tests)

if __name__ == '__main__':
    cli()