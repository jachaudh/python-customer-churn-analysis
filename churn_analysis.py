import pandas as pd

data = pd.read_csv("customer_data.csv")

print("Customer Churn Analysis")
print("-----------------------")

total_customers = len(data)
churned_customers = len(data[data["Churn"] == "Yes"])

churn_rate = (churned_customers / total_customers) * 100

print(f"Total Customers: {total_customers}")
print(f"Churned Customers: {churned_customers}")
print(f"Churn Rate: {churn_rate:.2f}%")

avg_monthly_charges = data.groupby("Churn")["MonthlyCharges"].mean()

print("\nAverage Monthly Charges:")
print(avg_monthly_charges)

contract_analysis = data.groupby("ContractType")["CustomerID"].count()

print("\nContract Distribution:")
print(contract_analysis)
