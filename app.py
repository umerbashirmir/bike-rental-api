from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("bike_rental_model.pkl")

@app.route("/")
def home():
    return render_template("index.html" , form = {})

@app.route("/predict", methods=["POST"])
def predict():
    form = request.form

    # Extract and scale inputs
    season = int(form["season"])
    yr = int(form["yr"])
    mnth = int(form["mnth"])
    holiday = int(form["holiday"])
    weekday = int(form["weekday"])
    workingday = int(form["workingday"])
    weathersit = int(form["weathersit"])
    temp = float(form["temp"]) / 50
    atemp = float(form["atemp"]) / 50
    hum = float(form["hum"]) / 100
    windspeed = float(form["windspeed"]) / 50

    features = np.array([[season, yr, mnth, holiday, weekday,
                          workingday, weathersit, temp, atemp, hum, windspeed]])

    prediction = model.predict(features)

    return render_template("index.html", prediction=round(prediction[0], 2), form=form)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
