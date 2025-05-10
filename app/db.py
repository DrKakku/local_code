import sqlite3
from datetime import datetime

DB_PATH = 'submissions.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY,
            problem TEXT,
            status TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_submission(problem: str, status: str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    ts = datetime.now().isoformat()
    c.execute('INSERT INTO submissions (problem, status, timestamp) VALUES (?, ?, ?)',
              (problem, status, ts))
    conn.commit()
    conn.close()