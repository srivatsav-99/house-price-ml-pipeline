import sys, joblib, numpy as np, pandas as pd

#Usage: python src/predict_one.py
#example
row = {
    "zipcode": 98103,
    "sqft_living": 2000,
    "sqft_above": 1800,
    "grade": 7,
    "lat": 47.68,
    "sqft_basement": 200,
    "sqft_living15": 1900
}
model = joblib.load("outputs/xgb_price_model.joblib")
X = pd.DataFrame([row])
pred = np.expm1(model.predict(X))[0]
print(f"Predicted price: ${pred:,.0f}")
