import joblib

model = joblib.load("model/gradient_boosting_model.pkl")
scaler = joblib.load("model/scaler.pkl")
columns = joblib.load("model/columns.pkl")

EXCHANGE_RATE_CACHE_DURATION = 3600  # 1 hour