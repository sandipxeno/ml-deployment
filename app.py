from flask import Flask, request, jsonify  # Import necessary modules for Flask

# Initialize the Flask application
app = Flask(__name__)

@app.route("/")  
def home():
    """
    Home route ('/').
    Returns a simple JSON response to confirm that the API is running.
    """
    return jsonify({"message": "Hello, Inference!"})  # Respond with a JSON message

@app.route("/predict", methods=["POST"])  
def predict():
    """
    Predict route ('/predict').
    - Accepts a JSON request (POST method).
    - Placeholder for ML model inference logic.
    - Returns a fake prediction as JSON response.
    """
    data = request.json  # Get JSON data from the request
    # Placeholder: In a real scenario, process 'data' using a trained ML model
    prediction = {"result": "fake_prediction"}  
    return jsonify(prediction)  # Return the prediction as JSON

if __name__ == "__main__":
    # Run the Flask app on host 0.0.0.0 and port 5000 (accessible from any IP)
    app.run(host="0.0.0.0", port=5000)

