import ast
from typing import Any
from rich.prompt import Prompt
from runner import Runner


def parse_input(sig: str) -> tuple:
    """
    Safely parse a comma-separated list of Python literals.

    Examples:
      [1,2,3], 4       -> ([1,2,3], 4)
      "hello", True   -> ("hello", True)
      1,2,3,4          -> (1, 2, 3, 4)

    Supports numbers, strings, lists, dicts, booleans, None.
    """
    # wrap in parentheses to enforce tuple
    try:
        node = ast.parse(f"({sig})", mode="eval")
        result = eval(compile(node, "<input>", "eval"))
        if not isinstance(result, tuple):
            return (result,)
        return result
    except Exception as e:
        raise ValueError(f"Invalid input signature '{sig}': {e}")


def prompt_for_args() -> tuple:
    """Prompt user to enter args until they type 'done'."""
    console_args = []
    console_args.append(Prompt.ask("Enter comma-separated args (e.g. [1,2,3], 4)"))
    try:
        return parse_input(console_args[0])
    except ValueError as e:
        print(e)
        return prompt_for_args()
