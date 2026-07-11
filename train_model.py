import pandas as pd
import pickle
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv("static/dataset/upi_data.csv")

# Adjust these column names to match your dataset
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = XGBClassifier(
    random_state=42,
    eval_metric="logloss"
)

model.fit(X_train, y_train)

with open("xgb_classifier_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully.")