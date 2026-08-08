# 💰 SmartSpend — Personal Expense & Financial Health Dashboard

## 📌 Project Overview

**SmartSpend** is a Python-based personal finance dashboard that helps users track their expenses, understand their spending habits, monitor their budget, and receive data-driven financial insights.

The application converts everyday expense data into useful visualizations, spending predictions, financial health scores, and budget alerts through an interactive web dashboard.

---

## 🎯 Problem Statement

Many people record expenses but do not properly analyze where their money is going.

SmartSpend addresses this problem by providing a simple application that allows users to:

* Track daily expenses
* Analyze spending by category
* Monitor their monthly budget
* Predict monthly spending
* Identify high-spending categories
* Receive personalized financial insights
* Monitor their overall financial health

---

## 🚀 Features

### 💸 Expense Management

* Add and store expenses
* Record expense date, category, description, and amount
* View complete expense history
* Filter expenses by category
* Download expense data as CSV

### 📊 Data Analysis

* Category-wise spending analysis
* Daily spending trends
* Monthly spending analysis
* Identification of highest spending categories

### 🔮 Spending Prediction

The application analyzes the user's current spending pattern and estimates their projected monthly spending.

### ❤️ Financial Health Score

SmartSpend calculates a financial health score out of 100 based on:

* Budget management
* Spending distribution

### 🚨 Spending Alerts

The application provides warnings when projected spending approaches or exceeds the user's monthly budget.

### 💡 Smart Financial Insights

The dashboard generates useful recommendations based on the user's spending behavior.

### 📈 Interactive Dashboard

All major results are presented through an interactive Streamlit web interface.

---

## 🛠️ Technologies Used

| Technology   | Purpose                        |
| ------------ | ------------------------------ |
| Python       | Main programming language      |
| Streamlit    | Interactive web dashboard      |
| Pandas       | Data manipulation and analysis |
| NumPy        | Numerical operations           |
| Matplotlib   | Data visualization             |
| Plotly       | Interactive visualization      |
| Scikit-learn | Machine learning / prediction  |
| SQLite       | Expense data storage           |
| CSV          | Data export                    |

---

## 🧠 Data Science Concepts Used

This project applies several important Data Science concepts:

### 1. Data Collection

Expense information is collected from the user through the application.

### 2. Data Storage

Expense records are stored in a database for future analysis.

### 3. Data Cleaning

The application processes and prepares expense data before performing analysis.

### 4. Exploratory Data Analysis

Spending patterns are analyzed using categories, dates, and amounts.

### 5. Data Visualization

Charts are used to make spending patterns easier to understand.

### 6. Predictive Analysis

Historical/current spending behavior is used to estimate projected monthly spending.

### 7. Rule-Based Insights

The application generates financial recommendations based on spending patterns and budget conditions.

---

## 🏗️ Project Structure

```text
Project(1)
│
├── app.py
├── analysis.py
├── database.py
├── prediction.py
├── insights.py
├── financial_score.py
├── expenses.db
├── README.md
└── venv/
```

### File Description

**app.py**
Main Streamlit application and dashboard.

**database.py**
Handles expense database operations.

**analysis.py**
Performs expense analysis and generates spending summaries.

**prediction.py**
Handles monthly spending prediction.

**insights.py**
Generates financial insights based on spending patterns.

**financial_score.py**
Calculates the user's Financial Health Score.

**expenses.db**
SQLite database containing expense records.

---

## ⚙️ How to Run the Project

### 1. Clone or download the project

Open the project folder in VS Code.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```bash
venv\Scripts\activate
```

If PowerShell blocks the activation script, use:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Then activate again:

```bash
venv\Scripts\activate
```

### 4. Install the required libraries

```bash
pip install streamlit pandas numpy matplotlib plotly scikit-learn
```

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser through a local Streamlit address.

---

## 📊 Application Workflow

```text
User enters expense
        ↓
Expense stored in SQLite
        ↓
Data loaded using Pandas
        ↓
Expense analysis
        ↓
Category & daily spending analysis
        ↓
Monthly spending prediction
        ↓
Financial Health Score
        ↓
Budget & spending alerts
        ↓
Smart financial insights
        ↓
Interactive Streamlit dashboard
```

---

## 🔮 Future Scope

The project can be extended with:

* User authentication
* Cloud database
* Mobile application
* Automatic bank transaction import
* Advanced machine learning models
* Personalized saving recommendations
* Expense anomaly detection
* Email/SMS spending alerts
* Multiple currency support
* Long-term financial goal tracking

---

## 🎓 Project Objective

The main objective of SmartSpend is to demonstrate how **Python, Data Science, data analysis, visualization, and predictive techniques** can be combined to create a practical real-world application.

---

## 👨‍💻 Author

**K Divya**

Data Science Engineering Student

---

## ⭐ Project

**SmartSpend — Personal Expense & Financial Health Dashboard**

Built using Python and Streamlit.
