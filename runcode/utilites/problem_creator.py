import os
from pathlib import Path
from typing import List, Dict, Any
from jinja2 import Template, TemplateError
from html import escape
from rich.console import Console
from rich.prompt import Prompt

console = Console()

# Directory containing templates
TEMPLATES_DIR: Path = Path(__file__).parent.parent / "templates"


def list_templates() -> List[str]:
    """List all available template files, excluding __init__.py."""
    try:
        templates = [
            p.name for p in TEMPLATES_DIR.glob("*.py") if p.name != "__init__.py"
        ]
        if not templates:
            console.print("[red]No templates found![/red]")
        return templates
    except Exception as e:
        console.print(f"[red]Error listing templates: {e}[/red]")
        return []


def sanitize_filename(filename: str) -> str:
    """Sanitize the filename to prevent directory traversal attacks."""
    return "".join(c for c in filename if c.isalnum() or c in ("_", "-"))


def get_multiline_input(prompt: str) -> str:
    """Prompt the user for multiline input."""
    try:
        console.print(prompt)
        lines: List[str] = []
        while True:
            line = Prompt.ask("")
            if not line:
                break
            lines.append(line)  # Escape user input
        return "\n".join(lines)
    except Exception as e:
        console.print(f"[red]Error getting input: {e}[/red]")
        return ""


def gather_test_cases() -> List[Dict[str, Any]]:
    """Gather test cases from the user."""
    try:
        cases: List[Dict[str, Any]] = []
        while (
            Prompt.ask("Add test case? (y/n)", choices=["y", "n"], default="y") == "y"
        ):
            inp = escape(
                Prompt.ask("Enter input tuple, e.g. ([1,2], 3)")
            )  # Escape input
            out = escape(
                Prompt.ask("Enter expected output (leave blank for ref)")
            )  # Escape output
            cases.append({"input": inp, "output": out or "None"})
        return cases
    except Exception as e:
        console.print(f"[red]Error gathering test cases: {e}[/red]")
        return []


def render_template(template_path: Path, context: Dict[str, Any]) -> str:
    """Render a Jinja2 template with the given context."""
    try:
        if not template_path.exists():
            raise FileNotFoundError(f"Template file not found: {template_path}")
        template_text = template_path.read_text()
        template = Template(template_text, autoescape=True)  # Enable autoescaping
        return template.render(context)
    except FileNotFoundError as e:
        console.print(f"[red]{e}[/red]")
        return ""
    except TemplateError as e:
        console.print(f"[red]Template rendering error: {e}[/red]")
        return ""
    except Exception as e:
        console.print(f"[red]Unexpected error: {e}[/red]")
        return ""


def write_problem_file(destination: Path, content: str) -> None:
    """Write the rendered content to a problem file."""
    try:
        if destination.exists():
            console.print(f"[red]File exists: {destination}[/red]")
        else:
            destination.write_text(content)
            console.print(f"[green]Created: {destination}[/green]")
    except Exception as e:
        console.print(f"[red]Error writing file: {e}[/red]")


def main() -> None:
    """Main function to create a new problem file."""
    try:
        # Choose template
        templates = list_templates()
        if not templates:
            return

        console.print("Available templates:")
        for i, t in enumerate(templates, 1):
            console.print(f"  {i}. {t}")
        choice = Prompt.ask(f"Select a template [1-{len(templates)}]")
        if not choice.isdigit() or not (1 <= int(choice) <= len(templates)):
            console.print("[red]Invalid choice![/red]")
            return
        tpl_path = TEMPLATES_DIR / templates[int(choice) - 1]

        # Gather metadata
        name = sanitize_filename(Prompt.ask("Problem filename (without .py)"))
        if not name:
            console.print("[red]Filename cannot be empty![/red]")
            return
        title = Prompt.ask("Problem title")  # Escape title
        description = get_multiline_input(
            "Enter detailed description (end with blank line):"
        )

        # Gather test cases
        cases = gather_test_cases()

        # Render template
        context = {"title": title, "description": description, "cases": cases}
        rendered_content = render_template(tpl_path, context)
        if not rendered_content:
            return

        # Write to file
        dest = Path(__file__).parent.parent / f"problems/{name}.py"
        write_problem_file(dest, rendered_content)
    except Exception as e:
        console.print(f"[red]Unexpected error: {e}[/red]")


if __name__ == "__main__":
    main()
