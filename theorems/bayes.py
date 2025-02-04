import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def bayes_page():
    st.title("Bayes' Theorem - Understanding Conditional Probability")
    
    # Introduction
    st.write("### Introduction to Bayes' Theorem")
    st.write("Bayes' Theorem is a fundamental concept in probability theory that describes how we update our beliefs based on new evidence. It is widely used in **medical diagnosis, spam detection, risk assessment, and even AI applications.**")
    
    # Project Goal
    st.write("### Project Goal")
    st.write("The goal of this project is to allow users to explore Bayes' Theorem interactively by adjusting parameters like **prior probability, sensitivity, and specificity**, and visualizing how they impact the final probability of an event occurring.")
    
    # Real-World Applications
    st.write("### Real-World Applications")
    st.write("- **Medical Diagnosis:** Estimating the probability of a disease given a positive test result 🏥")
    st.write("- **Spam Detection:** Determining if an email is spam based on certain words 📧")
    st.write("- **Fraud Detection:** Identifying fraudulent transactions using probabilistic models 💳")
    st.write("- **AI & Machine Learning:** Used in Naïve Bayes classifiers for text classification 🤖")
    
    # Explanation of Key Terms
    st.write("### Understanding the Key Terms")
    st.write("- **Prior Probability (Prevalence):** The initial probability of an event before new data is considered. (e.g., the percentage of people in a population who have a disease)")
    st.write("- **Sensitivity (True Positive Rate):** The probability that the test correctly identifies a positive case (e.g., how often a medical test correctly detects a disease when it's present).")
    st.write("- **Specificity (True Negative Rate):** The probability that the test correctly identifies a negative case (e.g., how often a test correctly gives a negative result when no disease is present).")
    
    # Interactive Inputs
    st.write("### Interactive Bayes' Theorem Calculator")
    prior = st.slider("Select Prior Probability (Prevalence of Condition)", 0.001, 1.0, 0.01, 0.001)
    sensitivity = st.slider("Select Sensitivity (True Positive Rate)", 0.5, 1.0, 0.95, 0.01)
    specificity = st.slider("Select Specificity (True Negative Rate)", 0.5, 1.0, 0.95, 0.01)
    
    # Bayes' Theorem Calculation
    def bayes_theorem(prior, sensitivity, specificity):
        false_positive_rate = 1 - specificity
        numerator = sensitivity * prior
        denominator = (sensitivity * prior) + (false_positive_rate * (1 - prior))
        return numerator / denominator
    
    posterior = bayes_theorem(prior, sensitivity, specificity)
    st.write(f"### Probability of Having the Condition Given a Positive Test Result: {posterior:.4f}")
    
    # Visualization
    fig, ax = plt.subplots()
    x_labels = ["Prior Probability", "Posterior Probability"]
    y_values = [prior, posterior]
    ax.bar(x_labels, y_values, color=['blue', 'green'])
    ax.set_ylabel("Probability")
    ax.set_title("Impact of Bayes' Theorem on Probability Updates")
    st.pyplot(fig)
