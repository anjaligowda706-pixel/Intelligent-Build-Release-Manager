import os

print("Starting Intelligent Build & Release Manager...\n")

os.system("python data_collection.py")
os.system("python data_preprocessing.py")
os.system("python ai_model.py")
os.system("python intell.py")

print("\nPipeline executed successfully ✅")
