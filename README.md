
# CDS Analyzer - Derivative Market Instruments Lab

This Streamlit application allows users to explore and analyze Credit Default Swaps (CDS),
which are financial derivatives used to transfer credit risk.

## Features

- Input key parameters such as notional amount, premium rate, recovery rate, and probability of default.
- Calculate and visualize expected payoffs for both CDS buyer and seller.
- Sensitivity analysis of payoffs relative to recovery rate changes.
- Visual diagram explaining the relationship between the lender, CDS buyer, and CDS seller.

## How to run

1. Install dependencies:

2. Launch the app:

## Notes

- The formulas used are:
  
  $$\text{Premium Payment} = \text{Notional Amount} \times \text{Premium Rate}$$
  
  $$\text{Payoff}_{Buyer} = \text{Notional} \times (1 - \text{Recovery Rate}) - \text{Premium Payment}$$
  
  $$\text{Payoff}_{Seller} = -\text{Notional} \times (1 - \text{Recovery Rate}) + \text{Premium Payment}$$

Enjoy exploring credit derivatives!
