from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello, Inference!"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    # Placeholder for ML model inference
    prediction = {"result": "fake_prediction"}
    return jsonify(prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
