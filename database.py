import sqlite3

def init_db():
    conn = sqlite3.connect("resumes.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analysis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        skills TEXT,
        score REAL
    )
    """)

    conn.commit()
    conn.close()


def save_analysis(skills, score):

    conn = sqlite3.connect("resumes.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO analysis (skills, score) VALUES (?, ?)",
        (",".join(skills), score)
    )

    conn.commit()
    conn.close()