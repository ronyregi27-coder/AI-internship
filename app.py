import streamlit as st
import pandas as pd
import joblib



model = joblib.load("heart_disease_model.pkl")


st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)


# Title
st.title("❤️ Heart Disease Prediction")
st.write("Enter the patient's information below to predict the heart disease status.")


age = st.number_input("Age", min_value=1, max_value=120, value=50)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

blood_pressure = st.number_input(
    "Blood Pressure",
    min_value=50.0,
    max_value=250.0,
    value=120.0
)

cholesterol = st.number_input(
    "Cholesterol Level",
    min_value=50.0,
    max_value=500.0,
    value=200.0
)

exercise = st.selectbox(
    "Exercise Habits",
    ["Low", "Medium", "High"]
)

smoking = st.selectbox(
    "Smoking",
    ["Yes", "No"]
)

family_heart_disease = st.selectbox(
    "Family Heart Disease",
    ["Yes", "No"]
)

diabetes = st.selectbox(
    "Diabetes",
    ["Yes", "No"]
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0
)

high_blood_pressure = st.selectbox(
    "High Blood Pressure",
    ["Yes", "No"]
)

low_hdl = st.selectbox(
    "Low HDL Cholesterol",
    ["Yes", "No"]
)

high_ldl = st.selectbox(
    "High LDL Cholesterol",
    ["Yes", "No"]
)

alcohol = st.selectbox(
    "Alcohol Consumption",
    ["Low", "Medium", "High"]
)

stress = st.selectbox(
    "Stress Level",
    ["Low", "Medium", "High"]
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=7.0
)

sugar = st.selectbox(
    "Sugar Consumption",
    ["Low", "Medium", "High"]
)

triglyceride = st.number_input(
    "Triglyceride Level",
    min_value=20.0,
    max_value=1000.0,
    value=150.0
)

fasting_blood_sugar = st.number_input(
    "Fasting Blood Sugar",
    min_value=50.0,
    max_value=400.0,
    value=100.0
)

crp = st.number_input(
    "CRP Level",
    min_value=0.0,
    max_value=100.0,
    value=3.0
)

homocysteine = st.number_input(
    "Homocysteine Level",
    min_value=0.0,
    max_value=100.0,
    value=10.0
)



if st.button("🔍 Predict Heart Disease"):

    
    input_data = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "Blood Pressure": [blood_pressure],
        "Cholesterol Level": [cholesterol],
        "Exercise Habits": [exercise],
        "Smoking": [smoking],
        "Family Heart Disease": [family_heart_disease],
        "Diabetes": [diabetes],
        "BMI": [bmi],
        "High Blood Pressure": [high_blood_pressure],
        "Low HDL Cholesterol": [low_hdl],
        "High LDL Cholesterol": [high_ldl],
        "Alcohol Consumption": [alcohol],
        "Stress Level": [stress],
        "Sleep Hours": [sleep_hours],
        "Sugar Consumption": [sugar],
        "Triglyceride Level": [triglyceride],
        "Fasting Blood Sugar": [fasting_blood_sugar],
        "CRP Level": [crp],
        "Homocysteine Level": [homocysteine]
    })

  
    prediction = model.predict(input_data)[0]

    
    st.subheader("Prediction Result")

    if prediction == "Yes":
        st.error("⚠️ Heart Disease Status: YES")
    else:
        st.success("✅ Heart Disease Status: NO")