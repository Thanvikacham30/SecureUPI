import os
import pickle

path = os.path.join(os.path.dirname(__file__), "xgb_classifier_model.pkl")

print("Exists:", os.path.exists(path))
print("Size:", os.path.getsize(path))

with open(path, "rb") as f:
    obj = pickle.load(f)

print(type(obj))