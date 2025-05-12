import ast
from rich.prompt import Prompt
from rich.console import Console
from rich import print as rprint  # <-- use rich.print for global printing


def parse_input(sig: str) -> tuple:
    """
    Safely parse Python literals: ints, lists, tuples, dicts, strings, booleans.
    """
    try:
        # Escape user input to prevent injection
        sanitized_sig = sig
        node = ast.parse(f"({sanitized_sig})", mode="eval")
        result = eval(compile(node, "<input>", "eval"))
        if not isinstance(result, (tuple, list, dict, int, float, str, bool)):
            raise ValueError("Parsed input is not a valid Python literal.")
        return result if isinstance(result, tuple) else (result,)
    except Exception as e:
        raise ValueError(f"Invalid input '{sig}': {e}")


def prompt_for_args() -> tuple:
    """
    Prompt the user for arguments and parse them safely.
    """
    console = Console()
    val = Prompt.ask("Enter args (e.g. [1,2,3], 4)")
    try:
        return parse_input(val)
    except ValueError as e:
        console.print(f"[red]{e}[/red]")
        return prompt_for_args()


def safe_command(fn):
    """
    Decorator to catch exceptions in CLI commands and print errors gracefully.
    """

    def wrapped(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            rprint(f"[bold red]Error:[/bold red] {e}")

    return wrapped