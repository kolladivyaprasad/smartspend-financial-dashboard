def generate_insights(df, predicted_monthly):

    insights = []

    if df.empty:
        return insights

    # Total spending
    total_spending = df["amount"].sum()

    # Find spending by category
    category_spending = (
        df.groupby("category")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    # Highest spending category
    highest_category = category_spending.index[0]
    highest_amount = category_spending.iloc[0]

    # Percentage of total spending
    highest_percentage = (
        highest_amount / total_spending
    ) * 100

    # Insight 1
    insights.append(
        f"Your highest spending category is "
        f"{highest_category}, accounting for "
        f"{highest_percentage:.1f}% of your total spending."
    )

    # Insight 2
    if highest_percentage > 40:

        insights.append(
            f"More than 40% of your spending is going "
            f"towards {highest_category}. Consider setting "
            f"a budget for this category."
        )

    elif highest_percentage > 25:

        insights.append(
            f"{highest_category} makes up a significant "
            f"part of your spending. Keep an eye on this category."
        )

    else:

        insights.append(
            f"Your spending is reasonably distributed "
            f"across categories."
        )

    # Insight 3
    if predicted_monthly is not None:

        insights.append(
            f"📈 Based on your current spending pattern, "
            f"your projected monthly spending is approximately "
            f"₹{predicted_monthly:,.0f}."
        )

    return insights