id: 68659076256ec903c05f2a0d_user_guide
summary: Derivative Market Instruments User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Credit Default Swap (CDS) Analyzer: A User Guide

This codelab provides a comprehensive guide to understanding and utilizing the Credit Default Swap (CDS) Analyzer application. This application is designed to help you grasp the fundamentals of CDS contracts, simulate credit events, and visualize the resulting payoffs. By stepping through the various features, you'll gain a clearer understanding of how CDS are used to manage credit risk. This application supports learning on credit derivatives as a class of derivative contracts between two parties, a credit protection buyer and a credit protection seller, in which the latter provides protection to the former against a specific credit loss.

## Introduction to the CDS Analyzer
Duration: 00:05

The CDS Analyzer is a Streamlit application designed to simulate and analyze Credit Default Swaps (CDS). It allows users to input various CDS parameters, such as notional amount, premium rate, and recovery rate, to calculate expected payoffs for both the buyer and seller under different scenarios.

This application highlights the importance of understanding:

*   **Credit Default Swaps (CDS):** Financial contracts that allow investors to offset their credit risk.
*   **Key Parameters:** Notional amount, premium rate, and recovery rate.
*   **Payoff Calculations:** How payoffs are determined for CDS buyers and sellers in default and non-default scenarios.

<aside class="positive">
The CDS Analyzer is a valuable tool for students, finance professionals, and anyone interested in learning about credit derivatives and risk management.
</aside>

## Navigating the Application
Duration: 00:02

The application has a sidebar that allows you to navigate between the different modules:

*   **CDS Analysis:** Analyze expected payoffs for the buyer and seller.
*   **Risk Analysis:** Explore the sensitivity of CDS payoffs to changes in the recovery rate.
*   **CDS Diagram:** Understand the relationship between the lender, the CDS buyer, and the CDS seller.

Select the desired module from the "Navigation" dropdown in the sidebar.

## CDS Analysis Module
Duration: 00:10

This module allows you to input CDS parameters and observe the expected payoffs for both the buyer and seller under different credit scenarios.

1.  **Input Parameters:**
    *   **Notional Amount:** Enter the notional amount of the CDS contract. This is the principal amount on which interest and payments are calculated.
    *   **Premium Rate (decimal):** Input the annual premium rate paid by the CDS buyer to the CDS seller.
    *   **Recovery Rate (decimal):** Use the slider to select the expected recovery rate in case of a credit event. This represents the percentage of the notional amount that is expected to be recovered.
    *   **Probability of Default (decimal):**  Use the slider to set the probability of default.

2.  **Payoff Scenarios:**
    A table displays the calculated payoffs for both the buyer and seller under "Default" and "No Default" scenarios, considering the probability of default.

3.  **Visualizations:**
    A bar chart visualizes the expected payoffs under different scenarios, allowing for easy comparison between buyer and seller payoffs.

4.  **Mathematical Formulas:**
    The module displays the mathematical formulas used for the payoff calculations:

    *   Premium Payment = Notional Amount × Premium Rate
    *   $Payoff_{Buyer} = NotionalAmount \times (1 - RecoveryRate) - PremiumPayment$
    *   $Payoff_{Seller} = -NotionalAmount \times (1 - RecoveryRate) + PremiumPayment$

<aside class="positive">
Experiment with different parameter values to see how they affect the payoffs for the CDS buyer and seller. This helps in understanding the sensitivity of CDS contracts to various market conditions.
</aside>

## Risk Analysis Module
Duration: 00:10

This module focuses on analyzing the sensitivity of CDS payoffs to changes in the Recovery Rate.

1.  **Input Parameters:**
    *   **Notional Amount:**  Enter the notional amount of the CDS contract.
    *   **Premium Rate (decimal):** Input the annual premium rate.
    *   **Probability of Default (decimal):** Input the probability of default.

2.  **Recovery Rate Range:**
    The application automatically calculates payoffs across a range of recovery rates from 0% to 100%.

3.  **Payoff Sensitivity Chart:**
    A line chart displays how the payoffs for the CDS buyer and seller change as the recovery rate varies.

4.  **Insights:**
    The application provides key insights on the chart, such as the inverse relationship between recovery rate and buyer payoff, and the direct relationship between recovery rate and seller payoff.

<aside class="negative">
Pay close attention to how the lines intersect on the chart. This indicates the recovery rate at which the payoffs for the buyer and seller are equal.
</aside>

## CDS Diagram Module
Duration: 00:05

This module provides a visual representation of the CDS agreement.

1.  **CDS Diagram:**
    An image displays the relationship between the Lender, CDS Buyer, and CDS Seller.

2.  **Explanation:**
    The application explains the role of each party in the CDS agreement:

    *   **Lender:** Provides a loan and faces default risk.
    *   **CDS Buyer:** Pays a premium to the seller to protect against the lender's default.
    *   **CDS Seller:** Receives the premium and agrees to compensate the buyer if the lender defaults.

<aside class="positive">
Understanding the CDS diagram helps visualize the flow of credit risk and payments in a CDS contract.
</aside>

## Conclusion
Duration: 00:03

By working through these modules, you should now have a better understanding of CDS contracts, how payoffs are calculated, and how various parameters influence risk and reward. The CDS Analyzer is a valuable tool for exploring these concepts in a dynamic and interactive environment.
