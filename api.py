from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = list(data)
    prediction = list(model.predict(df))
    return jsonify({'prediction': prediction})


if __name__ == '__main__':
    model = joblib.load('finalModel.pkl')
    app.run(debug=True)
