#  Bike Rental Demand Prediction API

This project builds a machine learning model to predict bike rental demand based on historical data. The best-performing model was deployed using a Flask API that accepts input features and returns a predicted bike count.

---

##  Workflow Overview

###  1. Data Preprocessing
- Loaded dataset from CSV
- Checked for null values and data types
- Feature selection and encoding

###  2. Model Training
- Trained two models: Linear Regression and Random Forest
- Compared performance using:
  - Mean Squared Error (MSE)
  - Root Mean Squared Error (RMSE)
  - R² Score

###  3. Model Evaluation
- Random Forest performed best and was saved using joblib
- Model file: bike_rental_model.pkl

###  4. Flask API Setup
- API built using Flask in VS Code
- Two endpoints:
  - / – base route to confirm the API is live
  - /predict – accepts POST request with input features and returns predicted rental count

###  5. API Testing
- Tested locally using Postman
- Verified successful JSON predictions

---

##  Tech Stack
- Python
- Flask
- Scikit-learn
- Joblib
- Postman (for API testing)

---

##  Project Structure
/bike-rental-api ----> app.py
Flask Api Script -----> bike_rental_model.pkl 
## Trained random foret model -----> requirements.txt ----- runtime.txt


post  https://bike-rental-api-6h1y.onrender.com 

## json input 
{
  "season": 1,
  "yr": 1,
  "mnth": 4,
  "holiday": 0,
  "weekday": 0,
  "workingday": 0,
  "weathersit": 2,
  "temp": 0.212,
  "atemp":0.212,
  "hum": 0.8,
  "windspeed": 0.1
}

##Json output 

{
    "prediction": 1771.82
}

## 🌐 Live Demo
👉 https://bike-rental-api-6h1y.onrender.com



 ## IN THIS :
 ALL STEPS ARE COMPLETED SUCCESSFULLY
 API DEPLOYED AND TESTED ON RENDER
 RETURN PREDECTION ACCURATELY 



 ## CREATED BY ABBAS NAZIR 
 DATE : 28 / MAY / 2025
