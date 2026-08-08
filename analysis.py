import pandas as pd
import sqlite3

DATABASE_NAME = "expenses.db"


def load_expenses():

    connection = sqlite3.connect(DATABASE_NAME)

    df = pd.read_sql_query(
        "SELECT * FROM expenses",
        connection
    )

    connection.close()

    return df


def calculate_total(df):

    if df.empty:
        return 0

    return df["amount"].sum()


def highest_category(df):

    if df.empty:
        return "No data"

    category_totals = df.groupby("category")["amount"].sum()

    return category_totals.idxmax()


def category_summary(df):

    if df.empty:
        return pd.DataFrame()

    return (
        df.groupby("category")["amount"]
        .sum()
        .reset_index()
        .sort_values("amount", ascending=False)
    )
def daily_spending(df):

    if df.empty:
        return pd.DataFrame()

    df = df.copy()

    # Convert date to datetime
    df["date"] = pd.to_datetime(df["date"])

    # Calculate total spending for each day
    daily = (
        df.groupby("date")["amount"]
        .sum()
        .reset_index()
        .sort_values("date")
    )

    return daily
def monthly_category_summary(df):

    if df.empty:
        return pd.DataFrame()

    df = df.copy()

    df["date"] = pd.to_datetime(df["date"])

    today = pd.Timestamp.today()

    current_month = df[
        (df["date"].dt.year == today.year) &
        (df["date"].dt.month == today.month)
    ]

    if current_month.empty:
        return pd.DataFrame()

    summary = (
        current_month
        .groupby("category")["amount"]
        .sum()
        .reset_index()
        .sort_values("amount", ascending=False)
    )

    return summary