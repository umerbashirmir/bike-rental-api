#  High-Level Design (HLD) – Bike Rental Demand Prediction API

##  Objective
To develop and deploy a machine learning model that predicts the demand for bike rentals using historical and weather-related data.

---

##  System Architecture

1. Data Processing
- Source: CSV file ( bike rental data)
- Cleaning, encoding, and scaling features
- Splitting into train and test sets

2. Model Building
- Models used: Linear Regression and Random Forest Regressor
- Evaluation metrics: MSE, RMSE, R²
- Best model saved as bike_rental_model.pkl using joblib

3. API Layer
- Developed using Flask
- Exposes 2 endpoints:
  - / → Health check route
  - /predict → Accepts POST request with JSON input and returns prediction

4. Deployment
- Platform: Render
- Deployment using GitHub → Auto builds → Exposed via public URL
- Runtime: Python 3.10

---

##  Tech Stack
- Python
- Flask
- Scikit-learn
- Joblib
- Render (for deployment)
- Postman (for testing)

---

## Security & Assumptions
- No user authentication (demo purpose only)
- Assumes input is clean and structured
