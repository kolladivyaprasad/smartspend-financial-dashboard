import sqlite3

DATABASE_NAME = "expenses.db"


def create_database():
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            amount REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_expense(date, category, description, amount):
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO expenses
        (date, category, description, amount)
        VALUES (?, ?, ?, ?)
    """, (date, category, description, amount))

    connection.commit()
    connection.close()


def get_expenses():
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM expenses
        ORDER BY date DESC
    """)

    expenses = cursor.fetchall()

    connection.close()

    return expenses