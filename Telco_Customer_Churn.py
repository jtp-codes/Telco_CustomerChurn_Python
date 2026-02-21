import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("data frame")
df = pd.read_csv("D:/git projects/WA_Fn-UseC_-Telco-Customer-Churn.csv")
print(df.head(100))

# Replace blanks in TotalCharges and convert to float
df["TotalCharges"] = df["TotalCharges"].replace(" ", "0")
df["TotalCharges"] = df["TotalCharges"].astype(float)

# Basic data checks
print(df.info())
print(df.isnull().sum())
print("Total null values:", df.isnull().sum().sum())
print(df.describe())
print("Duplicate rows:", df.duplicated().sum())
print("Duplicate customerIDs:", df["customerID"].duplicated().sum())

# Convert SeniorCitizen from 0/1 to Yes/No
def conv(value):
    return "Yes" if value == 1 else "No"

df['SeniorCitizen'] = df['SeniorCitizen'].apply(conv)
print(df.head(30))

# Count of customers by churn
ax = sns.countplot(x='Churn', data=df)
ax.bar_label(ax.containers[0])
plt.title("Count of Customers by Churn")
plt.show()

# Pie chart of churn percentage
plt.figure(figsize=(4, 4))
gb = df.groupby("Churn").size()
plt.pie(gb.values, labels=gb.index, autopct="%1.2f%%")
plt.title("Percentage of Churned Customers")
plt.show()

# Churn by gender
plt.figure(figsize=(4, 4))
sns.countplot(x="gender", data=df, hue="Churn")
plt.title("Churn by Gender")
plt.show()

# Count of customers by SeniorCitizen
plt.figure(figsize=(4, 4))
ax = sns.countplot(x="SeniorCitizen", data=df)
ax.bar_label(ax.containers[0])
plt.title("Count of Customers by Senior Citizen")
plt.show()

# Stacked bar chart: Churn by SeniorCitizen (percentage)
total_counts = (
    df.groupby('SeniorCitizen')['Churn']
    .value_counts(normalize=True)
    .unstack()
    * 100
)

fig, ax = plt.subplots(figsize=(6, 6))
total_counts.plot(kind='bar', stacked=True, ax=ax)

for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy()
    ax.text(x + width / 2, y + height / 2, f'{height:.1f}%', ha='center', va='center')

plt.title('Churn by Senior Citizen (Stacked Bar Chart)')
plt.xlabel('SeniorCitizen')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=0)
plt.legend(title='Churn', loc='upper right')
plt.show()

# Tenure distribution
plt.figure(figsize=(9, 4))
sns.histplot(x="tenure", data=df, bins=72)
plt.title("Tenure Distribution")
plt.show()

# Churn by contract type
plt.figure(figsize=(4, 4))
ax = sns.countplot(x="Contract", data=df, hue="Churn")
ax.bar_label(ax.containers[0])
plt.title("Count of Customers by Contract")
plt.show()

# Service-related columns
print(df.columns.values)

columns = [
    'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
    'OnlineBackup', 'DeviceProtection', 'TechSupport',
    'StreamingTV', 'StreamingMovies'
]

n_cols = 3
n_rows = (len(columns) + n_cols - 1) // n_cols

fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, n_rows * 4))
axes = axes.flatten()

for i, col in enumerate(columns):
    sns.countplot(x=col, data=df, hue="Churn", ax=axes[i])
    axes[i].set_title(f'Count Plot of {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Count')

for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()

# Churn by payment method
plt.figure(figsize=(8, 4))
ax = sns.countplot(x="PaymentMethod", data=df, hue="Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("Churned Customers by Payment Method")
plt.xticks(rotation=45)
plt.show()

# Monthly Charges vs Tenure with Regression line
plt.figure(figsize=(10, 6))
sns.lmplot(data=df, x='tenure', y='MonthlyCharges', hue='Churn', 
           markers=["o", "x"], palette="Set1", scatter_kws={'alpha':0.3})
plt.title("Relationship between Tenure and Monthly Charges by Churn")
plt.show()