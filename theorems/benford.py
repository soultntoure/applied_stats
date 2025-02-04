import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# These are my avialable datasets
preloaded_datasets = {
    "Invoices Dataset (Synthetic)": "data/invoices_synthetic.csv",
    "Credit Card Transactions": "data/credit_card_transactions.csv"
}

dataset_sources = {
    "Credit Card Transactions": "https://www.kaggle.com/datasets/priyamchoksi/credit-card-transactions-dataset",
    "Invoices Dataset (Synthetic)": "https://www.kaggle.com/datasets/cankatsrc/invoices"
}

def first_digit_distribution(data):
    first_digits = data.astype(str).str[0].astype(int)
    return first_digits.value_counts(normalize=True).sort_index()

benford_expected = np.array([np.log10(1 + 1/d) for d in range(1, 10)])

def plot_benford_analysis(observed, dataset_name, is_preloaded):
    digits = np.arange(1, 10)
    fig, ax = plt.subplots(figsize=(8, 5))
    
    if is_preloaded:
        ax.bar(digits, observed, color='blue', alpha=0.7, label="Observed")
        ax.plot(digits, benford_expected, marker='o', linestyle='-', color='red', label="Expected")
    else:
        ax.bar(digits - 0.2, benford_expected, width=0.4, label="Benford's Law", alpha=0.7)
        ax.bar(digits + 0.2, observed, width=0.4, label=f"Observed Data: {dataset_name}", alpha=0.7)
    
    ax.set_xticks(digits)
    ax.set_xlabel("Leading Digit")
    ax.set_ylabel("Frequency")
    ax.set_title("Benford's Law Analysis")
    ax.legend()
    st.pyplot(fig)

def analyze_fraud_risk(observed, dataset_name):
    deviations = np.abs(observed - benford_expected)
    max_deviation = np.max(deviations)
    
    if dataset_name == "Invoices Dataset (Synthetic)":
        return "### Conclusion for the Invoice Dataset\n- The observed first digit distribution in the **Invoice Dataset** shows a uniform distribution across digits 1 to 9.\n- This significantly deviates from the expected distribution under **Benford’s Law**, where we typically expect smaller digits (e.g., 1, 2, 3) to occur more frequently.\n\n#### Implications:\n- **Potential Data Manipulation**: The uniform distribution might suggest fraud or manipulation, but in this case, it is due to the **randomness of the synthetic dataset**.\n- **Flat Distribution**: A flat first-digit distribution is rare in real-world financial data, reinforcing that this dataset is **artificially generated**.\n- If such a distribution appears in real-world financial data, it could be a strong indicator of fraud or manipulation."
    elif dataset_name == "Credit Card Transactions":
        return "### Observations:\n- The observed distribution of first digits shows a generally good alignment with Benford's Law, particularly for the lower digits (1, 2, 3, etc.).\n- While there is some minor deviation, especially with the first digit \"1\", the distribution closely resembles what we would expect from a naturally occurring financial dataset.\n\n### Implications:\n- The small deviations from Benford's Law are not necessarily indicative of fraud or manipulation but could be the result of specific **business practices or rounding conventions** in the dataset.\n- The dataset follows a legitimate pattern, with **no major signs of manipulation**."
    elif max_deviation > 0.05:
        return "⚠️ High Deviation Detected: Possible fraud risk!"
    elif max_deviation > 0.02:
        return "⚠️ Moderate Deviation: Further investigation recommended."
    else:
        return "✅ Low Deviation: Data follows Benford’s Law closely."

def benford_page():
    st.title("Fraud Detection using Benford's Law")
    
    # Introduction
    st.write("### Introduction to Benford's Law")
    st.image("images/intro_Benf.png", caption="Understanding Benford's Law", width=400)
    st.write("Benford’s Law states that in many naturally occurring datasets, the leading digits are not uniformly distributed but rather follow a logarithmic distribution. This principle is so stable that it has been used in **financial fraud detection, election data verification, and even social media analytics**—such as TikTok likes and population statistics.")
    st.write("It appears in **scientific data, demographic statistics, and stock market prices**, among others.")
    
    st.write("### Project Goal")
    st.write("The goal of this project is to analyze datasets and, using **Benford's Law**, detect anomalies and potential fraud. By applying this principle, we can flag **irregularities in financial records, election results, and other datasets where numerical integrity is crucial.**")
    
    st.write("### Conditions for a Dataset to be Usable by Benford’s Law")
    st.write("- The dataset should have numerical values that span multiple orders of magnitude.")
    st.write("- The numbers should not be artificially constrained (e.g., human-set thresholds).")
    st.write("- The dataset should contain a sufficiently large sample size for statistical validity.")
    st.write("- The numbers should represent naturally occurring values rather than assigned identifiers.")
    

    st.image("images/Benf_dist.png", caption="Expected Benford's Law Distribution", use_container_width=True)
    
    # Option to choose between available datasets and uploading
    st.subheader("Choose a Data Source")
    data_source = st.radio("Select an option:", ["Use Available Datasets", "Upload Your Own Dataset"])
    
    df, dataset_name, is_preloaded = None, None, False
    
    if data_source == "Use Available Datasets":
        dataset_choice = st.selectbox("Available Datasets", list(preloaded_datasets.keys()))
        df = pd.read_csv(preloaded_datasets[dataset_choice])
        dataset_name = dataset_choice
        is_preloaded = True
    else:
        uploaded_file = st.file_uploader("Upload a CSV file with financial transaction data", type=["csv"])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            dataset_name = uploaded_file.name
    
    if df is not None:
        if dataset_name == "Credit Card Transactions":
            st.write("ℹ️ This dataset contains detailed records of credit card transactions, including transaction amounts and timestamps.")
        elif dataset_name == "Invoices Dataset (Synthetic)":
            st.write("ℹ️ The Invoice Dataset provided is a mock dataset generated using the Python Faker library. All data is randomly generated and does not represent actual individuals or products.")
        st.write(f"### Preview of {dataset_name}:")
        st.write(df.head())
        
        column_name = st.selectbox(f"Select column for {dataset_name}", [None] + list(df.columns), key=dataset_name)
        
        if column_name and column_name != "None":
            data = df[column_name].dropna()
            observed_distribution = first_digit_distribution(data)
            plot_benford_analysis(observed_distribution, dataset_name, is_preloaded)
            
            # Generate and display fraud risk insights
            risk_message = analyze_fraud_risk(observed_distribution, dataset_name)
            st.write(f"### Fraud Risk Analysis for {dataset_name}:")
            st.write(risk_message)
