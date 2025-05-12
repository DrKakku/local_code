import importlib
import time
import io
from contextlib import redirect_stdout
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
import inspect
from db import log_submission

console = Console()

class Runner:
    def __init__(self, problem_name: str):
        module = importlib.import_module(f"problems.{problem_name}")
        self.Problem = module.Problem
        self.name = problem_name

    def run_tests(self, custom_tests=None):
        tests = custom_tests or self.Problem.tests
        results = [self._run_single(idx, test) for idx, test in enumerate(tests, 1)]
        self._print_summary(results)
        self._print_details(results)

    def _run_single(self, idx, test):
        args = test.get("input", ())
        expected = test.get("output")
        if expected is None:
            expected = self.Problem.reference_solution(*args)
        exp_str = str(expected)
        buf = io.StringIO()
        start = time.perf_counter()
        with redirect_stdout(buf):
            try:
                got_val = self.Problem.user_solution(*args)
                status = got_val == expected
            except Exception as e:
                got_val = f"Error: {e}"
                status = False
        duration = time.perf_counter() - start
        out_str = buf.getvalue().strip()
        log_submission(self.name, idx,
                       'correct' if status else 'incorrect',
                       duration, exp_str, str(got_val),
                       inspect.getsource(self.Problem.user_solution))
        return {"idx":idx, "input":args, "exp":exp_str,
                "got":str(got_val), "time":duration,
                "out":out_str, "status":status}

    def _print_summary(self, results):
        total = len(results)
        passed = sum(r["status"] for r in results)
        avg_time = sum(r["time"] for r in results) / total if total else 0
        tbl = Table(box=box.SIMPLE_HEAVY)
        for label, val in [("🎯 Total", total), ("✅ Passed", passed),
                           ("❌ Failed", total - passed), ("⏱️ Avg(s)", f"{avg_time:.4f}")]:
            tbl.add_column(label, justify="center")
        tbl.add_row(*(str(v) for v in [total, passed, total-passed, f"{avg_time:.4f}"]))
        console.print(Panel(tbl, title="🚀 Test Summary 🚀", box=box.ROUNDED))

    def _print_details(self, results):
        total = len(results)
        show_all = total <= 10
        tbl = Table(title="🧪 Test Details 🧪", box=box.ROUNDED)
        tbl.add_column("🔢 #")
        tbl.add_column("🔎 Input")
        tbl.add_column("🔍 Status")
        tbl.add_column("✅ Expected")
        tbl.add_column("❌ Got")
        tbl.add_column("⏱️ Time")
        tbl.add_column("📤 StdOut")
        rows = results if show_all else [r for r in results if not r["status"]]
        for r in rows:
            emoji = "🎉" if r["status"] else "💥"
            status_text = "[green]PASS[/green]" if r["status"] else "[red]FAIL[/red]"
            tbl.add_row(
                emoji + str(r["idx"]),
                str(r["input"]),
                status_text,
                r["exp"],
                r["got"],
                f"{r['time']:.4f}",
                r["out"]
            )
        console.print(Panel(tbl, title="🔬 Detailed Results", box=box.ROUNDED))
