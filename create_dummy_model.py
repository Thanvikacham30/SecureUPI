import pickle
from sklearn.dummy import DummyClassifier
import numpy as np

# Dummy training data (5 features)
X = np.array([
    [0, 100, 1000, 900, 100],
    [1, 200, 1000, 800, 200]
])

y = np.array([0, 1])

model = DummyClassifier(strategy="most_frequent")
model.fit(X, y)

with open("xgb_classifier_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Dummy model created.")