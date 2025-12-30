import pandas as pd
import lightgbm as lgb
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("app/data/priority_training.csv")

# Encode categorical
dept_encoder = LabelEncoder()
df["dept_encoded"] = dept_encoder.fit_transform(df["department"])

priority_encoder = LabelEncoder()
df["priority_encoded"] = priority_encoder.fit_transform(df["priority_label"])

X = df[["confidence_score", "dept_encoded", "complaint_length", "time_keywords"]]
y = df["priority_encoded"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = lgb.LGBMClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "app/models/priority_model.pkl")
joblib.dump(dept_encoder, "app/models/dept_encoder.pkl")
joblib.dump(priority_encoder, "app/models/priority_encoder.pkl")

print("Priority model trained.")
