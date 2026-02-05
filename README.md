# Intelligent Build and Release Manager

## Overview
This project implements an Intelligent Build and Release Manager using Machine Learning to automate build stability analysis and release decisions.

## Problem Statement
Manual build and release processes are time-consuming and error-prone. Unstable builds may be released accidentally, causing failures in production.

## Proposed Solution
The system analyzes build parameters using a Machine Learning model and automatically approves or blocks releases based on build stability.

## System Architecture
Data Collection → Preprocessing → ML Model Training → Build Prediction → Auto Release → Logging

## Technologies Used
- Python
- Machine Learning (Scikit-learn)
- Git & GitHub
- CSV for logging

## How to Run
1. Train the model:
python train_model.py
2. Run the build manager:


## Output
- Predicts build status (Stable / Unstable)
- Automatically approves stable builds
- Logs results in `build_monitor_log.csv`

## Conclusion
The Intelligent Build and Release Manager improves software reliability by automating build and release decisions using Machine Learning.
