#  Project Architecture – Bike Rental Demand Prediction

This architecture shows the end-to-end flow of the project from user input to model prediction and response.

---

##  Components

1. Client (Postman / Python Script / User)
   - Sends a POST request to the API
   - Includes input data (11 features like temp, atemp, hum, etc.)

2. Flask API (Deployed on Render)
   - Receives the request at the /predict endpoint
   - Extracts the data and converts it into a NumPy array
   - Loads the trained model (bike_rental_model.pkl)
   - Sends the array to the model for prediction

3. Machine Learning Model
   - Random Forest Regressor
   - Trained using historical bike rental data
   - Returns the predicted rental count as output

4. Response (Returned to Client)
   - JSON response with "prediction": value
   - Sent back to Postman or Python script

---

##  Data Flow Summary
User Input (Postman)  Flask API Load Model (.pkl)  Make Prediction  Return JSON Response

---

## 🧰 Deployment

- Platform: Render (uses GitHub auto-deploy)
- Public URL: [https://bike-rental-api.onrender.com](https://bike-rental-api.onrender.com)
- Method: GitHub → Render Web Service
- Port: 5000 (bound to 0.0.0.0)
