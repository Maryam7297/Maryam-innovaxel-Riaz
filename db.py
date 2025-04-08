import sqlite3

def get_db():
    conn = sqlite3.connect('urls.db')  # This creates a new SQLite database file named 'urls.db' 
    conn.row_factory = sqlite3.Row  # This allows access to rows by column name
    return conn

def create_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_url TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()
