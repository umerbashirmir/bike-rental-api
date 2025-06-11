#  Project Wireframe – Bike Rental Prediction App

This wireframe outlines the flow of the deployed machine learning application that predicts bike rental demand based on user inputs.

---

##  User Flow


+------------------------+
| User Enters Data |
| (via Form or Postman) |
+------------------------+
↓
+------------------------+
| Flask API (app.py) |
| - Receives input |
| - Loads model (.pkl) |
| - Preprocesses data |
| - Makes prediction |
+------------------------+
↓
+------------------------+
| Prediction Returned |
| - Web Output (HTML) |
| - JSON via Postman |
+------------------------+




---

##  Input Fields

Users provide:
- Season (Spring, Summer, Fall, Winter)
- Year (2011 or 2012 – from dataset)
- Month (January to December)
- Weekday (Sunday to Saturday)
- Holiday (Yes/No)
- Working Day (Yes/No)
- Weather (Clear, Misty, Rainy, Foggy)
- Temperature (°C)
- Feels Like Temp (°C)
- Humidity (%)
- Windspeed (km/h)

---

##  Backend Workflow

1. Receives input via form
2. Normalizes temperature, humidity, and windspeed
3. Uses joblib to load `bike_rental_model.pkl`
4. Predicts using Random Forest
5. Returns prediction to user

---

##  Output

- Prediction shown in browser as:  
  📈 **Predicted Rentals: 1720.57**

- Also viewable via Postman as JSON:
  ```json
  {
    "prediction": 1720.57
  }

This app only accepts 2011 and 2012 as year inputs.
Why? Because the model was trained on the original dataset which only contains data from 2011 and 2012.
More years can be added in the future by retraining with newer data.



















