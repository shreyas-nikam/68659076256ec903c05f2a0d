id: 68659076256ec903c05f2a0d_documentation
summary: Derivative Market Instruments Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# CDS Analyzer Codelab: Understanding Credit Default Swaps

This codelab will guide you through the functionalities of the CDS Analyzer application.  This application is designed to simulate and analyze credit default swaps (CDS), enabling you to understand their mechanics and risk profiles. You will learn how to manipulate key parameters, visualize payoffs, and explore the relationship between risk factors and outcomes in CDS contracts.  Understanding CDS is crucial for anyone involved in fixed-income investing, credit analysis, or risk management.

## Introduction to CDS and the CDS Analyzer
Duration: 00:05

This application provides a user-friendly interface to explore the world of Credit Default Swaps. CDS are a vital tool in modern finance, used to transfer and manage credit risk. This codelab will help you understand the core concepts and how they translate into practical applications.

**Key Concepts you'll explore:**

*   **Credit Default Swaps (CDS):** What they are and how they work as insurance against credit risk.
*   **Notional Amount:** The principal amount being protected by the CDS.
*   **Recovery Rate:** The percentage of the notional amount recovered in case of default.
*   **Premium Rate (CDS Spread):** The annual payment made by the buyer to the seller.
*   **Payoff Analysis:** Understanding the potential gains and losses for both the buyer and seller.
*   **Risk Sensitivity:** How CDS payoffs change with varying Recovery Rates.

<aside class="positive">
By the end of this codelab, you will have a solid understanding of CDS mechanics and the ability to use the CDS Analyzer to simulate various scenarios.
</aside>

## Setting Up the Application
Duration: 00:02

Before diving into the details, ensure you have the application code available. You will need Python and Streamlit installed. To run the application, navigate to the directory containing `app.py` in your terminal and execute the following command:

```console
streamlit run app.py
```

This will open the application in your web browser.

## Exploring the CDS Analyzer Interface
Duration: 00:03

The application has a simple, intuitive interface.  The sidebar provides the main navigation, allowing you to switch between different analysis modules.

*   **CDS Analysis:** This module allows you to input CDS parameters and view the expected payoffs for the buyer and seller.
*   **Risk Analysis:** This module allows you to analyze the sensitivity of CDS payoffs to changes in the recovery rate.
*   **CDS Diagram:** This module presents a visual representation of the CDS agreement.

The main area of the application displays the active module with interactive controls and visualizations.

## CDS Analysis Module: Payoff Simulation
Duration: 00:15

This is the core module for understanding CDS payoffs. It allows you to input various CDS parameters and see the resulting payoffs for the buyer and seller in different scenarios.

1.  **Navigate to the "CDS Analysis" page** using the sidebar.

2.  **Input Parameters:**

    *   **Notional Amount:** Enter the principal amount of the CDS contract. This represents the underlying debt being protected.
    *   **Premium Rate (decimal):** Enter the annual premium rate paid by the CDS buyer to the seller, expressed as a decimal (e.g., 0.01 for 1%).
    *   **Recovery Rate (decimal):**  Use the slider to adjust the expected recovery rate in case of a default. This is the percentage of the notional amount the bondholder expects to recover (e.g., 0.4 for 40%).
    *   **Probability of Default (decimal):** Use the slider to adjust the probability of default.

3.  **Observe the Results:**

    *   **Payoff Scenarios:** A table displays the expected payoffs for both the buyer and seller under the scenarios of "Default" and "No Default". The payoffs are calculated based on the formulas:
        *   $PremiumPayment = NotionalAmount \times PremiumRate$
        *   $Payoff_{Buyer} = NotionalAmount \times (1 - RecoveryRate) - PremiumPayment$
        *   $Payoff_{Seller} = -NotionalAmount \times (1 - RecoveryRate) + PremiumPayment$

    *   **Expected Payoffs under Different Scenarios:** A bar chart visualizes these payoffs, making it easy to compare the potential gains and losses.

**Experiment:**

*   Try changing the **Notional Amount** to see how it scales the payoffs.
*   Increase the **Premium Rate**.  How does this affect the buyer's and seller's payoffs?
*   Decrease the **Recovery Rate**.  How does this affect the buyer's and seller's payoffs in a default scenario?
*   Increase the **Probability of Default**. While the table values don't change directly with probability, it influences the expected value of the contract in the real world.

<aside class="positive">
This module helps you understand how the key parameters of a CDS interact and how they impact the potential gains and losses for both parties involved.
</aside>

## Risk Analysis Module: Sensitivity to Recovery Rate
Duration: 00:10

This module focuses on understanding the sensitivity of CDS payoffs to changes in the Recovery Rate. It helps you visualize how the payoffs for the CDS buyer and seller change as the recovery rate varies, allowing you to assess risk exposure.

1.  **Navigate to the "Risk Analysis" page** using the sidebar.

2.  **Input Parameters:**

    *   **Notional Amount:** Enter the principal amount of the CDS contract.
    *   **Premium Rate (decimal):** Enter the annual premium rate.
    *   **Probability of Default (decimal):** Enter the probability of default.

3.  **Observe the Results:**

    *   **CDS Payoff Sensitivity to Recovery Rate:** A line chart displays how the buyer's and seller's payoffs change across a range of Recovery Rates (from 0% to 100%).

**Experiment:**

*   Observe the intersection point of the Buyer Payoff and Seller Payoff lines.  What does this point represent?
*   Change the **Notional Amount**.  How does this affect the magnitude of the payoff changes?
*   Increase the **Premium Rate**.  How does this shift the lines on the chart?

<aside class="negative">
This module highlights the importance of Recovery Rate in CDS analysis. Understanding how payoffs are affected by different recovery rates is crucial for assessing the risk associated with CDS contracts.
</aside>

## CDS Diagram Module: Visualizing the Relationship
Duration: 00:05

This module provides a visual representation of the CDS agreement, illustrating the relationship between the lender, the CDS buyer, and the CDS seller.

1.  **Navigate to the "CDS Diagram" page** using the sidebar.

2.  **Observe the Diagram:**

    *   The diagram clearly shows the flow of payments and risk transfer between the three parties.
    *   The **Lender** faces the risk of default.
    *   The **CDS Buyer** pays a premium to the CDS seller to protect against the lender's default.
    *   The **CDS Seller** receives the premium and agrees to compensate the CDS buyer if the lender defaults.

**Understanding the Flow:**

The diagram illustrates the essence of a CDS as a form of insurance against credit risk.  The CDS Buyer is essentially hedging their investment against the possibility of the Lender defaulting.

<aside class="positive">
This visual representation reinforces your understanding of the contractual relationships in a CDS agreement.
</aside>

## Conclusion
Duration: 00:02

You have now successfully explored the CDS Analyzer application. You have learned how to:

*   Simulate CDS payoffs under different scenarios.
*   Analyze the sensitivity of CDS payoffs to changes in the Recovery Rate.
*   Visualize the relationships between the parties in a CDS agreement.

This codelab provides a solid foundation for understanding CDS and their role in modern finance. You can further enhance your knowledge by experimenting with different parameter combinations and analyzing real-world CDS data.
