from flask import Flask, render_template, request
import joblib
import numpy

app = Flask(__name__)
model = joblib.load("model/heart_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect user input
        age = float(request.form['age'])
        anaemia = float(request.form['anaemia'])
        diabetes = float(request.form['diabetes'])
        high_blood_pressure = float(request.form['high_blood_pressure'])
        sex = float(request.form['sex'])
        smoking = float(request.form['smoking'])

        # Use default or average values for the rest
        creatinine_phosphokinase = 250.0     # average
        ejection_fraction = 38.0             # average
        platelets = 263358.03                # average
        serum_creatinine = 1.0               # average
        serum_sodium = 137.0                 # average
        time = 130.0                         # median follow-up time

        features = [
            age, anaemia, creatinine_phosphokinase, diabetes,
            ejection_fraction, high_blood_pressure, platelets,
            sex, serum_creatinine, serum_sodium, smoking, time
        ]

        prediction = model.predict([features])
        result = "⚠️ High Risk of Heart Failure" if prediction[0] == 1 else "✅ Low Risk of Heart Failure"

        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)