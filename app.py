
import streamlit as st

st.set_page_config(page_title="CDS Analyzer", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("Credit Default Swap (CDS) Analyzer")
st.divider()

st.markdown("""
This application is designed to analyze credit default swaps (CDS) by allowing users to simulate credit events and visualize the resulting payoffs. The application takes key CDS parameters as input, calculates expected payoffs, and presents this information in both tabular and graphical formats. This application supports learning on credit derivatives as a class of derivative contracts between two parties, a credit protection buyer and a credit protection seller, in which the latter provides protection to the former against a specific credit loss.

**Core Concepts:**

-   **Credit Default Swap (CDS):** A financial derivative contract that allows an investor to "swap" or offset their credit risk with that of another investor. It essentially acts as insurance for bondholders, where the CDS seller agrees to compensate the buyer if the bond issuer defaults.

**Key Formulae:**

-   **Expected Payoff for CDS Buyer (Default)**:
    
    $Payoff_{Buyer} = NotionalAmount \times (1 - RecoveryRate) - PremiumPayment$
    

-   **Expected Payoff for CDS Seller (Default)**:
    
    $Payoff_{Seller} = -NotionalAmount \times (1 - RecoveryRate) + PremiumPayment$
    

-   **Premium Payment**:
    
    $PremiumPayment = NotionalAmount \times PremiumRate$
    

Where:

-   $NotionalAmount$: The notional amount of the CDS contract.
-   $RecoveryRate$: The expected recovery rate in case of a credit event (expressed as a decimal).
-   $PremiumRate$: The annual premium rate paid by the CDS buyer to the CDS seller (expressed as a decimal).
-   $PremiumPayment$: The periodic payment made by the CDS buyer to the seller.

**Explanations:**

-   **Notional Amount**: This is the principal amount of the underlying debt that the CDS is protecting. It's the base amount used to calculate payoffs and premium payments. *Example:* If a CDS has a \$1,000,000 notional amount, this is the reference amount used in calculations.
-   **Recovery Rate**: In the event of a default, the *Recovery Rate* is the percentage of the notional amount that the bondholder expects to recover. This value is typically between 0 and 100 percent. *Example:* If the recovery rate is 40% (or 0.4), it means the bondholder expects to recover 40% of the notional amount if the issuer defaults.
-   **Premium Rate**: The *Premium Rate* (also known as the CDS spread) is the annual payment made by the buyer to the seller, expressed as a percentage of the notional amount. *Example*: A premium rate of 1% on a \$1,000,000 notional amount would result in an annual premium payment of \$10,000. The Premium payment is often divided into quarterly payments.
-   **Expected Payoff**:  Expected Payoff shows what the parties can expect to receive based on the probability of default.

**Real-World Applications:**

CDS are used extensively in credit risk management by banks, hedge funds, and other financial institutions. They can be used to hedge credit risk, speculate on creditworthiness, or create synthetic credit exposures.  Understanding CDS payoffs is crucial for anyone involved in fixed-income investing or credit analysis.
""")

page = st.sidebar.selectbox(label="Navigation", options=["CDS Analysis", "Risk Analysis", "CDS Diagram"])

if page == "CDS Analysis":
    from application_pages.cds_analysis import run_cds_analysis
    run_cds_analysis()
elif page == "Risk Analysis":
    from application_pages.risk_analysis import run_risk_analysis
    run_risk_analysis()
elif page == "CDS Diagram":
    from application_pages.cds_diagram import run_cds_diagram
    run_cds_diagram()

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
