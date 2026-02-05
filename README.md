# Intelligent Build and Release Manager

## Project Description
This project demonstrates an Intelligent Build and Release Manager using Machine Learning.
It predicts build stability based on historical build data and automates release approval.

## Technologies Used
- Python
- Machine Learning (Logistic Regression)
- Scikit-learn
- Git & GitHub

## Project Structure
- train_model.py : Trains and saves ML model
- intell.py : Main pipeline execution
- build_model.pkl : Trained ML model
- build_monitor_log.csv : Build monitoring logs

## How to Run
1. Install dependencies
   pip install -r requirements.txt

2. Train the model (optional)
   python train_model.py

3. Run the pipeline
   python intell.py

## Output
- Build stability prediction
- Auto release approval
- Pipeline execution status

## Conclusion
The project automates build monitoring and release decisions using ML.
