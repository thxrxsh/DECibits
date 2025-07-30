from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from flask import jsonify

from config import model, scaler, columns
from utils import prepare_features, encode_binary_columns


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    
    
    # Prepare features
    df = prepare_features(data)

    # Encode binary columns
    df = encode_binary_columns(df, columns)

    # Predict using the model
    df_scaled = scaler.transform(df)
    pred = model.predict(df_scaled)[0]
    prob = model.predict_proba(df_scaled)[0]
    confidence = abs(prob[1] - prob[0]) * 100

    
    print(f"Prediction: {model.predict(df_scaled)}\n Confidence: {confidence} \n Probability: {model.predict_proba(df_scaled)} ")

    # Return JSON response
    return jsonify({
        "churn_prediction": int(pred),
        "confidence": round(confidence, 2),
        "probabilities": {
            "churn": float(prob[1]),
            "stay": float(prob[0])
        }
    })

if __name__ == "__main__":
    app.run(debug=True)
