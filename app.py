from flask import Flask, render_template, request
import numpy as np
import pickle
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the heart disease prediction model
try:
    with open('heart_disease_model.pkl', 'rb') as file:
        model = pickle.load(file)
    if not hasattr(model, 'predict'):
        raise TypeError("The loaded model does not have a 'predict' method.")
except (FileNotFoundError, TypeError, pickle.UnpicklingError) as e:
    model = None
    logger.error(f"Error loading model: {e}")

# Initialize the Flask application
app = Flask(__name__)

# Home route to display the HTML form
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission and make a prediction
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return render_template('index.html', prediction_text="Model not loaded. Please check the server logs for more details.")

    if request.method == 'POST':
        # Retrieve input values from the form
        try:
            age = float(request.form['age'])
            sex = float(request.form['sex'])
            cp = float(request.form['cp'])
            trestbps = float(request.form['trestbps'])
            chol = float(request.form['chol'])
            fbs = float(request.form['fbs'])
            restecg = float(request.form['restecg'])
            thalach = float(request.form['thalach'])
            exang = float(request.form['exang'])
            oldpeak = float(request.form['oldpeak'])
            slope = float(request.form['slope'])
            ca = float(request.form['ca'])
            thal = float(request.form['thal'])

            # Prepare input data for prediction
            input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            prediction = model.predict(input_data)

            # Generate result based on the prediction
            result = 'The Person has Heart Disease' if prediction[0] == 1 else 'The Person does not have a Heart Disease'

        except ValueError as ve:
            result = f"Invalid input values: {ve}"

        # Return the result and display it on the HTML page
        return render_template('index.html', prediction_text=result)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
