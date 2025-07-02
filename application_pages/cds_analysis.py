
import streamlit as st
import pandas as pd
import plotly.express as px

def run_cds_analysis():
    st.header("Credit Default Swap (CDS) Payoff Analysis")

    st.markdown(""" 
    In this module, you can input parameters related to a credit default swap (CDS) and observe the expected payoffs for both the buyer and seller under different credit scenarios.
    
    The formulas used are:
    

    $$\text{Premium Payment} = \text{Notional Amount} \times \text{Premium Rate}$$
    

    $$\text{Payoff (Buyer)} = \text{Notional} \times (1 - \text{Recovery Rate}) - \text{Premium Payment}$$
    

    $$\text{Payoff (Seller)} = -\text{Notional} \times (1 - \text{Recovery Rate}) + \text{Premium Payment}$$
    

    Adjust the inputs to see how the payoffs change with different credit risk parameters.
    """)

    # Input parameters
    notional_amount = st.number_input("Notional Amount", value=1_000_000, step=100_000, format="%d")
    premium_rate = st.number_input("Premium Rate (decimal)", value=0.01, step=0.001, format="%.3f")
    recovery_rate = st.slider("Recovery Rate (decimal)", min_value=0.0, max_value=1.0, value=0.4, step=0.05)
    probability_of_default = st.slider("Probability of Default (decimal)", min_value=0.0, max_value=1.0, value=0.05, step=0.01)

    # Calculations
    premium_payment = notional_amount * premium_rate
    # Calculate expected payoffs under default scenario
    buyer_payoff = notional_amount * (1 - recovery_rate) - premium_payment
    seller_payoff = -notional_amount * (1 - recovery_rate) + premium_payment

    # Create a DataFrame for display
    data = {
        "Scenario": ["Default", "No Default"],
        "Probability": [probability_of_default, 1 - probability_of_default],
        "Buyer Payoff": [buyer_payoff, 0],
        "Seller Payoff": [seller_payoff, 0]
    }

    df = pd.DataFrame(data)

    st.subheader("Payoff Scenarios")
    st.dataframe(df)

    # Plotting
    fig = px.bar(
        df,
        x="Scenario",
        y=["Buyer Payoff", "Seller Payoff"],
        title="Expected Payoffs under Different Scenarios",
        barmode="group"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Display formulas
    st.markdown("### Mathematical Formulas")
    st.latex(r"Premium\,Payment = Notional 	imes Premium\,Rate")
    st.latex(r"Payoff_{Buyer} = Notional 	imes (1 - Recovery\,Rate) - Premium\,Payment")
    st.latex(r"Payoff_{Seller} = -Notional 	imes (1 - Recovery\,Rate) + Premium\,Payment")
