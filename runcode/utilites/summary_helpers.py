import os
from typing import Any, Dict, Tuple

from rich.panel import Panel
from rich.table import Table

import inspect


def get_problem_details(problem_class: Any) -> Tuple[str, str, int, bool, bool]:
    """Extracts problem details."""
    title = getattr(problem_class, "title", "No title available")
    description = getattr(problem_class, "description", "No description available")
    test_cases = getattr(problem_class, "tests", None)
    user_solution = getattr(problem_class, "user_solution", None)
    reference_solution = getattr(problem_class, "reference_solution", None)

    # Verify if user_solution contains actual code
    user_solution_implemented = (
        user_solution is not None
        and len(inspect.getsource(user_solution)) > 0
        and "NotImplementedError" not in inspect.getsource(user_solution)
    )

    reference_solution_implemented = (
        reference_solution is not None
        and len(inspect.getsource(reference_solution)) > 0
        and "NotImplementedError" not in inspect.getsource(reference_solution)
    )

    return (
        title,
        description,
        len(test_cases),
        user_solution_implemented,
        reference_solution_implemented,
    )


def format_value(value: Any) -> str:
    """Formats boolean and null values for display."""
    if value is True:
        return "[green]✅ Yes[/green]"
    elif value is False:
        return "[red]❌ No[/red]"
    elif value is None:
        return "[gray]Null[/gray]"
    return str(value)


def get_additional_variables(problem_class: Any) -> Dict[str, Any]:
    """Retrieves additional variables from the problem class."""
    return {
        var.upper(): getattr(problem_class, var)
        for var in dir(problem_class)
        if not var.startswith("_")
        and var
        not in ["title", "description", "tests", "user_solution", "reference_solution"]
    }


def create_summary_panel(
    prob: str,
    title: str,
    description: str,
    test_case_count: int,
    user_solution_implemented: bool,
    reference_solution: bool,
    additional_vars: Dict[str, Any],
) -> Panel:
    """Creates a summary panel for a problem."""
    test_case_count_str = (
        f"[gray]{test_case_count}[/gray]"
        if test_case_count == 0
        else str(test_case_count)
    )

    summary_content = f"""
[bold cyan]TITLE:[/bold cyan] [bold]{title.upper()}[/bold]
📜 [bold]Description:[/bold]
{description}

[bold]Number of Test Cases:[/bold] {test_case_count_str}
[bold]User Solution Implemented:[/bold] {format_value(user_solution_implemented)}
[bold]Reference Solution Implemented:[/bold] {format_value(reference_solution)}
"""

    if additional_vars:
        summary_content += "\n[bold]Additional Variables:[/bold]\n"
        for var_name, var_value in additional_vars.items():
            summary_content += (
                f"[bold magenta]{var_name}:[/bold magenta] {format_value(var_value)}\n"
            )

    return Panel(
        summary_content.strip(), title=f"Summary for: {prob}", border_style="blue"
    )


def create_summary_table(
    total_problems: int = 0, total_test_cases: int = 0, total_solutions: int = 0
) -> Table:
    """Creates a table for displaying problem summaries with footers."""
    table = Table(
        title="Problem Summary",
        caption="Overview of problems",
        border_style="blue",
        footer_style="bold blue",
        show_footer=True,
    )
    table.add_column("Problem", style="cyan", no_wrap=True)
    table.add_column("Title", style="bold")
    table.add_column("Test Cases", style="bold")
    table.add_column("User Solution", style="bold")
    table.add_column("Reference Solution", style="bold")
    table.add_column("Status", style="bold")  # New column for status

    # Add footers for totals
    table.columns[0].footer = f"Total: {total_problems}"
    table.columns[2].footer = f"Total: {total_test_cases}"
    table.columns[3].footer = f"Solutions: {total_solutions}"
    table.columns[4].footer = f"Solutions: {total_solutions}"

    return table


def determine_status(user_solution: bool, reference_solution: bool) -> str:
    """
    Determines the status of a problem based on solution implementation.

    Args:
        user_solution (bool): Whether the user solution is implemented.
        reference_solution (bool): Whether the reference solution is implemented.

    Returns:
        str: Status with appropriate color and emoji.
    """
    if user_solution and reference_solution:
        return "[green]✅ Fully Implemented[/green]"
    elif user_solution or reference_solution:
        return "[yellow]⚠️ Partially Implemented[/yellow]"
    else:
        return "[red]❌ Not Implemented[/red]"


def update_totals_in_table(table: Table, new_problem: Any) -> None:
    """
    Updates the totals in the footer of a given table by adding values from a new problem.

    Args:
        table (Table): The table whose footer needs to be updated.
        new_problem (Any): A new problem class to add to the totals.
    """
    # Retrieve current footer values from the table
    current_total_problems = int(table.columns[0].footer.split(":")[1].strip())
    current_total_test_cases = int(table.columns[2].footer.split(":")[1].strip())
    current_total_solutions = int(table.columns[3].footer.split(":")[1].strip())
    current_total_reff_solutions = int(table.columns[4].footer.split(":")[1].strip())

    # Increment totals based on the new problem
    current_total_problems += 1
    test_cases = getattr(new_problem, "tests", [])
    current_total_test_cases += len(test_cases)

    user_solution = getattr(new_problem, "user_solution", None)
    if (
        user_solution is not None
        and inspect.getsource(user_solution)
        and "NotImplementedError" not in inspect.getsource(user_solution)
    ):
        current_total_solutions += 1

    reff_solution = getattr(new_problem, "reference_solution", None)
    if (
        reff_solution is not None
        and inspect.getsource(reff_solution)
        and "NotImplementedError" not in inspect.getsource(reff_solution)
    ):
        current_total_reff_solutions += 1

    # Update the table footers
    table.columns[0].footer = f"Total: {current_total_problems}"
    table.columns[2].footer = f"Total: {current_total_test_cases}"
    table.columns[3].footer = f"Solutions: {current_total_solutions}"
    table.columns[4].footer = f"Solutions: {current_total_reff_solutions}"


def get_class_file_name(problem_class: Any) -> str:
    """
    Retrieves the file name of the class.

    Args:
        problem_class (Any): The class to get the file name for.

    Returns:
        str: The file name of the class.
    """
    if inspect.isclass(problem_class):
        full_name = inspect.getfile(problem_class)
        return os.path.basename(full_name).split(".")[0]
    return "Unknown Problem"


def add_problem_row_in_summary_table(table: Table, problem_class: Any) -> None:
    """
    Updates the 'Status' column in the table for a given problem.

    Args:
        table (Table): The table to update.
        problem_class (Any): The problem class to determine the status for.
    """
    # Extract user and reference solution implementation status
    user_solution = getattr(problem_class, "user_solution", None)
    reference_solution = getattr(problem_class, "reference_solution", None)

    user_solution_implemented = (
        user_solution is not None
        and len(inspect.getsource(user_solution)) > 0
        and "NotImplementedError" not in inspect.getsource(user_solution)
    )

    reference_solution_implemented = (
        reference_solution is not None
        and len(inspect.getsource(reference_solution)) > 0
        and "NotImplementedError" not in inspect.getsource(reference_solution)
    )

    # Determine the status
    status = determine_status(user_solution_implemented, reference_solution_implemented)
    class_file_name = get_class_file_name(problem_class)
    # Add the status to the table
    table.add_row(
        class_file_name,
        getattr(problem_class, "title", "No Title Available"),
        str(len(getattr(problem_class, "tests", []))),
        format_value(user_solution_implemented),
        format_value(reference_solution_implemented),
        status,
    )

    update_totals_in_table(table, problem_class)
