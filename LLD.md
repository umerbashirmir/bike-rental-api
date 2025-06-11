#  Low-Level Design (LLD) – Bike Rental Demand Prediction API

##  Files & Structure
/bike-rental-api/

├── app.py                  # Flask API with predict logic
├── bike_rental_model.pkl   # Trained model
├── requirements.txt        # Python dependencies
├── runtime.txt             # Python version for Render
└── README.md               # Project summary

---

## 📄 app.py

`python
@app.route("/")
def home():
    return "Bike Rental Prediction API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = np.array([[...]])
    prediction = model.predict(features)
    return jsonify({"prediction": float(prediction[0])})

Receives POST request with JSON body

Extracts 11 features (including atemp)

Sends data to the Random Forest model

Returns prediction as JSON



