import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pipeline/clean_transactions.csv")

st.title("💳 Banking Fraud Detection Dashboard")

# KPI Metrics
total_transactions = len(df)
fraud_transactions = len(df[df["fraud_flag"] == 1])
safe_transactions = len(df[df["fraud_flag"] == 0])

col1, col2, col3 = st.columns(3)

col1.metric("Total Transactions", total_transactions)
col2.metric("Fraud Transactions", fraud_transactions)
col3.metric("Safe Transactions", safe_transactions)

# Data Preview
st.subheader("Transaction Data Preview")
st.dataframe(df.head())

# Fraud Count Chart
st.subheader("Fraud vs Safe Transactions")

fraud_counts = df["fraud_flag"].value_counts()

fig, ax = plt.subplots()
ax.bar(["Safe", "Fraud"], fraud_counts.values)

st.pyplot(fig)

# Payment Type Analysis
st.subheader("Payment Type Distribution")

payment_counts = df["payment_type"].value_counts()

fig2, ax2 = plt.subplots()
ax2.bar(payment_counts.index, payment_counts.values)

plt.xticks(rotation=45)

st.pyplot(fig2)