import ast
from rich.prompt import Prompt
from rich.console import Console


def parse_input(sig: str) -> tuple:
    """
    Safely parse Python literals: ints, lists, tuples, dicts, strings, booleans.
    """
    try:
        node = ast.parse(f"({sig})", mode="eval")
        result = eval(compile(node, "<input>", "eval"))
        return result if isinstance(result, tuple) else (result,)
    except Exception as e:
        raise ValueError(f"Invalid input '{sig}': {e}")


def prompt_for_args() -> tuple:
    console = Console()
    val = Prompt.ask("Enter args (e.g. [1,2,3], 4)")
    try:
        return parse_input(val)
    except ValueError as e:
        console.print(f"[red]{e}[/red]")
        return prompt_for_args()
