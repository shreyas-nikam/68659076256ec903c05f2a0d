
import streamlit as st

def run_cds_diagram():
    st.header("Credit Default Swap (CDS) Diagram")

    st.markdown("""
    This page provides a visual representation of the relationship between the lender, the CDS buyer, and the CDS seller in a Credit Default Swap (CDS) agreement.
    Understanding this relationship is crucial for grasping the concept of credit risk transfer in CDS contracts.
    """)

    # Display the CDS diagram
    st.image("https://www.investopedia.com/thmb/CD4j0C9NFbI_EdJEqg4BfB-bHBo=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/cds_diagram_updated-5c579220c9e77c00016368d3.png",
              caption="CDS Diagram: Lender, CDS Buyer, and CDS Seller",
              use_column_width=True)

    st.markdown("""
    **Explanation:**

    -   The **Lender** provides a loan to a borrower and faces the risk of default.
    -   The **CDS Buyer** pays a premium to the CDS seller to protect against the lender's default.
    -   The **CDS Seller** receives the premium and agrees to compensate the CDS buyer if the lender defaults.
    """)
