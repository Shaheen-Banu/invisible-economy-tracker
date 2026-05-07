import pandas as pd


def clean_columns(df):

    df.columns = [
        col.strip().lower().replace(" ", "_")
        for col in df.columns
    ]

    return df


def calculate_hidden_spending(
    cash_score,
    forget_score,
    split_score,
    tracking_score
):

    score = (
        0.35 * cash_score +
        0.25 * forget_score +
        0.20 * split_score +
        0.20 * (4 - tracking_score)
    )

    return round(score, 2)


def classify_personality(score):

    if score >= 2.8:
        return "Impulse Buyer"

    elif score >= 2.3:
        return "Cash Hoarder"

    elif score >= 1.8:
        return "Social Splitter"

    else:
        return "Silent Spender"