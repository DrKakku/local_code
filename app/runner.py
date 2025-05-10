import importlib
import pkgutil
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from difflib import ndiff
from db import log_submission

console = Console()

class Runner:
    def __init__(self, problem_name: str):
        module_path = f"problems.{problem_name}"
        self.module = importlib.import_module(module_path)
        self.problem = self.module.Problem
        self.name = problem_name

    def run_tests(self, custom_tests=None):
        tests = custom_tests or self.problem.tests
        table = Table(title=self.problem.title, box=box.SIMPLE)
        table.add_column("Case", justify="center")
        table.add_column("Input", justify="left")
        table.add_column("Expected", justify="left")
        table.add_column("Got", justify="left")
        table.add_column("Result", justify="center")

        for idx, test in enumerate(tests, 1):
            expected = test.get("output")
            try:
                got = self.problem.user_solution(*test.get("input"))
                status = "✅" if got == expected else "❌"
            except Exception as e:
                got = f"Error: {e}"
                status = "❌"

            table.add_row(str(idx), str(test.get("input")), str(expected), str(got), status)

            # log each submission
            log_submission(self.name, 'correct' if status == '✅' else 'incorrect')

            if status == "❌":
                ref = self.problem.reference_solution(*test.get("input"))
                diff = '\n'.join(ndiff(str(ref).split(), str(got).split()))
                console.print(Panel(diff, title="Difference (ref vs yours)"))

        console.print(table)