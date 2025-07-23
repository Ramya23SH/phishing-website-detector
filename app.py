from flask import Flask, render_template, request
import pickle
from feature_extraction import extract_features

app = Flask(__name__)  # ✅ Define the app object before routes

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    url = request.form["url"]
    features = extract_features(url)

    # Debug print: see what features you're extracting
    print("Extracted Features:", features)
    print("Number of features:", len(features) if features else "No features")

    # Fix: Check if model expects 30 features but extract_features gives 31
    if features is None:
        prediction = "Feature extraction failed!"
    elif len(features) != 30:
        prediction = f"Feature count mismatch! Expected 30, got {len(features)}"
    else:
        result = model.predict([features])[0]
        prediction = "Phishing Website" if result == 1 else "Legitimate Website"

    return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
