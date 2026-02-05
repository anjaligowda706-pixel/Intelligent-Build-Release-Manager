import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib   # <-- important

# Load data
df = pd.read_csv("preprocessed_build_data.csv")

X = df[["Build_Time"]]
y = df["Build_Status"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# SAVE MODEL (deployment step)
joblib.dump(model, "build_model.pkl")

print("ML Model Trained Successfully ✅")
print("Model Accuracy:", accuracy)
print("Model saved successfully")

