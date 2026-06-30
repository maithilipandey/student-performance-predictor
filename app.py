from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("models/student_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    hours = float(request.form["hours"])
    sleep = float(request.form["sleep"])
    attendance = float(request.form["attendance"])
    previous = float(request.form["previous"])

    student = pd.DataFrame({
        "Hours_Studied": [hours],
        "Sleep_Hours": [sleep],
        "Attendance": [attendance],
        "Previous_Marks": [previous]
    })

    prediction = model.predict(student)[0]

    return render_template(
        "index.html",
        prediction=round(prediction, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)