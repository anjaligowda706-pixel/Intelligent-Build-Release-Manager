import pandas as pd

df = pd.read_csv("preprocessed_build_data.csv")

success_rate = df["Build_Status"].mean()

if success_rate > 0.6:
    print("Build is STABLE. Ready for Release ✅")
else:
    print("Build is UNSTABLE. Fix issues ❌")

print("Success Rate:", success_rate)
