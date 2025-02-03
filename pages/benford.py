import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Predefined datasets
preloaded_datasets = {
    "Credit Card Transactions": "data/credit_card_transactions.csv",
    "Invoices Dataset (Synthetic)": "data/invoices_synthetic.csv"
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
        return "ℹ️ This dataset is synthetic and does not follow Benford’s Law. If a real-world dataset showed this behavior, it could indicate fraud."
    elif dataset_name == "Credit Card Transactions":
        return "✅ This dataset is real financial data and aligns well with Benford’s Law. Some deviations exist, likely due to rounding or business practices."
    elif max_deviation > 0.05:
        return "⚠️ High Deviation Detected: Possible fraud risk!"
    elif max_deviation > 0.02:
        return "⚠️ Moderate Deviation: Further investigation recommended."
    else:
        return "✅ Low Deviation: Data follows Benford’s Law closely."

def run():
    st.title("Benford's Law - Financial Fraud Detection")
    
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
            
            # Display dataset source if predefined dataset is chosen
            if is_preloaded and dataset_name in dataset_sources:
                st.write(f"### Data Source: [{dataset_name}]({dataset_sources[dataset_name]})")
