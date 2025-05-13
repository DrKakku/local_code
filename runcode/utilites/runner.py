import importlib
import time
import io
from contextlib import redirect_stdout
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
import inspect
from utilites.db import log_submission

console = Console()

MAX_TEST_DETAILS = 10  # Constant for maximum test details to display


class Runner:
    def __init__(self, problem_name: str):
        try:
            module = importlib.import_module(f"problems.{problem_name}")
            self.problem = module.Problem
            self.name = problem_name
        except ModuleNotFoundError as e:
            console.print(
                f"[red]Error: Problem module '{problem_name}' not found.[/red]"
            )
            raise e

    def run_tests(self, custom_tests=None, return_results=False, print_results=True):
        tests = custom_tests or self.problem.tests
        results = [self._run_single(idx, test) for idx, test in enumerate(tests, 1)]

        # Add analytics for summary table
        total = len(results)
        passed = sum(r["status"] for r in results)
        failed = total - passed
        times = [r["time"] for r in results]
        avg_time = sum(times) / total if total else 0.0
        min_time = min(times) if times else 0.0
        max_time = max(times) if times else 0.0
        pass_rate = (passed / total) * 100 if total else 0.0
        failed_indices = [r["idx"] for r in results if not r["status"]]
        # Attach analytics to results for summary
        results = [
            {
                **r,
                "total": total,
                "passed": passed,
                "failed": failed,
                "avg_time": avg_time,
                "min_time": min_time,
                "max_time": max_time,
                "pass_rate": pass_rate,
                "failed_indices": failed_indices,
            }
            for r in results
        ]

        if print_results:
            self._print_summary(results)
            self._print_details(results)

        if return_results:
            return results

    def _run_single(self, idx, test):
        args = test.get("input", ())
        expected = test.get("output")  # Use provided output if available
        exp_str = str(expected) if expected is not None else "N/A"

        buf = io.StringIO()
        start_time = time.perf_counter()

        try:
            with redirect_stdout(buf):
                got_val = self.problem.user_solution(*args)
            status = got_val == expected if expected is not None else False
        except Exception as e:
            got_val = f"Error: {e}"
            status = False

        duration = (
            (time.perf_counter() - start_time) / 1000
            if False
            else (time.perf_counter() - start_time) * 1000
        )  # ms
        out_str = buf.getvalue().strip()

        # Run reference solution only if expected output is not provided
        if expected is None:
            try:
                expected = self._get_reference_output(args)
                exp_str = str(expected)
                status = got_val == expected
            except Exception as e:
                console.print(f"[red]Error in reference solution: {e}[/red]")
                got_val = f"Error: {e}"
                status = False

        self._log_submission(idx, status, duration, exp_str, got_val)
        return self._format_result(
            idx, args, exp_str, got_val, duration, out_str, status
        )

    def _get_reference_output(self, args):
        try:
            return self.problem.reference_solution(*args)
        except Exception as e:
            console.print(f"[red]Error in reference solution: {e}[/red]")
            raise e

    def _log_submission(self, idx, status, duration, expected, got_val):
        log_submission(
            self.name,
            idx,
            "correct" if status else "incorrect",
            duration,
            expected,
            str(got_val),
            inspect.getsource(self.problem.user_solution),
        )

    def _format_result(self, idx, args, expected, got, duration, stdout, status):
        return {
            "idx": idx,
            "input": args,
            "exp": expected,
            "got": str(got),
            "time": duration,
            "out": stdout,
            "status": status,
        }

    def _print_summary(self, results):
        total = len(results)
        passed = sum(r["status"] for r in results)
        failed = total - passed
        times = [r["time"] for r in results]
        avg_time = round(sum(times) / total, 1) if total else 0.0
        min_time = round(min(times), 1) if times else 0.0
        max_time = round(max(times), 1) if times else 0.0
        pass_rate = round((passed / total) * 100, 1) if total else 0.0
        failed_indices = [str(r["idx"]) for r in results if not r["status"]]

        tbl = Table(box=box.SIMPLE_HEAVY)
        tbl.add_column("🎯 Total", justify="center")
        tbl.add_column("✅ Passed", justify="center")
        tbl.add_column("❌ Failed", justify="center")
        tbl.add_column("⏱️ Avg (ms)", justify="center")
        tbl.add_column("⏱️ Min (ms)", justify="center")
        tbl.add_column("⏱️ Max (ms)", justify="center")
        tbl.add_column("🏆 Pass Rate (%)", justify="center")
        tbl.add_column("❌ Failed Indices", justify="center")

        tbl.add_row(
            str(total),
            str(passed),
            str(failed),
            f"{avg_time} ms",
            f"{min_time} ms",
            f"{max_time} ms",
            f"{pass_rate}%",
            ", ".join(failed_indices) if failed_indices else "-",
        )

        console.print(Panel(tbl, title="🚀 Test Summary 🚀", box=box.ROUNDED))

    def _print_details(self, results):
        tbl = Table(title="🧪 Test Details 🧪", box=box.ROUNDED)
        tbl.add_column("🔢 #")
        tbl.add_column("🔎 Input")
        tbl.add_column("🔍 Status")
        tbl.add_column("✅ Expected")
        tbl.add_column("❌ Got")
        tbl.add_column("⏱️ Time")
        tbl.add_column("📤 StdOut")

        rows = self._get_detailed_rows(results)
        for r in rows:
            emoji = "🎉" if r["status"] else "💥"
            status_text = "[green]PASS[/green]" if r["status"] else "[red]FAIL[/red]"
            tbl.add_row(
                emoji + str(r["idx"]),
                str(r["input"]),
                status_text,
                r["exp"],
                r["got"],
                f"{r['time']:.2f} ms",
                r["out"],
            )

        console.print(Panel(tbl, title="🔬 Detailed Results", box=box.ROUNDED))

    def _get_detailed_rows(self, results):
        total = len(results)
        if total <= 5 or all(r["status"] for r in results):
            return results[:MAX_TEST_DETAILS]  # Show up to MAX_TEST_DETAILS if all pass
        return [r for r in results if not r["status"]]
