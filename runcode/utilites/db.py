import sqlite3
from datetime import datetime
from typing import List, Optional, Tuple, Any

DB_PATH: str = "submissions.db"


def init_db() -> None:
    """Initialize the database and create the submissions table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY,
            problem TEXT,
            case_idx INTEGER,
            status TEXT,
            duration REAL,
            expected TEXT,
            actual TEXT,
            solution TEXT,
            timestamp TEXT,
            UNIQUE(problem, case_idx, solution)
        )
    """)
    conn.commit()
    conn.close()


def log_submission(
    problem: str,
    case_idx: int,
    status: str,
    duration: float,
    expected: str,
    actual: str,
    solution: str,
) -> None:
    """
    Log a submission to the database.

    Args:
        problem: The name of the problem.
        case_idx: The index of the test case.
        status: The status of the submission (e.g., "correct" or "incorrect").
        duration: The time taken to execute the solution in milliseconds.
        expected: The expected output of the test case.
        actual: The actual output of the test case.
        solution: The solution code submitted by the user.
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    ts: str = datetime.now().isoformat()
    c.execute(
        """
        INSERT OR IGNORE INTO submissions 
        (problem, case_idx, status, duration, expected, actual, solution, timestamp) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (problem, case_idx, status, duration, expected, actual, solution, ts),
    )
    conn.commit()
    conn.close()


def fetch_history(
    problem: Optional[str] = None, entry_id: Optional[int] = None
) -> List[Tuple[Any, ...]]:
    """
    Fetch submission history from the database.

    Args:
        problem: The name of the problem to filter by (optional).
        entry_id: The ID of a specific submission to fetch (optional).

    Returns:
        A list of tuples representing the submission history.
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    if entry_id is not None:
        c.execute("SELECT * FROM submissions WHERE id = ?", (entry_id,))
    elif problem:
        c.execute(
            "SELECT * FROM submissions WHERE problem = ? ORDER BY timestamp DESC",
            (problem,),
        )
    else:
        c.execute("SELECT * FROM submissions ORDER BY timestamp DESC")
    rows: List[Tuple[Any, ...]] = c.fetchall()
    conn.close()
    return rows