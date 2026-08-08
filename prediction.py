import pandas as pd


def predict_monthly_spending(df):

    if df.empty:
        return None

    df = df.copy()

    # Convert date column to datetime
    df["date"] = pd.to_datetime(df["date"])

    # Get today's date
    today = pd.Timestamp.today()

    # Keep only expenses from the current month
    current_month = df[
        (df["date"].dt.year == today.year) &
        (df["date"].dt.month == today.month)
    ]

    # If there are no expenses this month
    if current_month.empty:
        return None

    # Total spending this month
    total_spending = current_month["amount"].sum()

    # Number of days passed in the current month
    days_passed = today.day

    # Average spending per day
    average_daily_spending = total_spending / days_passed

    # Number of days in the current month
    days_in_month = today.days_in_month

    # Projected spending for the full month
    predicted_monthly = (
        average_daily_spending * days_in_month
    )

    return predicted_monthly