import joblib
from monitor import log_build

model = joblib.load("build_model.pkl")

new_build_time = 20
prediction = model.predict([[new_build_time]])[0]

if prediction == 1:
    print("Build is STABLE 🚀")
    print("Auto Release Approved ✅")
else:
    print("Build is UNSTABLE ❌")
    print("Release Blocked ⚠️")

# Log build
log_build(new_build_time, prediction)
