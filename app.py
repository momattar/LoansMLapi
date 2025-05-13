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





if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001)

