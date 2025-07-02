
import streamlit as st
import pandas as pd
import plotly.express as px

def run_risk_analysis():
    st.header("CDS Risk Analysis")

    st.markdown("""
    This page allows you to analyze the sensitivity of CDS payoffs to changes in the Recovery Rate.
    By adjusting the Recovery Rate, you can visualize how the payoffs for the CDS buyer and seller are affected.
    This helps in understanding the risk exposure associated with CDS contracts under varying market conditions.
    """)

    # Input parameters
    notional_amount = st.number_input("Notional Amount", value=1_000_000, step=100_000, format="%d")
    premium_rate = st.number_input("Premium Rate (decimal)", value=0.01, step=0.001, format="%.3f")
    probability_of_default = st.number_input("Probability of Default (decimal)", value=0.05, step=0.01, format="%.3f")

    # Recovery Rate Range
    recovery_rates = [i/100 for i in range(0, 101, 5)] # Recovery rates from 0 to 100% in steps of 5%

    # Calculate Payoffs for each recovery rate
    buyer_payoffs = []
    seller_payoffs = []
    premium_payment = notional_amount * premium_rate # Calculate it only once
    for recovery_rate in recovery_rates:
        buyer_payoff = notional_amount * (1 - recovery_rate) - premium_payment
        seller_payoff = -notional_amount * (1 - recovery_rate) + premium_payment
        buyer_payoffs.append(buyer_payoff)
        seller_payoffs.append(seller_payoff)

    # Create DataFrame for plotting
    data = {
        "Recovery Rate": recovery_rates,
        "Buyer Payoff": buyer_payoffs,
        "Seller Payoff": seller_payoffs
    }
    df = pd.DataFrame(data)

    # Plot the data
    fig = px.line(
        df,
        x="Recovery Rate",
        y=["Buyer Payoff", "Seller Payoff"],
        title="CDS Payoff Sensitivity to Recovery Rate",
        labels={"value": "Payoff", "Recovery Rate": "Recovery Rate (decimal)"}
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    **Insights:**

    -   The chart illustrates how the payoffs for the CDS buyer and seller change as the recovery rate varies.
    -   A higher recovery rate reduces the payoff for the buyer and increases the payoff for the seller, as the loss due to default is smaller.
    -   This analysis helps in understanding the risk and potential rewards associated with CDS contracts under different economic scenarios.
    """)
