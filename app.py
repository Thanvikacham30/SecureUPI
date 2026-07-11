from flask import Flask, render_template, request, jsonify
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
from model import predictor

app = Flask(__name__)
scaler = StandardScaler()

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(BASE_DIR, "static", "dataset", "upi_data.csv")

data = pd.read_csv(csv_path) 

scaler.fit_transform(data.values) 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # balance_diff = int(request.form.get('balance_diff'))
        payment_method = np.float64(request.form.get('payment_method'))
        amount = np.float64(request.form.get('amount'))
        initial_balance = np.float64(request.form.get('initial_balance'))
        final_balance = np.float64(request.form.get('final_balance'))
        balance_diff = abs(initial_balance-final_balance)
        
        x_input = np.array([[payment_method,
                            amount,
                            initial_balance,
                            final_balance,
                            balance_diff]])

        x_input_scaled = scaler.transform(x_input)
        
        input_data = [
            payment_method,
            amount,
            initial_balance,
            final_balance,
            balance_diff
        ]

        fraud_prediction = predictor(input_data)
        
        if fraud_prediction:
            fraud_code = "Fraud Detected"
        else:
            fraud_code = "No Fraud Detected"
        return jsonify({'fraud_code': fraud_code})
    return render_template('index3.html')

if __name__ == '__main__':
    app.run(debug=True)
