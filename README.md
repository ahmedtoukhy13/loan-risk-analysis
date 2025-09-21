# 🏦 Loan Risk Analysis – Credit Classification & Dashboard

## 📌 Project Overview
This project analyzes banking loan data and classifies clients based on their credit scores using Python and Excel.  
It includes feature engineering, pivot table analysis, DAX metrics, and dashboard design for executive insights.

## 🛠️ Tools Used
- Excel – Dashboard design, DAX metrics, pivot tables  
- Power Query – Data cleaning and transformation  
- Python (pandas) – Credit score classification  
- Jupyter Notebook – Optional workflow documentation  
- GitHub – Project hosting and version control

## 🧠 Workflow Summary

### 1. Data Cleaning
- Removed duplicates and standardized columns using Power Query  
- Handled missing values in `Credit_Score` and `Monthly_Installment`

### 2. Credit Score Classification (Python)
```python
import pandas as pd

df = pd.read_excel("banking_data.xlsx")

def classify_credit(score):
    if score > 750:
        return "Satisfactory"
    elif score >= 600:
        return "High Risk"
    else:
        return "Unsatisfactory"

df["Risk_Category"] = df["Credit_Score"].apply(classify_credit)
df.to_excel("banking_data_with_risk.xlsx", index=False)

3. Pivot Table Analysis (Excel)
Loan Status × Loan Type

Loan Guarantee × Loan Status

Loan Status × Credit Score

Branch-wise loan distribution

Average Installment per Status

Total Loan Amount per Status

4. Dashboard Design
Title: Loan Portfolio Dashboard – Summary of Insights

Filters: Branch, Guarantee, Loan Type, Monthly Installment, Interest Rate

Charts:

Loan Type vs. Loan Status

Loan Status Distribution (Pie)

Guarantee Type vs. Loan Status

Average Loan Amount per Status

Loan Status vs. Credit Status

Average Monthly Installment per Status

KPIs: Total loan amount by status

📸 Dashboard Preview

📂 Files Included
Loan_Portfolio_Dashboard_Final.xlsx – Final dashboard

credit_classification.py – Python script for credit scoring

loan_dashboard_final.ipynb – Optional notebook version

loan_dashboard_final.png – Dashboard screenshot

👨‍💻 Author
Ahmed Samir Toukhy Data Analyst | Excel & Python Specialist | Banking & E-commerce Insights Cairo, Egypt
