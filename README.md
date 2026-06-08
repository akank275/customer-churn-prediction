# 📊 Customer Churn Prediction System

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

# 🚀 Customer Churn Prediction Using Machine Learning

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to churn based on customer demographics, subscription details, contract type, and billing information.

This project combines:

✅ Data Cleaning

✅ Exploratory Data Analysis (EDA)

✅ Feature Engineering

✅ Machine Learning Modeling

✅ Streamlit Deployment

✅ Business Insights

---

## 🎯 Business Problem

Customer churn is one of the biggest challenges faced by telecom companies.

Acquiring a new customer is significantly more expensive than retaining an existing one.

The goal of this project is to identify customers who are likely to leave the company so proactive retention strategies can be implemented.

---

## 📂 Dataset

**Dataset:** IBM Telco Customer Churn Dataset

### Features

* Gender
* Senior Citizen
* Partner
* Dependents
* Tenure
* Phone Service
* Multiple Lines
* Internet Service
* Online Security
* Online Backup
* Device Protection
* Tech Support
* Streaming TV
* Streaming Movies
* Contract Type
* Paperless Billing
* Payment Method
* Monthly Charges
* Total Charges

### Target Variable

**Churn**

* Yes
* No

---

## ⚙️ Tech Stack

### Programming

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib

### Deployment

* Streamlit

### Version Control

* Git
* GitHub

---

## 🔄 Project Workflow


Data Collection
        ↓
Data Cleaning
        ↓
Data Preprocessing
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Churn Prediction
        ↓
Streamlit Deployment


---

## 📈 Exploratory Data Analysis

### Correlation Heatmap

![Heatmap](screenshots/heatmap.png)

---

## 🤖 Machine Learning Models

The following models were evaluated:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

### Best Performing Model

🏆 Random Forest Classifier

### Accuracy

**79.56%**

---

## 📊 Model Comparison

![Model Comparison](screenshots/model_comparison.png)

---

## 📉 ROC Curve

![ROC Curve](screenshots/roc_curve.png)

---

## 🔥 Feature Importance

Top factors influencing churn:

* Contract Type
* Tenure
* Monthly Charges
* Total Charges
* Internet Service

### Feature Importance Chart

![Feature Importance](screenshots/feature_importance.png)

---

## 💡 Key Business Insights

### Finding #1

Customers with Month-to-Month contracts have the highest churn rate.

### Finding #2

Customers with lower tenure are more likely to churn.

### Finding #3

Higher monthly charges are associated with increased churn risk.

### Finding #4

Long-term contracts improve customer retention.

### Finding #5

Customers using Tech Support services churn less frequently.

---

## 🖥️ Streamlit Web Application

### Home Page

![Application](screenshots/app_home.png)

---

### Prediction Example

![Prediction](screenshots/prediction_result.png)

---

## ✨ Application Features

* Real-Time Churn Prediction
* Churn Probability Score
* Customer Risk Classification
* Interactive Dashboard
* Business-Oriented Insights

---

## 📁 Project Structure

customer-churn-prediction/

├── app.py
├── requirements.txt
├── README.md

├── models/
│   └── churn_model.pkl

├── notebooks/
│   └── churn_analysis.ipynb

├── screenshots/
│   ├── heatmap.png
│   ├── model_comparison.png
│   ├── roc_curve.png
│   ├── feature_importance.png
│   ├── app_home.png
│   └── prediction_result.png


---

## ▶️ Installation

Clone the repository


git clone https://github.com/akank275/customer-churn-prediction.git


Move into the project directory

cd customer-churn-prediction


Install dependencies


pip install -r requirements.txt


Run the application


streamlit run app.py


---

## 🌐 Live Demo

Add your deployed Streamlit URL here:


https://your-app-name.streamlit.app


---

## 🚀 Future Enhancements

* Hyperparameter Tuning
* XGBoost Implementation
* SHAP Explainability
* Power BI Dashboard
* Automated Retention Recommendations

---

## 👩‍💻 Author

### Akanksha Kumari Sinha

Aspiring Data Analyst | Python | SQL | Power BI | Machine Learning

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
