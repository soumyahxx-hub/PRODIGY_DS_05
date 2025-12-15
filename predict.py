# predict.py
import joblib
import pandas as pd

# Load saved pipeline (preprocessor + model)
obj = joblib.load("tree_pipeline.joblib")
preprocessor = obj['preprocessor']
model = obj['model']

# Example input row - EDIT these values to match your dataset columns
single = {
    "age": [30],
    "job": ["technician"],
    "marital": ["married"],
    "education": ["secondary"],
    "default": ["no"],
    "balance": [1000],
    "housing": ["yes"],
    "loan": ["no"],
    "contact": ["cellular"],
    "day": [5],
    "month": ["may"],
    "duration": [200],
    "campaign": [1],
    "pdays": [999],
    "previous": [0],
    "poutcome": ["unknown"]
}

# Create dataframe, transform, and predict
df = pd.DataFrame(single)
Xt = preprocessor.transform(df)
pred = model.predict(Xt)
prob = model.predict_proba(Xt) if hasattr(model, "predict_proba") else None

print("Prediction (1 = yes, 0 = no):", int(pred[0]))
if prob is not None:
    print("Probabilities:", prob[0])

