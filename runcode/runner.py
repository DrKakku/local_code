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
        module = importlib.import_module(f"problems.{problem_name}")
        self.problem = module.Problem
        self.name = problem_name

    def run_tests(self, custom_tests=None):
        tests = custom_tests or self.problem.tests
        total = len(tests)
        passed = 0
        times = []
        fail_details = []

        for idx, test in enumerate(tests, 1):
            args = test.get("input", ())
            expected_val = test.get("output")
            if expected_val is None:
                expected_val = self.problem.reference_solution(*args)
            exp_str = str(expected_val)

            start = time.perf_counter()
            try:
                got_val = self.problem.user_solution(*args)
                status = got_val == expected_val
            except Exception as e:
                got_val = f"Error: {e}"
                status = False
            dur = time.perf_counter() - start
            times.append(dur)

            log_submission(
                self.name,
                idx,
                "correct" if status else "incorrect",
                dur,
                exp_str,
                str(got_val),
                inspect.getsource(self.problem.user_solution),
            )

            if status:
                passed += 1
            else:
                fail_details.append((idx, args, exp_str, str(got_val), dur))

        avg_time = sum(times) / total if total else 0
        # Summary
        console.print(
            Panel(f"Passed {passed}/{total} tests. Avg time: {avg_time:.4f}s")
        )

        # Table of failures or all if <=10
        display_all = total <= 10
        table = Table(title=self.problem.title, box=box.SIMPLE)
        table.add_column("#")
        table.add_column("Input")
        table.add_column("Expected")
        table.add_column("Got")
        table.add_column("Time (s)")
        if display_all:
            for idx, test in enumerate(tests, 1):
                exp = str(
                    test.get("output")
                    if test.get("output") is not None
                    else self.problem.reference_solution(*test.get("input", ()))
                )
                got = str(self.problem.user_solution(*test.get("input", ())))
                dur = f"{times[idx - 1]:.4f}"
                table.add_row(str(idx), str(test.get("input")), exp, got, dur)
        else:
            for idx, inp, exp, got, dur in fail_details:
                table.add_row(str(idx), str(inp), exp, got, f"{dur:.4f}")
        console.print(table)
