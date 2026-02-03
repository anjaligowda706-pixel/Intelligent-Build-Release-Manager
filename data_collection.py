import pandas as pd

data = {
    "Build_ID": [1, 2, 3, 4, 5],
    "Build_Time": [12, 25, 15, 30, 18],
    "Build_Status": ["SUCCESS", "FAILURE", "SUCCESS", "FAILURE", "SUCCESS"],
    "Error_Log": ["None", "Compile Error", "None", "Test Failed", "None"]
}

df = pd.DataFrame(data)
df.to_csv("build_data.csv", index=False)

print("Data collection completed")
print(df)
