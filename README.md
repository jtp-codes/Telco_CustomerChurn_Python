# 📊 Telco Customer Churn Analysis

---

**Telco Customer Churn Analysis** is a comprehensive data science project designed to identify the key factors that lead to customer "churn" (attrition) in a telecommunications company. By leveraging Python's powerful analytical stack, this project provides a deep dive into demographic trends, service usage, and financial risk profiles to help businesses improve retention strategies.

## ✅ Features

---

* **Data Preprocessing:** Automated handling of missing values and conversion of `TotalCharges` to numerical formats.
* **Statistical Analysis:** In-depth data validation checking for null values, duplicates, and unique identifiers.
* **Behavioral Insights:** Analysis of how `Contract` types and `PaymentMethods` influence loyalty.
* **Advanced Visualizations:** High-quality plots including Heatmaps, KDE Density plots, and Regression analysis using `Seaborn` and `Matplotlib`.

## 🚀 Installation

---

### 1. Clone the repository:

```bash
git clone https://github.com/jtp-codes/Telco_Customer_Churn-using-R-.git
cd Telco_Customer_Churn-using-R-

```

### 2. Install Python dependencies:

```bash
pip install pandas numpy matplotlib seaborn

```

## 📈 Key Insights

---

* **Financial Risk:** Customers with higher **Monthly Charges** show a significantly higher density of churn, particularly in the **$70–$100** range.
* **The "Danger Zone":** Bivariate Density analysis reveals that new customers (**0–12 months tenure**) with high monthly bills are the most likely to leave.
* **Contract Impact:** Month-to-month contracts carry the highest churn risk, while two-year contracts ensure the highest stability.
* **Senior Citizens:** This demographic shows a significantly higher churn rate compared to younger customers.

## 📂 Repository Structure

---

* `churn_analysis.py`: Main Python script containing data logic and visualization code.
* `WA_Fn-UseC_-Telco-Customer-Churn.csv`: The raw Telco customer dataset.
* `README.md`: Project documentation and insights.

## 🛠️ Requirements

---

* **Python 3.8+**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**

---

## 👥 Creators

---

* **ARJUN RAJ B**
* **TEJUS C**
* **JOEL TOM PHILIP**

---