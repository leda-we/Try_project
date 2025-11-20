import sqlite3
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER,
    name TEXT,
    age TEXT,
    city TEXT
)
""")

conn.commit()

def add_user(telegram_id, name, age, city):
    cursor.execute("""
    INSERT INTO users (telegram_id, name, age, city)
    VALUES (?, ?, ?, ?)
    """, (telegram_id, name, age, city))
    conn.commit()

def get_all_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()