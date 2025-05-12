import sqlite3
from datetime import datetime

DB_PATH = "submissions.db"


def init_db():
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
):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    ts = datetime.now().isoformat()
    c.execute(
        "INSERT OR IGNORE INTO submissions (problem, case_idx, status, duration, expected, actual, solution, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (problem, case_idx, status, duration, expected, actual, solution, ts),
    )
    conn.commit()
    conn.close()


def fetch_history(problem: str = None, entry_id: int = None):
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
    rows = c.fetchall()
    conn.close()
    return rows
