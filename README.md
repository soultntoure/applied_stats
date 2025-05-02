## **📌 Project Overview**

**Applied Theorems** is an interactive web application designed to **explore, exemplify, and visualize mathematical, statistical, and algorithmic theorems**. The project aims to bridge the gap between **theoretical concepts and real-world applications**, making complex ideas intuitive through **interactive simulations, real datasets, and insightful visualizations**.

I started with two foundational theorems:  
✅ **Benford’s Law** – Used for **fraud detection and anomaly analysis**.  
✅ **Bayes' Theorem** – Applied in **medical diagnosis, risk assessment, and probabilistic decision-making**.

This is just the beginning, we plan to expand the project with more theorems that have significant real-world implications! 🚀

---

## **📊 Theorems Implemented**

### **1️⃣ Benford’s Law – Detecting Anomalies & Fraud**

📌 **What is Benford’s Law?**  
Benford’s Law states that in many naturally occurring datasets, the **leading digits (1-9) do not appear equally** but follow a **logarithmic distribution**, where smaller digits (like 1, 2, and 3) occur more frequently than larger ones.

🔹 **Real-World Applications:**

- **Fraud Detection**: Used by auditors and forensic accountants to detect financial manipulation.
- **Election Data Validation**: Helps verify the legitimacy of reported election results.
- **Scientific Data & Social Media**: Found in population statistics, stock prices, and even TikTok likes!

🔹 **Features Implemented:**  
✅ **Upload Your Own Dataset** – Users can upload financial or transaction data for analysis.  
✅ **Preloaded Datasets** – Includes a **synthetic invoice dataset** and a **real-world credit card transaction dataset**.  
✅ **Interactive Data Visualization** – Side-by-side comparison of **expected vs observed first-digit distributions**.  
✅ **Dynamic Fraud Risk Assessment** – Classifies datasets into **low, moderate, or high risk** based on statistical deviation.

🔹 **Available Datasets:**  
📌 **Invoices Dataset (Synthetic)** – A dataset generated using the Python Faker library to simulate fake transactions. Since the data is artificial, it does **not** follow Benford’s Law—making it a **good example of anomalies in fraudulent data**.  
📌 **Credit Card Transactions Dataset** – A real-world dataset containing detailed records of credit card transactions, which largely follows Benford’s distribution with minor deviations due to business practices.

---

### **2️⃣ Bayes' Theorem – Probability & Decision Making**

📌 **What is Bayes’ Theorem?**  
Bayes’ Theorem is a fundamental principle in probability that **updates our belief about an event given new evidence**. It is widely used in:

- **Medical Diagnosis** 🏥 – Evaluating the probability of a disease given a positive test result.
- **Spam Detection** 📧 – Filtering emails based on word probabilities.
- **Fraud Detection** 💳 – Identifying suspicious transactions.
- **AI & Machine Learning** 🤖 – Used in Naïve Bayes classifiers.

🔹 **Features Implemented:**  
✅ **Bayes’ Theorem Formula Visualization** – Users can see and understand the formula:

P(D∣T)=P(T∣D)⋅P(D)P(T)P(D|T) = \frac{P(T|D) \cdot P(D)}{P(T)}P(D∣T)=P(T)P(T∣D)⋅P(D)​

✅ **Interactive Probability Calculator** – Users can adjust:

- **Prior Probability (Prevalence of Condition)**
- **Sensitivity (True Positive Rate)**
- **Specificity (True Negative Rate)**
- See how these factors influence the **posterior probability** dynamically.  
    ✅ **Fixed Y-Axis for Stability** – Probability results are visualized with a **fixed 0-1 scale** to ensure clarity.  
    ✅ **Dynamic Analysis & Interpretation** – The application **adjusts its interpretation** based on the computed probability:
- **Low probability** → False positives likely, further testing recommended.
- **Moderate probability** → Uncertainty remains, confirm with additional tests.
- **High probability** → Test results strongly suggest the presence of the condition.

---

## **🛠️ Technologies Used**

- **Python** 🐍 – Core programming language.
- **Streamlit** 🎨 – Web framework for interactive UI and visualization.
- **Pandas** 🏗️ – Data manipulation and analysis.
- **NumPy** 🔢 – Numerical computations.
- **Matplotlib** 📊 – Data visualization.
- **SciPy** 📉 – Statistical tests (Chi-Square for Benford’s Law).

---

## **🚀 How to Run the Project Locally**

### **1️⃣ Clone the Repository**


`git clone https://github.com/soultntoure/applied_theorems.git cd applied_theorems`

### **2️⃣ Install Dependencies**


`pip install -r requirements.txt`

### **3️⃣ Run the Streamlit App**


`streamlit run app.py`

This will start the app, and you can interact with it in your browser.

---

## **🌍 Deployment & Live Demo**

We deployed the application using **Streamlit Cloud**. You can access it here:

🔗 **Live Demo**: https://appliedtheorems.streamlit.app/

---

## **📌 Future Plans**

We plan to expand **Applied Theorems** with more mathematical and statistical models, including:

- **Law of Large Numbers** – Demonstrating how sample sizes affect probability estimates.
- **Markov Chains** – Simulating transitions in probabilistic systems.
- **Central Limit Theorem** – Visualizing how distributions become normal over repeated sampling.

---

## **💡 Contributors & Acknowledgments**

This project was developed as part of an **exploration into applied statistical methods**, with a focus on making complex theorems **practical and easy to understand**.

Special thanks to everyone who contributed insights, feedback, and dataset ideas! 😊

---

### **📌 Summary**

✅ **Benford’s Law for fraud detection & anomaly detection**  
✅ **Bayes' Theorem for medical & probabilistic decision-making**  
✅ **Interactive visualizations & real-world datasets**  
✅ **Expanding with more statistical theorems in the future**
