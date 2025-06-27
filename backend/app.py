from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import joblib
import numpy

app = Flask(__name__)
CORS(app)
model = joblib.load("model/heart_model.pkl")


@app.route("/")
def home():
    return "Heart Failure Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Received data:", data)  # Debug statement

        age = float(data['age'])
        anaemia = float(data['anaemia'])
        diabetes = float(data['diabetes'])
        high_blood_pressure = float(data['high_blood_pressure'])
        sex = float(data['sex'])
        smoking = float(data['smoking'])
        
        

        # Default values
        creatinine_phosphokinase = 250.0
        ejection_fraction = 38.0
        platelets = 263358.03
        serum_creatinine = 1.0
        serum_sodium = 137.0
        time = 130.0

        features = [
            age, anaemia, creatinine_phosphokinase, diabetes,
            ejection_fraction, high_blood_pressure, platelets,
            sex, serum_creatinine, serum_sodium, smoking, time
        ]
        print("Features for prediction:", features)  # Debug

        prediction = model.predict([features])
        result = int(prediction[0])

        print("Prediction result:", prediction)  # Debug
        return jsonify({
            'prediction': result,
            'message': "⚠️ High Risk" if result == 1 else "✅ Low Risk"
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == "__main__":
    app.run(debug=True)