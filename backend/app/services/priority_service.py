import joblib

model = joblib.load("app/models/priority_model.pkl")
dept_encoder = joblib.load("app/models/dept_encoder.pkl")
priority_encoder = joblib.load("app/models/priority_encoder.pkl")

def predict_priority(confidence, department, complaint_length, time_keywords):
    dept_encoded = dept_encoder.transform([department])[0]
    X = [[confidence, dept_encoded, complaint_length, time_keywords]]
    pred = model.predict(X)[0]
    return priority_encoder.inverse_transform([pred])[0]
