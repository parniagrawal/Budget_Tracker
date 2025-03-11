import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Load the trained model
model_path = "rf_budget_model.pkl"  # Make sure your model is saved
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.title("💰 Budget Tracking & Expense Prediction App")

# User inputs for prediction
st.sidebar.header("Enter Expense Details")
category = st.sidebar.selectbox("Category", ["Food", "Transport", "Entertainment", "Bills", "Other"])
sub_category = st.sidebar.text_input("Sub-category")
payment_mode = st.sidebar.selectbox("Payment Mode", ["Cash", "Credit Card", "Online Payment"])
expense_type = st.sidebar.radio("Income or Expense?", ["Income", "Expense"])
amount = st.sidebar.number_input("Transaction Amount (₹)", min_value=0.0, step=0.01)

# Convert categorical inputs to numerical values
category_encoded = hash(category) % 10  # Simple hash encoding
payment_mode_encoded = hash(payment_mode) % 10
expense_type_encoded = 1 if expense_type == "Income" else 0

# Prepare input for prediction
input_features = np.array([[category_encoded, payment_mode_encoded, expense_type_encoded, amount]])

# Predict future expense
if st.sidebar.button("Predict Future Expense"):
    prediction = model.predict(input_features)
    st.success(f"📊 Predicted Future Expense: ₹{prediction[0]:.2f}")

# File Upload for bulk analysis
st.header("📂 Upload Financial Data for Analysis")
uploaded_file = st.file_uploader("Upload an Excel or CSV file", type=["csv", "xlsx"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
    st.dataframe(df)

    # Predict expenses for uploaded data
    if st.button("Analyze & Predict"):
        df["Predicted Expense"] = model.predict(df.drop(columns=["Debit/Credit"], errors="ignore"))
        st.write("🔮 Predicted Future Expenses:")
        st.dataframe(df[["Predicted Expense"]])
