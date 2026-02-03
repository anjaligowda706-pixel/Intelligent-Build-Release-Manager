import pandas as pd

# Load collected data
df = pd.read_csv("build_data.csv")

# Replace None values
df["Error_Log"] = df["Error_Log"].replace("None", "No Error")

# Convert SUCCESS / FAILURE to numbers
df["Build_Status"] = df["Build_Status"].map({
    "SUCCESS": 1,
    "FAILURE": 0
})

# Save preprocessed data
df.to_csv("preprocessed_build_data.csv", index=False)

print("Data preprocessing completed successfully")
print(df)
