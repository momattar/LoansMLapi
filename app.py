from flask import Flask, request, jsonify
import pandas as pd
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = joblib.load("Model2.pkl")  # pipeline includes preprocessing


# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         data = request.json

#         # Convert all keys to lowercase
#         lowercase_data = {k.lower(): v for k, v in data.items()}

#         df = pd.DataFrame([lowercase_data])  # must match model training features

#         prediction = model.predict(df)[0]

#         return jsonify({
#             "prediction": int(prediction),
#             "message": "This transaction can be fraud" if prediction == 1 else "This transaction looks like it is not a fraud"
#         })

#     except Exception as e:
#         print("❌ Error:", e)
#         return jsonify({"error": str(e)}), 400
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        lowercase_data = {k.lower(): v for k, v in data.items()}
        df = pd.DataFrame([lowercase_data])

        proba = model.predict_proba(df)[0]
        prediction = model.predict(df)[0]

        return jsonify({
            "prediction": int(prediction),
            "probability_fraud": round(float(proba[1]), 4),
            "message": "This transaction can be fraud" if prediction == 1 else "This transaction looks like it is not a fraud"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/test', methods=['GET'])
def test_page():
    return '''
    <html>
    <head><title>Test Fraud Detection</title></head>
    <body>
        <h2>Test Transaction Input (Model 2)</h2>
        <button onclick="sendTest()">Send Test Fraud Sample</button>
        <pre id="output"></pre>
        <script>
            async function sendTest() {
                const data = {
                    dpd_5_cnt: 6,
                    dpd_15_cnt: 5,
                    dpd_30_cnt: 4,
                    close_loans_cnt: 0,
                    federal_district_nm: 5,
                    payment_type_0: 0,
                    payment_type_1: 0,
                    payment_type_2: 1,
                    payment_type_3: 0,
                    payment_type_4: 0,
                    payment_type_5: 0,
                    past_billings_cnt: 22,
                    score_1: 320,
                    score_2: 280,
                    age: 19,
                    gender: 1,
                    rep_loan_date_year: 2024,
                    rep_loan_date_month: 12,
                    rep_loan_date_day: 20,
                    rep_loan_date_weekday: 3,
                    first_loan_year: 2024,
                    first_loan_month: 6,
                    first_loan_day: 10,
                    first_loan_weekday: 1,
                    first_overdue_date_year: 2024,
                    first_overdue_date_month: 7,
                    first_overdue_date_day: 18,
                    first_overdue_date_weekday: 5,
                    has_delinquency: 1
                };

                const response = await fetch('/predict', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });

                const result = await response.json();
                document.getElementById('output').innerText = JSON.stringify(result, null, 2);
            }
        </script>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(port=5000)

