# Credit Default Swap (CDS) Analyzer: An Educational Streamlit Application

## Project Title and Description

This Streamlit application provides a comprehensive analysis of Credit Default Swaps (CDS), a crucial financial instrument for managing credit risk. It allows users to simulate credit events, analyze expected payoffs for both the buyer and seller of a CDS, and visualize the sensitivity of these payoffs to various parameters. This application is designed primarily for educational purposes, allowing users to gain a deeper understanding of CDS contracts, their underlying mechanisms, and their applications in the financial world.  The application provides both tabular and graphical representations of CDS scenarios.

## Features

*   **CDS Payoff Analysis:**  Input key CDS parameters (Notional Amount, Premium Rate, Recovery Rate, Probability of Default) and calculate the expected payoffs for both the CDS buyer and seller in different scenarios (default, no default).
*   **Risk Analysis (Sensitivity Analysis):** Explore how the CDS payoffs change in response to varying Recovery Rates, visualizing the sensitivity through interactive plots.
*   **Interactive Visualization:**  Utilize Plotly to create dynamic and informative charts that illustrate payoff scenarios and risk profiles.
*   **Educational Content:** Provides explanations of core CDS concepts, key formulas, and real-world applications.
*   **Visual Diagram:** Display a diagram illustrating the relationship between the lender, CDS buyer, and CDS seller.
*   **User-Friendly Interface:** Designed with Streamlit for an intuitive and accessible user experience.

## Getting Started

### Prerequisites

*   **Python 3.7+**:  Ensure you have Python 3.7 or a later version installed on your system.
*   **Pip**: Make sure you have pip installed (it usually comes with Python).

### Installation

1.  **Clone the Repository:**

    ```bash
    git clone <your_repository_url>  # Replace with the actual repository URL
    cd cds-analyzer
    ```

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    Create a `requirements.txt` file if it doesn't exist.  Populate it with the following:

    ```
    streamlit
    pandas
    plotly
    ```

## Usage

1.  **Run the Application:**

    ```bash
    streamlit run app.py
    ```

2.  **Access the Application:**

    Open your web browser and navigate to the URL displayed in the terminal (usually `http://localhost:8501`).

3.  **Navigate the Application:**

    *   Use the sidebar navigation to switch between the "CDS Analysis", "Risk Analysis", and "CDS Diagram" pages.
    *   On the "CDS Analysis" page:
        *   Enter the Notional Amount, Premium Rate, Recovery Rate, and Probability of Default using the input fields.
        *   Observe the calculated payoffs in the table and the corresponding bar chart.
    *   On the "Risk Analysis" page:
        *   Enter the Notional Amount, Premium Rate, and Probability of Default.
        *   View the line chart displaying the sensitivity of payoffs to changes in the Recovery Rate.
    *   On the "CDS Diagram" page:
        *   Review the diagram illustrating the relationship between the lender, CDS buyer, and CDS seller.

## Project Structure

```
cds-analyzer/
├── app.py                         # Main Streamlit application file
├── application_pages/
│   ├── cds_analysis.py          # Module for CDS payoff analysis
│   ├── risk_analysis.py         # Module for risk (sensitivity) analysis
│   └── cds_diagram.py           # Module for displaying the CDS diagram
├── requirements.txt               # List of Python dependencies
├── README.md                      # This file
└── .gitignore                     # Specifies intentionally untracked files that Git should ignore
```

## Technology Stack

*   **Streamlit:**  Python library for creating interactive web applications.
*   **Pandas:**  Data analysis and manipulation library.
*   **Plotly:**  Interactive charting library.

## Contributing

We welcome contributions to enhance this application! To contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Implement your changes.
4.  Test your changes thoroughly.
5.  Submit a pull request with a clear description of your changes.

Please adhere to the existing coding style and conventions.

## License

This project is licensed under the [MIT License](LICENSE) - see the `LICENSE` file for details. *(You should create an actual LICENSE file if you plan to release under MIT license. If you use a different license, specify it here and include the appropriate LICENSE file.)*

## Contact

QuantUniversity: [https://www.quantuniversity.com](https://www.quantuniversity.com)
