import sqlite3

def init_db():
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symptoms TEXT,
        response TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_query(symptoms, response):
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO history (symptoms, response) VALUES (?, ?)",
        (symptoms, str(response))
    )

    conn.commit()
    conn.close()
