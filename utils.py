import pandas as pd
import requests
import time

from config import EXCHANGE_RATE_CACHE_DURATION

exchange_cache = {}
def convert_currency(amount, from_currency="USD", to_currency="USD"):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    # Return same value if conversion not needed
    if from_currency == to_currency:
        return amount

    # Generate cache key
    cache_key = f"{from_currency}_TO_{to_currency}"

    # Check cache
    now = time.time()
    if cache_key in exchange_cache:
        cached_data = exchange_cache[cache_key]
        if now - cached_data["timestamp"] < EXCHANGE_RATE_CACHE_DURATION:
            rate = cached_data["rate"]
            return amount * rate

    # Fetch new rate
    try:
        url = f"https://api.frankfurter.app/latest?amount=1&from={from_currency}&to={to_currency}"
        response = requests.get(url)
        response.raise_for_status()
        rate = response.json()["rates"][to_currency]

        # Update cache
        exchange_cache[cache_key] = {
            "rate": rate,
            "timestamp": now
        }

        return amount * rate
    except Exception as e:
        print(f"[Currency Conversion Error]: {e}")
        return amount  # fallback to original



def is_senior(age):
    return 1 if int(age) >= 60 else 0

def estimate_total_charges(monthly_charges, tenure):
    return float(monthly_charges) * int(tenure)


def prepare_features(data):
    senior = is_senior(data['age'])
    tenure = int(data['tenure'])

    monthly_input = float(data['MonthlyCharges'])
    currency = data.get('currency', 'USD')
    monthly_usd = convert_currency(monthly_input, currency, "USD")
    
    total = estimate_total_charges(monthly_usd, tenure)

    raw_input = {
        "gender": data['gender'],
        "SeniorCitizen": senior,
        "Partner": data['Partner'],
        "Dependents": data['Dependents'],
        "tenure": tenure,
        "PhoneService": data['PhoneService'],
        "MultipleLines": data['MultipleLines'],
        "InternetService": data['InternetService'],
        "OnlineSecurity": data['OnlineSecurity'],
        "OnlineBackup": data['OnlineBackup'],
        "DeviceProtection": data['DeviceProtection'],
        "TechSupport": data['TechSupport'],
        "StreamingTV": data['StreamingTV'],
        "StreamingMovies": data['StreamingMovies'],
        "Contract": data['Contract'],
        "PaperlessBilling": data['PaperlessBilling'],
        "PaymentMethod": data['PaymentMethod'],
        "MonthlyCharges": monthly_usd,
        "TotalCharges": total
    }
    
    df = pd.DataFrame([raw_input])
    return df


def encode_binary_columns(df, columns):
    binary_cols = ['gender', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']
    for col in binary_cols:
        df[col] = df[col].map({"Yes": 1, "No": 0, "Male": 1, "Female": 0})

    df = pd.get_dummies(df)
    for col in columns:
        if col not in df:
            df[col] = 0
    df = df[columns]
    
    return df

