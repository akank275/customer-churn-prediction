import streamlit as st
import pandas as pd
import joblib

# Page Config
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# Load Model
model = joblib.load("models/churn_model.pkl")

# Title
st.title("📊 Customer Churn Prediction")
st.info(
    """
    This machine learning application predicts whether a telecom customer
    is likely to churn based on customer demographics, services, contract
    details and billing information.
    """
)

st.markdown("""
This application predicts whether a telecom customer is likely to churn based on customer behavior and subscription details.
""")

# Inputs
gender_option = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

gender = 0 if gender_option == "Female" else 1

senior = st.selectbox("Senior Citizen", [0, 1])

partner = st.selectbox("Partner", [0, 1])

dependents = st.selectbox("Dependents", [0, 1])

tenure = st.slider("Tenure (Months)", 0, 72, 12)

phone = st.selectbox("Phone Service", [0, 1])

multiple = st.selectbox("Multiple Lines", [0, 1, 2])

internet_option = st.selectbox(
    "Internet Service",
    [
        "DSL",
        "Fiber optic",
        "No"
    ]
)

internet_map = {
    "DSL": 0,
    "Fiber optic": 1,
    "No": 2
}

internet = internet_map[internet_option]

security = st.selectbox("Online Security", [0, 1, 2])

backup = st.selectbox("Online Backup", [0, 1, 2])

device = st.selectbox("Device Protection", [0, 1, 2])

support = st.selectbox("Tech Support", [0, 1, 2])

tv = st.selectbox("Streaming TV", [0, 1, 2])

movies = st.selectbox("Streaming Movies", [0, 1, 2])

contract_option = st.selectbox(
    "Contract",
    [
        "Month-to-month",
        "One year",
        "Two year"
    ]
)

contract_map = {
    "Month-to-month": 0,
    "One year": 1,
    "Two year": 2
}

contract = contract_map[contract_option]

paperless = st.selectbox("Paperless Billing", [0, 1])

payment = st.selectbox("Payment Method", [0, 1, 2, 3])

monthly = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)

total = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=1000.0
)

# Prediction
if st.button("Predict Churn"):

    data = pd.DataFrame([[
        gender,
        senior,
        partner,
        dependents,
        tenure,
        phone,
        multiple,
        internet,
        security,
        backup,
        device,
        support,
        tv,
        movies,
        contract,
        paperless,
        payment,
        monthly,
        total
    ]], columns=[
        'gender',
        'SeniorCitizen',
        'Partner',
        'Dependents',
        'tenure',
        'PhoneService',
        'MultipleLines',
        'InternetService',
        'OnlineSecurity',
        'OnlineBackup',
        'DeviceProtection',
        'TechSupport',
        'StreamingTV',
        'StreamingMovies',
        'Contract',
        'PaperlessBilling',
        'PaymentMethod',
        'MonthlyCharges',
        'TotalCharges'
    ])

    prediction = model.predict(data)[0]

    probability = model.predict_proba(data)[0][1]

    st.metric(
        "Churn Probability",
        f"{probability:.2%}"
    )

    if probability > 0.7:

      st.error(
        f"🔴 High Churn Risk ({probability:.2%})"
    )

    elif probability > 0.4:

      st.warning(
        f"🟠 Medium Churn Risk ({probability:.2%})"
    )

    else:

       st.success(
           f"🟢 Low Churn Risk ({probability:.2%})"
    )
