import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def bayes_page():
    st.title("Bayes' Theorem - Understanding Conditional Probability")
    
    # Introduction
    st.write("### Introduction to Bayes' Theorem")
    st.write("Bayes' Theorem is a fundamental concept in probability theory that describes how we update our beliefs based on new evidence. It is widely used in **medical diagnosis, spam detection, risk assessment, and even AI applications.**")
    
    # Display the formula for Bayes' Theorem
    st.latex(r"P(D|T) = \frac{P(T|D) \cdot P(D)}{P(T)}")
    
    st.write("Where:")
    st.write("- **P(D|T):** The posterior probability, which represents the probability of an event occurring given that certain evidence is observed.")
    st.write("- **P(T|D):** The sensitivity (true positive rate), which measures how accurately a test identifies positive cases when the condition is actually present.")
    st.write("- **P(D):** The prior probability, which represents the initial likelihood of the event before considering new evidence.")
    st.write("- **P(T):** The total probability of observing the evidence, accounting for both true and false positives.")
    
    st.write("For scenarios where the prior probability is very low (such as rare occurrences), sensitivity and specificity play a crucial role in determining the final probability.")
    
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
    st.write("- **Prior Probability (P(D)):** This represents the prevalence of the disease. For rare diseases, the prior probability is typically a small value (e.g., 1% or 0.01).")
    st.write("- **Sensitivity (P(T|D)):** Also known as the true positive rate, this is the probability that the test correctly identifies a positive case when the disease is actually present.")
    st.write("- **Specificity (P(T|¬D)):** The true negative rate, which measures how accurately the test identifies negative cases when the disease is not present.")
    st.write("- **Posterior Probability (P(D|T)):** The probability of having the disease given a positive test result, calculated using Bayes' Theorem.")
    
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
    st.write(f"### Probability of Having the Condition Given a Positive Test Result: {posterior * 100:.2f}%")
    
    # Visualization
    fig, ax = plt.subplots()
    x_labels = ["Prior Probability", "Posterior Probability"]
    y_values = [prior, posterior]
    ax.bar(x_labels, y_values, color=['blue', 'green'])
    ax.set_ylabel("Probability")
    ax.set_ylim(0, 1)  # Fixed scale between 0 and 1
    ax.set_title("Impact of Bayes' Theorem on Probability Updates")
    st.pyplot(fig)
    
    # Analysis of Results and Discussion
    st.write("### Analysis of Results and Discussion")
    
    if posterior < 0.2:
        st.write("The posterior probability is relatively low, indicating that even with a positive test result, the likelihood of having the disease remains low. This is often the case for rare diseases where the prior probability is small, and despite a good test, false positives are still more common than true positives.")
    elif posterior < 0.8:
        st.write("The posterior probability is moderate, suggesting that while the test result is informative, further confirmation may be needed. This is common for conditions with medium prevalence where test accuracy plays a significant role.")
    else:
        st.write("The posterior probability is high, suggesting that a positive test result strongly indicates the presence of the disease. In such cases, the prior probability is typically higher, and the test's accuracy helps reinforce the conclusion.")
    
    st.write("This analysis highlights the importance of considering prior probability, sensitivity, and specificity when interpreting test results. A positive test alone is not always definitive, and further diagnostic evaluation may be required.")
