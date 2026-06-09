# 🏦 Banking Fraud Detection System

## 📌 Overview

The Banking Fraud Detection System is a Data Analytics project designed to identify suspicious banking transactions using Python, SQL, and Streamlit. The project generates transaction data, cleans and processes it, analyzes fraud patterns, and presents insights through an interactive dashboard.

---

## 🚀 Features

* Generate synthetic banking transaction data using Python
* Clean and preprocess transaction records
* Analyze fraud patterns using SQL queries
* Visualize insights using an interactive Streamlit dashboard
* Detect fraudulent and safe transactions
* Track payment type distribution
* Manage source code using Git and GitHub

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* SQL
* Streamlit
* Matplotlib
* Git & GitHub

---

## 📂 Project Structure

```text
banking-fraud-detection/
│
├── data_generator/
│   └── fake_transactions.py
│
├── pipeline/
│   ├── raw_transactions.csv
│   └── clean_transactions.py
│
├── analytics/
│   └── fraud_queries.sql
│
├── dashboard/
│   └── dashboard.py
│
└── README.md
```

---

## 📊 Dashboard Insights

* Total Transactions Analyzed: 1000
* Fraud Transactions Detected: 57
* Safe Transactions: 943
* Multiple payment methods analyzed:

  * UPI
  * Credit Card
  * Debit Card
  * Net Banking

---

## 📈 Key Analysis

### Fraud vs Safe Transactions

The dashboard compares fraudulent and legitimate transactions, helping identify risk levels in the banking system.

### Payment Type Distribution

Transaction volume is analyzed across various payment methods to understand usage patterns.

### Transaction Preview

Users can view processed transaction records including:

* Transaction ID
* Timestamp
* Location
* Amount
* Payment Type
* Fraud Flag

---

## ▶️ How to Run

### Generate Transaction Data

```bash
python3 data_generator/fake_transactions.py
```

### Clean Transaction Data

```bash
python3 pipeline/clean_transactions.py
```

### Launch Dashboard

```bash
streamlit run dashboard/dashboard.py
```

---

## 🎯 Business Impact

This project helps financial institutions monitor suspicious activities, visualize fraud trends, and improve decision-making through data-driven insights.

---

## 👩‍💻 Author

Akansha Pandey

Data Analytics Project
