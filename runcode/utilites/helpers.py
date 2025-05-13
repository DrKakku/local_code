import ast
import csv
import pkgutil

from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

import problems as problems
from utilites.db import fetch_history
from utilites.runner import Runner
from utilites.utils import parse_input

console = Console()


def choose_problem(pre_selected=None):
    modules = [name for _, name, _ in pkgutil.iter_modules(problems.__path__)]
    if not modules:
        console.print("[red]No problems available![/red]")
        raise SystemExit

    if pre_selected:
        try:
            indices = [int(i.strip()) - 1 for i in pre_selected.split(",")]
            if any(i < 0 or i >= len(modules) for i in indices):
                raise ValueError
            return [modules[i] for i in indices]
        except ValueError:
            console.print("[red]Invalid selection, aborting.[/red]")
            raise SystemExit

    console.print("📚 Pick a problem (you can select multiple, e.g., 1,3,5):")
    for i, m in enumerate(modules, 1):
        console.print(f"  {i}. {m}")
    try:
        choices = Prompt.ask(f"Enter number(s) [1-{len(modules)}] (comma-separated)")
        indices = [int(i.strip()) - 1 for i in choices.split(",")]
        if any(i < 0 or i >= len(modules) for i in indices):
            raise ValueError
        return [modules[i] for i in indices]
    except ValueError:
        console.print("[red]Invalid selection, aborting.[/red]")
        raise SystemExit


def _run_custom_tests(problem):
    mode = Prompt.ask(
        "How do you want to provide test cases?",
        choices=["interactive", "text"],
        default="interactive",
    )

    custom_tests = []

    if mode == "text":
        text_path = Prompt.ask(
            "Enter path to text file (one test case per line, Python tuple or args)"
        )
        try:
            with open(text_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    try:
                        args = parse_input(line)
                    except Exception as e:
                        console.print(f"[red]Invalid input in line: {line} ({e})[/red]")
                        continue
                    custom_tests.append({"input": args, "output": None})
        except Exception as e:
            console.print(f"[red]Failed to read text file: {e}[/red]")
            return
    else:
        while True:
            input_str = Prompt.ask("Enter input args (Python tuple, e.g. (1,2,3))")
            try:
                args = ast.literal_eval(input_str)
                if not isinstance(args, tuple):
                    args = (args,)
            except Exception as e:
                console.print(f"[red]Invalid input: {e}[/red]")
                continue

            output = None
            if (
                Prompt.ask("Provide expected output?", choices=["y", "n"], default="n")
                == "y"
            ):
                out_raw = Prompt.ask("Enter expected output (Python literal)")
                try:
                    output = ast.literal_eval(out_raw)
                except Exception as e:
                    console.print(f"[red]Invalid output literal: {e}[/red]")
                    continue

            custom_tests.append({"input": args, "output": output})

            if (
                Prompt.ask("Add another test case?", choices=["y", "n"], default="n")
                == "n"
            ):
                break

    Runner(problem).run_tests(custom_tests)


def _fetch_and_display_history(problem, full, limit, entry_id):
    rows = fetch_history(problem, entry_id)
    if limit:
        rows = rows[:limit]
    table = Table(title=f"History for {problem or 'All Problems'}")
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
