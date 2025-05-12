import os
from pathlib import Path
from jinja2 import Template
from rich.console import Console
from rich.prompt import Prompt

console = Console()

# Directory containing templates
TEMPLATES_DIR = Path(__file__).parent / "templates"


def list_templates():
    return [p.name for p in TEMPLATES_DIR.glob("*.py")]


def get_multiline(prompt: str) -> str:
    console.print(prompt)
    lines = []
    while True:
        line = Prompt.ask("")
        if not line:
            break
        lines.append(line)
    return "\n".join(lines)


def main():
    # Choose template
    templates = list_templates()
    console.print("Available templates:")
    for i, t in enumerate(templates, 1):
        console.print(f"  {i}. {t}")
    choice = int(Prompt.ask(f"Select a template [1-{len(templates)}]")) - 1
    tpl_path = TEMPLATES_DIR / templates[choice]
    tpl_text = tpl_path.read_text()

    # Gather metadata
    name = Prompt.ask("Problem filename (without .py)")
    title = Prompt.ask("Problem title")
    description = get_multiline("Enter detailed description (end with blank line):")

    # Gather test cases
    cases = []
    while Prompt.ask("Add test case? (y/n)", choices=["y", "n"], default="y") == "y":
        inp = Prompt.ask("Enter input tuple, e.g. ([1,2], 3)")
        out = Prompt.ask("Enter expected output (leave blank for ref)")
        cases.append({"input": inp, "output": out or "None"})

    # Render
    template = Template(tpl_text)
    rendered = template.render(title=title, description=description, cases=cases)

    # Write
    dest = Path(__file__).parent / f"problems/{name}.py"
    if dest.exists():
        console.print(f"[red]File exists: {dest}[/red]")
    else:
        dest.write_text(rendered)
        console.print(f"[green]Created: {dest}[/green]")


if __name__ == "__main__":
    main()
