def calculate_financial_score(
    df,
    predicted_monthly,
    monthly_budget
):

    if df.empty or predicted_monthly is None:
        return None

    score = 100

    # Budget score
    if predicted_monthly > monthly_budget:

        over_percentage = (
            (predicted_monthly - monthly_budget)
            / monthly_budget
        ) * 100

        budget_score = max(
            50,
            100 - over_percentage
        )

    else:

        budget_score = 100

    # Spending concentration score
    category_totals = (
        df.groupby("category")["amount"]
        .sum()
    )

    total_spending = category_totals.sum()

    if total_spending > 0:

        highest_percentage = (
            category_totals.max()
            / total_spending
        ) * 100

        if highest_percentage > 50:

            concentration_score = 80

        elif highest_percentage > 40:

            concentration_score = 90

        else:

            concentration_score = 100

    else:

        concentration_score = 100

    # Final score
    score = (
        budget_score * 0.6
        + concentration_score * 0.4
    )

    return {
        "overall": round(score),
        "budget": round(budget_score),
        "concentration": concentration_score
    }