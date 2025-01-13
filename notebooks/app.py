from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('D:/week4 data/linear_regression_pipeline_12-01-2025-04-44-43-590226.pkl')

# Define home route
@app.route('/')
def home():
    return "Welcome to the Sales Prediction API!"

# Define API endpoint for predictions
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get the data from the request
            data = request.get_json()
            print(f"Received data (POST): {data}")  # Print the received data for debugging
            input_df = pd.DataFrame(data)

            # Make prediction using the model
            prediction = model.predict(input_df)

            # Return the prediction as JSON
            return jsonify({'prediction': prediction.tolist()})
        except Exception as e:
            return jsonify({'error': str(e)})
    elif request.method == 'GET':
        return "The /predict endpoint expects a POST request with input data in JSON format."

if __name__ == '__main__':
    app.run(debug=True)
