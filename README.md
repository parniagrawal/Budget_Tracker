# 💰 Budget Tracker ML - Predict & Manage Your Expenses

![Budget Tracker Banner](https://img.shields.io/badge/Machine_Learning-Budget_Tracking-blue?style=flat-square)

## 📌 Overview
This project is a **Machine Learning-based Budget Tracking Model** that predicts **future expenses** based on past spending patterns. It uses **Random Forest Regression** to analyze financial transactions and helps users track, visualize, and forecast their expenses efficiently.

## 🚀 Features
✅ Predict future expenses based on spending patterns  
✅ Categorize transactions into **Income** and **Expense**  
✅ Interactive **Streamlit web app** for user-friendly predictions  
✅ **Visual analytics**: Expense trends, category-wise distribution, and actual vs. predicted expenses  
✅ Supports **CSV & Excel file uploads** for bulk expense analysis  
✅ **Feature importance analysis** to understand key factors affecting expenses  

---

## 🛠️ Installation & Setup
### **1️⃣ Clone the Repository**
git clone https://github.com/parniagrawal/Budget_Tracker.git
cd Budget_Tracker

2️⃣ Install Dependencies
Make sure you have Python installed, then run:
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app.py

📂 Project Structure
📦 Budget_Tracker
│-- 📁 model_graphs/           # Contains saved visualization graphs
│-- 📂 data/                   # Dataset for training
│-- 📂 models/                 # Trained ML models
│-- app.py                     # Streamlit web app
│-- budget_model.pkl           # Saved Random Forest Model
│-- requirements.txt           # Dependencies for easy setup
│-- README.md                  # Project documentation (this file)

📊 Model Performance
Metric	Score
R² Score	0.99
MAE	~608
MSE	1,733,007
The model achieves 99% accuracy in predicting expenses, ensuring precise budgeting.

📈 Visualizations
This project includes important graphs to analyze spending patterns:
📊 Expense Distribution
📈 Monthly Expense Trends
🎯 Actual vs. Predicted Expenses
🌟 Feature Importance Analysis

🔥 Future Enhancements
🚀 Implement LSTM (Deep Learning) for time-series forecasting
🚀 Add a database (PostgreSQL) for persistent tracking
🚀 Deploy the app on Streamlit Cloud, AWS, or Heroku




