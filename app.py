import streamlit as st
from pages import benford, bayes

# Sidebar Navigation
st.sidebar.title("Statistical Analysis App")
page = st.sidebar.radio("Choose Analysis:", ["Benford's Law", "Bayes' Theorem", "Future Theorems"])

# Routing to Different Theorems
if page == "Benford's Law":
    benford.run()
elif page == "Bayes' Theorem":
    bayes.run()
else:
    st.write("More theorems will be added in the future!")