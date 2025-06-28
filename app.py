import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load trained model
with open("xgb_final_model.pkl", "rb") as f:
    model = pickle.load(f)

# Page config
st.set_page_config(page_title="SenioScan – NHANES Senior Predictor", layout="centered")

# Title and intro
st.title("🧠 SenioScan")
st.subheader("Predict Senior Age Category (65+) Based on NHANES Health Indicators")


st.markdown("---")

# Sidebar input form
st.sidebar.header("Enter Health Parameters")

def user_input_features():
    gender = st.sidebar.selectbox("Gender", options=["Male", "Female"])
    physical_activity = st.sidebar.selectbox("Engages in Weekly Physical Activity?", options=["Yes", "No"])
    bmi = st.sidebar.slider("BMI (Body Mass Index)", 10.0, 50.0, 25.0)
    glucose = st.sidebar.slider("Glucose Level (LBXGLU)", 50, 300, 100)
    diabetes = st.sidebar.selectbox("Diagnosed with Diabetes?", options=["Yes", "No"])
    glucose_tolerance = st.sidebar.slider("Oral Glucose Tolerance (LBXGLT)", 50, 300, 120)
    insulin = st.sidebar.slider("Insulin Level (LBXIN)", 0.0, 300.0, 50.0)

    # Encode categorical variables
    encoded_gender = 1 if gender == "Male" else 2
    encoded_activity = 1 if physical_activity == "Yes" else 2
    encoded_diabetes = 1 if diabetes == "Yes" else 2

    data = {
        "RIAGENDR": encoded_gender,
        "PAQ605": encoded_activity,
        "BMXBMI": bmi,
        "LBXGLU": glucose,
        "DIQ010": encoded_diabetes,
        "LBXGLT": glucose_tolerance,
        "LBXIN": insulin
    }

    return pd.DataFrame([data])

# Collect user input
input_df = user_input_features()

# Display input
st.markdown("### 📝 Input Summary")
st.write(input_df)

# Prediction
if st.button("🔍 Predict"):
    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.success(f"🧓 Prediction: **Senior (65+)** with {proba:.2%} confidence.")
    else:
        st.info(f"🧍 Prediction: **Non-Senior (<65)** with {1 - proba:.2%} confidence.")

    st.markdown("🧠 *Model used:* XGBoost (best performer after tuning multiple models: RandomForest, CatBoost, SVM, AdaBoost)")

else:
    st.caption("Click the button above to predict age group.")

# Footer
st.markdown("---")
st.markdown("Built during AI Planet's NHANES Hackathon | Summer Analytics 2025 – IIT Guwahati")
