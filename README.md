# 🕵️‍♂️ Loan Fraud Detection API

A Flask-based REST API that detects fraudulent loan applications using a machine learning model. This API is designed to integrate with client applications (like a web dashboard or back-office system) to provide real-time fraud detection.

## 🌐 Hosted API

The API is deployed and live at:

👉 [https://loansmlapi-production.up.railway.app](https://loansmlapi-production.up.railway.app)

## 📂 Project Overview

This project provides:
- A trained fraud detection ML model
- A Flask API for serving predictions
- A single endpoint to classify incoming loan application data as fraudulent or not

## 🧠 Model Details

The model was trained using various features extracted from a loan application dataset. It uses:
- One-hot encoding for categorical features
- Preprocessing using `scikit-learn`
- A classification algorithm (e.g., Logistic Regression, Random Forest, etc.) 

## 🛠️ Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas / NumPy
- Railway for deployment

## 🔧 API Usage 
### `POST /predict`


### 📥 Request Format

Send a JSON object with the following structure (sample):

```json
{
    'dpd_5_cnt': 0.0,
    'dpd_15_cnt': 0.0,
    'dpd_30_cnt': 0.0,
    'close_loans_cnt': 2.0,
    'federal_district_nm': 3,
    'payment_type_0': 1,
    'payment_type_1': 0,
    'payment_type_2': 0,
    'payment_type_3': 0,
    'payment_type_4': 0,
    'payment_type_5': 0,
    'past_billings_cnt': 5.0,
    'score_1': 650.0,
    'score_2': 670.0,
    'age': 35,
    'gender': 1,
    'rep_loan_date_year': 2024,
    'rep_loan_date_month': 6,
    'rep_loan_date_day': 15,
    'rep_loan_date_weekday': 5,
    'first_loan_year': 2018,
    'first_loan_month': 4,
    'first_loan_day': 20,
    'first_loan_weekday': 4,
    'first_overdue_date_year': 2024.0,
    'first_overdue_date_month': 7.0,
    'first_overdue_date_day': 10.0,
    'first_overdue_date_weekday': 2,
    'has_delinquency': 0
}
```

### 📥 Response Format
```json
{
  "prediction": "Fraud"  // or "Not Fraud"
}
```
