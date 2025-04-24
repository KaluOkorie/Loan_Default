import streamlit as st
import joblib
import pandas as pd

# Load the 4-feature model
model = joblib.load('4_feature_model.pkl')  # Ensure this is the retrained model

# Streamlit UI
st.title("Loan Default Prediction")

# Inputs for the 4 features
age = st.number_input("Age", min_value=18, max_value=100, value=30)
credit_amount = st.number_input("Credit Amount (USD)", min_value=0, value=1000)
employment_duration = st.number_input("Employment Duration (years)", min_value=0, value=3)
credit_history = st.selectbox(
    "Credit History",
    options=[0, 1, 2, 3, 4],
    format_func=lambda x: [
        "No credits/all paid",
        "All credits paid",
        "Existing credits paid",
        "Past delays",
        "Critical account"
    ][x]
)

# Create input DataFrame (order must match model's feature order)
input_data = pd.DataFrame({
    'age': [age],
    'credit_amount': [credit_amount],
    'employment_duration': [employment_duration],
    'credit_history': [credit_history]
})

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    result = "High Risk (Default)" if prediction == 1 else "Low Risk (No Default)"
    st.success(f"**Prediction:** {result}")