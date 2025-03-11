import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# ✅ Load the Trained Model
# -------------------------
model_path = "rf_budget_model_fixed_v2.pkl"
with open(model_path, "rb") as f:
    pipeline = pickle.load(f)

# ✅ Ensure user input matches model expectations
def preprocess_input(category, payment_mode, expense_type, amount):
    """Prepares raw input data for model prediction, ensuring 'Amount' is included."""
    input_df = pd.DataFrame({
        "Mode": [payment_mode], 
        "Category": [category], 
        "Income/Expense": [expense_type], 
        "Debit/Credit": [amount]  # Ensure 'Amount' is included
    })
    return input_df

# -------------------------
# 🎨 Streamlit UI
# -------------------------
st.title("💰 Budget Tracker & Future Expense Prediction")
st.sidebar.header("🔢 Enter Expense Details")

# -------------------------
# 🔹 User Inputs for Prediction
# -------------------------
category = st.sidebar.selectbox("Category", ["Food", "Transport", "Entertainment", "Bills", "Other"])
payment_mode = st.sidebar.selectbox("Payment Mode", ["Cash", "Credit Card", "Online Payment"])
expense_type = st.sidebar.radio("Income or Expense?", ["Income", "Expense"])
amount = st.sidebar.number_input("Transaction Amount (₹)", min_value=1.0, step=1.0)

# -------------------------
# 🔮 Make Prediction When Button is Clicked
# -------------------------
if st.sidebar.button("Predict Future Expense"):
    # ✅ Preprocess Input
    input_df = preprocess_input(category, payment_mode, expense_type, amount)

    # ✅ Ensure DataFrame has all required columns
    st.write("✅ **Processed Input Data Before Prediction:**")
    st.dataframe(input_df)

    try:
        prediction = pipeline.predict(input_df)
        st.success(f"📊 **Predicted Expense: ₹{prediction[0]:.2f}**")
    except ValueError as e:
        st.error(f"❌ Prediction Error: {e}")

# -------------------------
# 📂 File Upload for Bulk Analysis
# -------------------------
st.header("📂 Upload Financial Data for Bulk Analysis")
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
    
    st.write("📊 **Uploaded Data:**")
    st.dataframe(df)

    # ✅ Ensure required columns exist
    required_columns = ["Mode", "Category", "Income/Expense", "Debit/Credit"]
    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        st.error(f"❌ Missing columns: {', '.join(missing_columns)}. Please upload a valid file.")
    else:
        try:
            # ✅ Model expects raw categorical columns, so pass them directly
            df["Predicted Expense"] = pipeline.predict(df[["Mode", "Category", "Income/Expense", "Debit/Credit"]])

            # 🔮 Show results
            st.write("🔮 **Predicted Future Expenses:**")
            st.dataframe(df[["Debit/Credit", "Predicted Expense"]])
        except ValueError as e:
            st.error(f"❌ Bulk Prediction Error: {e}")

# -------------------------
# ✅ Run the App
# -------------------------
if __name__ == "__main__":
    st.write("📌 **Use the sidebar to enter details & predict future expenses!**")
