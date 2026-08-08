import streamlit as st
import pandas as pd
from datetime import date
from prediction import predict_monthly_spending
from insights import generate_insights
from financial_score import calculate_financial_score
from database import create_database, add_expense
from analysis import (
    load_expenses,
    calculate_total,
    highest_category,
    category_summary,
    daily_spending,
    monthly_category_summary
)


# Create database
create_database()


# Page configuration
st.set_page_config(
    page_title="Smart Expense Advisor",
    page_icon="💰",
    layout="wide"
)


# Title
st.title(" Smart Expense & Financial Advisor")

st.write(
    "Track your expenses, understand your spending habits, "
    "and get smart financial insights."
)
df = load_expenses()
# Sidebar
st.sidebar.header("💰 Budget Settings")

category_budgets = {}

categories = sorted(
    df["category"].dropna().unique().tolist()
)

for category in categories:

    category_budgets[category] = st.sidebar.number_input(
        f"{category} Budget (₹)",
        min_value=0.0,
        value=2000.0,
        step=500.0,
        key=f"budget_{category}"
    )
st.sidebar.header("Add New Expense")
monthly_budget = st.sidebar.number_input(
    "Monthly Budget (₹)",
    min_value=0.0,
    value=15000.0,
    step=500.0
)

expense_date = st.sidebar.date_input(
    "Date",
    date.today()
)


category = st.sidebar.selectbox(
    "Category",
    [
        "Food",
        "Transport",
        "Shopping",
        "Entertainment",
        "Education",
        "Healthcare",
        "Bills",
        "Other"
    ]
)


description = st.sidebar.text_input(
    "Description"
)


amount = st.sidebar.number_input(
    "Amount (₹)",
    min_value=0.0,
    step=10.0
)


if st.sidebar.button("Add Expense"):

    if amount > 0:

        add_expense(
            str(expense_date),
            category,
            description,
            amount
        )

        st.sidebar.success("Expense added successfully!")

        st.rerun()

    else:

        st.sidebar.error("Please enter an amount greater than 0.")


# Load data
df = load_expenses()
daily = daily_spending(df)
monthly_summary = monthly_category_summary(df)
# Dashboard
st.header(" Expense Dashboard")


if df.empty:

    st.info(
        "No expenses yet. Add your first expense using the sidebar."
    )

else:

    total = calculate_total(df)

    highest = highest_category(df)

    predicted_monthly = predict_monthly_spending(df)
    insights = generate_insights(
        df,
        predicted_monthly
    )
    budget_difference = None
    if predicted_monthly is not None:
        budget_difference = predicted_monthly - monthly_budget
    financial_score = calculate_financial_score(
        df,
        predicted_monthly,
        monthly_budget
    )    
    st.subheader("❤️ Financial Health Score")
    st.subheader("🚨 Spending Alerts")
    if predicted_monthly is not None:
        if predicted_monthly > monthly_budget:
            st.error(
                f"⚠️ Warning! Your projected monthly spending "
                f"of ₹{predicted_monthly:,.2f} is above your "
                f"₹{monthly_budget:,.2f} budget."
            )
        elif predicted_monthly > monthly_budget * 0.8:
            st.warning(
                f"⚠️ You are approaching your monthly budget. "
                f"Projected spending: ₹{predicted_monthly:,.2f}"
            )
        else:
            st.success(
                f"✅ Your projected spending of "
                f"₹{predicted_monthly:,.2f} is comfortably "
                f"within your budget."
                )
    if financial_score is not None:
        overall_score = financial_score["overall"]
        budget_score = financial_score["budget"]
        concentration_score = financial_score["concentration"]
        st.metric(
            "❤️ Overall Score",
            f"{overall_score}/100"
        )
        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                "💰 Budget Management",
                f"{budget_score}/100"
            )
        with col2:
            st.metric(
                "📊 Spending Distribution",
                f"{concentration_score}/100"
            )
    else:
        st.info(
            "Add expenses across different dates to calculate "
            "your Financial Health Score."
        )
    # Metrics
    st.subheader("💰 Budget Overview")
    if budget_difference is not None:
        if budget_difference > 0:
            st.error(
                f"⚠️ You may exceed your monthly budget by "
                f"₹{budget_difference:,.0f}."
            )
        else:
            st.success(
                f"✅ You are currently projected to stay "
                f"₹{abs(budget_difference):,.0f} under your budget."
                )
    else:
        st.info(
            "Add expenses across at least two different dates "
            "to see your budget projection."
            )
    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            " Total Spending",
            f"₹{total:,.2f}"
        )


    with col2:

        st.metric(
            " Highest Spending Category",
            highest
        )
    with col3:
        if predicted_monthly is not None:
            st.metric(
                " Predicted Monthly Spending",
                f"₹{predicted_monthly:,.2f}"
            )
        else:
            st.metric(
                "📈 Predicted Monthly Spending",
                "Need more data"
            )
    


    st.subheader("📋 Your Expenses")
    filter_category = st.selectbox(
        "🔎 Filter by Category",
        ["All"] + sorted(df["category"].dropna().unique().tolist())
        )
    if filter_category == "All":
        filtered_df = df
    else:
        filtered_df = df[
            df["category"] == filter_category
        ]
    st.dataframe(
        filtered_df,
        use_container_width=True
    )
    st.download_button(
        label="📥 Download Expenses as CSV",
        data=filtered_df.to_csv(index=False),
        file_name="my_expenses.csv",
        mime="text/csv"
        )

    st.subheader(" Spending by Category")

    summary = category_summary(df)

    st.bar_chart(
        summary.set_index("category")
    )
    st.subheader("📈 Daily Spending Trend")
    if not daily.empty:
        st.line_chart(
            daily.set_index("date")["amount"]
        )
    else:
        st.info("Not enough expense data to show the spending trend.")
    st.subheader("📅 This Month's Spending")
    if not monthly_summary.empty:
        st.bar_chart(
            monthly_summary.set_index("category")
        )
    else:
        st.info(
            "No expenses recorded for the current month."
        )
    st.subheader(" Category Breakdown")

    st.dataframe(
        summary,
        use_container_width=True
    )
    st.subheader("💰 Category Budget Status")
    for category_name, budget in category_budgets.items():
        if budget > 0 and not df.empty:
            spent = df[
                df["category"] == category_name
            ]["amount"].sum()
            remaining = budget - spent
            if remaining < 0:
                st.error(
                    f"⚠️ {category_name}: "
                    f"You are ₹{abs(remaining):,.0f} over budget."
                    )
            else:
                st.success(
                    f"✅ {category_name}: "
                    f"₹{remaining:,.0f} remaining."
            )
    st.subheader("💡 Smart Financial Insights")
    for insight in insights:
        st.info(insight)