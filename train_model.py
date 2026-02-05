import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Sample training data
data = {
    "build_time": [5, 7, 12, 15, 20],
    "failures": [0, 0, 1, 2, 3],
    "result": [1, 1, 0, 0, 0]  # 1=Stable, 0=Unstable
}

df = pd.DataFrame(data)

X = df[["build_time", "failures"]]
y = df["result"]

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "build_model.pkl")
print("Model trained & saved ✅")
