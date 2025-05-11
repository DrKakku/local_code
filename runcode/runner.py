import importlib
import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from difflib import ndiff
import inspect
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
        table.add_column("Time (s)", justify="center")

        for idx, test in enumerate(tests, 1):
            args = test.get("input", ())
            expected_val = test.get("output")
            if expected_val is None:
                expected_val = self.problem.reference_solution(*args)
            expected_str = str(expected_val)

            start = time.perf_counter()
            try:
                got_val = self.problem.user_solution(*args)
                status = "✅" if got_val == expected_val else "❌"
            except Exception as e:
                got_val = f"Error: {e}"
                status = "❌"
            duration = time.perf_counter() - start
            got_str = str(got_val)

            table.add_row(
                str(idx), str(args), expected_str, got_str, status, f"{duration:.4f}"
            )

            src = inspect.getsource(self.problem.user_solution)
            log_submission(
                self.name,
                idx,
                "correct" if status == "✅" else "incorrect",
                duration,
                expected_str,
                got_str,
                src,
            )

            if status == "❌":
                diff = "\n".join(ndiff(expected_str.split(), got_str.split()))
                console.print(Panel(diff, title="Difference (ref vs yours)"))

        console.print(table)
