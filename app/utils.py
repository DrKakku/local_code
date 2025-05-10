from runner import Runner
from rich.prompt import Prompt

def parse_input(sig: str):
    """
    Basic evaluator for Python literals.
    Users can input tuples, lists, ints, etc.
    """
    return eval(f"({sig})")