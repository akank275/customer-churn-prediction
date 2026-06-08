# 📊 Customer Churn Prediction System

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to churn based on customer demographics, services, billing information, and contract details.

---

## 🚀 Project Overview

Customer churn is one of the biggest challenges faced by telecom companies. Retaining existing customers is significantly cheaper than acquiring new ones.

This project uses Machine Learning to:

- Identify customers likely to churn
- Analyze key churn drivers
- Generate business insights
- Provide real-time predictions through a Streamlit web application

---

## 🎯 Business Problem

Telecom companies lose revenue when customers leave their services.

The objective of this project is to:

- Predict customer churn
- Identify high-risk customers
- Support retention strategies
- Improve customer lifetime value

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Streamlit
- Joblib
- Git & GitHub

---

## 📂 Dataset

Dataset: IBM Telco Customer Churn Dataset

Features Include:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract Type
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

Target Variable:

- Churn (Yes / No)

---

## 🔄 Project Workflow

Data Collection
↓
Data Cleaning
↓
Data Preprocessing
↓
Exploratory Data Analysis (EDA)
↓
Feature Engineering
↓
Model Training
↓
Model Evaluation
↓
Model Comparison
↓
Streamlit Deployment

---

## 📈 Exploratory Data Analysis

### Correlation Heatmap

![Heatmap](screenshots/heatmap.png)

### Churn Distribution

(Add Screenshot Here)

---

## 🤖 Machine Learning Models

The following models were trained and compared:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

### Model Comparison

![Model Comparison](screenshots/model_comparison.png)

---

## 📊 Model Performance

### Best Model

Random Forest Classifier

### Accuracy

**79.56%**

### ROC Curve

![ROC Curve](screenshots/roc_curve.png)

### Confusion Matrix

(Add Screenshot Here)

---

## 🔥 Feature Importance

Top factors affecting customer churn:

- Contract Type
- Tenure
- Monthly Charges
- Total Charges
- Internet Service

### Feature Importance Chart

![Feature Importance](screenshots/feature_importance.png)

---

## 💡 Business Insights

### Key Findings

1. Customers with Month-to-Month contracts have the highest churn rate.

2. Customers with low tenure are more likely to churn.

3. High monthly charges increase churn probability.

4. Long-term contracts improve customer retention.

5. Customers with Tech Support services churn less frequently.

---

## 🖥️ Streamlit Application

### Application Home Page

![App Home](screenshots/app_home.png)

### Prediction Result

![Prediction Result](screenshots/prediction_result.png)

### Features

- Real-Time Churn Prediction
- Churn Probability Score
- Customer Risk Classification
- Interactive User Interface

---

## 📁 Project Structure

```text
customer-churn-prediction/

├── data/
│
├── notebooks/
│   └── churn_analysis.ipynb
│
├── models/
│   └── churn_model.pkl
│
├── screenshots/
│   ├── heatmap.png
│   ├── model_comparison.png
│   ├── roc_curve.png
│   ├── feature_importance.png
│   ├── app_home.png
│   └── prediction_result.png
│
├── app.py
├── requirements.txt
├── README.md
│
└── .gitignore
```

---

## ▶️ Installation

Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/customer-churn-prediction.git
```

Move into project directory

```bash
cd customer-churn-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit App

```bash
streamlit run app.py
```

---

## 🌐 Deployment

Streamlit Cloud Deployment:

Add your deployed Streamlit URL here.

Example:

https://your-app-name.streamlit.app

---

## 📌 Future Improvements

- XGBoost Implementation
- Hyperparameter Tuning
- SHAP Explainability
- Power BI Dashboard
- Customer Retention Recommendation Engine

---

## 👨‍💻 Author

Akanksha Kumari Sinha

Aspiring Data Analyst | Python | SQL | Power BI | Machine Learning

LinkedIn:
(Add LinkedIn URL)

GitHub:
(Add GitHub URL)

---

## ⭐ If you found this project useful

Please consider giving it a star on GitHub.