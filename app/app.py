import streamlit as st
import pandas as pd

st.title("Invisible Economy Tracker")

st.subheader("Student Hidden Spending Predictor")

cash_usage = st.selectbox(
    "How often do you use cash?",
    ["Rarely", "Sometimes", "Frequently"]
)

bill_splitting = st.selectbox(
    "Do you split bills with friends?",
    ["No", "Yes"]
)

forget_recording = st.selectbox(
    "Do you forget recording expenses?",
    ["Never", "Sometimes", "Often"]
)

expense_tracking = st.selectbox(
    "Do you track your expenses?",
    ["Never", "Sometimes", "Always"]
)

cash_map = {
    "Rarely": 1,
    "Sometimes": 2,
    "Frequently": 3
}

split_map = {
    "No": 0,
    "Yes": 1
}

forget_map = {
    "Never": 1,
    "Sometimes": 2,
    "Often": 3
}

tracking_map = {
    "Never": 1,
    "Sometimes": 2,
    "Always": 3
}

if st.button("Predict Hidden Spending"):

    cash_score = cash_map[cash_usage]
    split_score = split_map[bill_splitting]
    forget_score = forget_map[forget_recording]
    tracking_score = tracking_map[expense_tracking]

    hidden_spending_score = (
        0.35 * cash_score +
        0.25 * forget_score +
        0.20 * split_score +
        0.20 * (4 - tracking_score)
    )

    if hidden_spending_score >= 2.8:
        personality = "Impulse Buyer"

    elif hidden_spending_score >= 2.3:
        personality = "Cash Hoarder"

    elif hidden_spending_score >= 1.8:
        personality = "Social Splitter"

    else:
        personality = "Silent Spender"

    st.success(
        f"Predicted Hidden Spending Score: {hidden_spending_score:.2f}"
    )

    st.info(
        f"Spending Personality: {personality}"
    )