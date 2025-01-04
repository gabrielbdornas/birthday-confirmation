import sqlite3

def init_sqlite():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    # Ensure the table exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS confirmations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sponsor_name TEXT,
        companions TEXT,
        total INTEGER
    )
    """)
    conn.commit()
    return conn

def save_to_sqlite(st, sponsor_name, companions, total):

    conn = init_sqlite()

    try:
        cursor = conn.cursor()
        # Store names as a JSON-like string for simplicity
        companions_str = str(companions)
        cursor.execute(
            "INSERT INTO confirmations (sponsor_name, companions, total) VALUES (?, ?, ?)",
            (sponsor_name, companions_str, total)
        )
        conn.commit()
        return True
    except Exception as e:
        st.error(f"SQLite Error: {e}")
        return False
