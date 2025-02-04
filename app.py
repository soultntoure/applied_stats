import streamlit as st
from theorems import benford, bayes  

# Sidebar Navigation
st.sidebar.title("Statistical Analysis App")
page = st.sidebar.radio("Choose Analysis:", ["Home", "Benford's Law", "Bayes' Theorem", "Future Theorems"])

# Routing to Different Pages
if page == "Home":
    st.title("Welcome to Applied Theorems")
    st.write("This project explores statistical theorems like **Benford's Law** and **Bayes' Theorem** to detect anomalies and analyze data.")
    st.write("Choose an analysis from the sidebar to get started! 📊")
elif page == "Benford's Law":
    benford.benford_page()
elif page == "Bayes' Theorem":
    bayes.bayes_page()
else:
    st.write("More theorems will be added in the future!")
