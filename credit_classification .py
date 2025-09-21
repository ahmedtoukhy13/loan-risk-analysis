import pandas as pd

# Load the loan dataset
df = pd.read_excel("banking_data.xlsx")

# Define credit score classification function
def classify_credit(score):
    if score > 750:
        return "Satisfactory"
    elif score >= 600:
        return "High Risk"
    else:
        return "Unsatisfactory"

# Apply classification to each customer
df["Risk_Category"] = df["Credit_Score"].apply(classify_credit)

# Save the updated dataset to a new Excel file
df.to_excel("banking_data_with_risk.xlsx", index=False)
