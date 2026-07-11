from flask import Flask, render_template, redirect, url_for, request, session, jsonify
import requests
import io
import base64
import qrcode
import numpy as np
import pandas as pd
from model import predictor


app2 = Flask(__name__)
app2.secret_key = 'your_secret_key'

PRODUCTS_API_URL = 'https://fakestoreapi.com/products'

data = pd.read_csv(r'.\static\dataset\upi_data.csv')


@app2.route('/')
def index():
    response = requests.get(PRODUCTS_API_URL)
    products = response.json()
    return render_template('index.html', products=products)

@app2.route('/buy/<int:product_id>', methods=['GET'])
def buy(product_id):
    product_url = f'https://fakestoreapi.com/products/{product_id}'
    response = requests.get(product_url)
    product = response.json()
    return render_template('payment.html', product=product)



@app2.route('/payment', methods=['POST'])
def payment():
    email = request.form.get('email')
    address = request.form.get('address')
    session['email'] = email
    session['address'] = address

    return redirect(url_for('checkout'))


@app2.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart = session.get('cart', [])
    total_amount = sum(item['price'] * item['quantity'] for item in cart)
    email = session.get('email', '')
    address = session.get('address', '')
    qr_code = None

    if total_amount:
        upi_id = "9705858229@axl"
        name = "Shekar"
        transaction_note = "Shopping"
        upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={total_amount}&tn={transaction_note}"

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(upi_url)
        qr.make(fit=True)

        img_buffer = io.BytesIO()
        qr_img = qr.make_image(fill='black', back_color='white')
        qr_img.save(img_buffer)
        img_buffer.seek(0)

        qr_code = base64.b64encode(img_buffer.read()).decode()

    return render_template('checkout.html', cart=cart, total_amount=total_amount, email_data=email, address=address, qr_code=qr_code)




@app2.route('/complete-purchase', methods=['POST'])
def complete_purchase():
    cart = session.get('cart', [])
    total_amount = sum(item['price'] * item['quantity'] for item in cart)

    upi_id = "9705858229@axl"
    name = "Shekar"
    transaction_note = "Shopping"
    upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={total_amount}&tn={transaction_note}"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(upi_url)
    qr.make(fit=True)

    img_buffer = io.BytesIO()
    qr_img = qr.make_image(fill='black', back_color='white')
    qr_img.save(img_buffer)
    img_buffer.seek(0)
    img_str = base64.b64encode(img_buffer.read()).decode()
    return render_template('checkout.html', cart=cart, total_amount=total_amount, qr_code=img_str)

@app2.route('/payment-success')
def payment_success():
    return render_template('payment_success.html')

@app2.route('/add-to-cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    
    email = request.form.get('email')
    address = request.form.get('address')
    session['email'] = email
    session['address'] = address
    
    
    product_url = f'https://fakestoreapi.com/products/{product_id}'
    response = requests.get(product_url)
    product = response.json()

    if 'cart' not in session:
        session['cart'] = []

    session['cart'].append({
        'product_id': product_id,
        'title': product['title'],
        'price': product['price'],
        'quantity': 1
    })

    session.modified = True
    return redirect(url_for('cart'))

@app2.route('/cart')
def cart():
    cart = session.get('cart', [])
    total_amount = sum(item['price'] * item['quantity'] for item in cart)
    session['total_amount'] = round(total_amount,2)
    email = session.get('email', '')
    address = session.get('address', '')
    return render_template('cart.html', cart=cart, total_amount=total_amount, email_data=email, address=address)



@app2.route('/update-cart/<int:product_id>', methods=['POST'])
def update_cart(product_id):
    quantity = int(request.form.get('quantity'))
    cart = session.get('cart', [])

    for item in cart:
        if item['product_id'] == product_id:
            item['quantity'] = quantity
            break

    session.modified = True
    return redirect(url_for('cart'))



@app2.route('/remove-from-cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    cart = session.get('cart', [])
    cart = [item for item in cart if item['product_id'] != product_id]
    session['cart'] = cart
    session.modified = True
    return redirect(url_for('cart'))


@app2.route('/payment-details', methods=['POST'])
def payment_details():
    total_amount = session.get('total_amount')
    print('total amount sss ', total_amount)
    return render_template('index4.html', total_amount=total_amount)


from model import predictor
@app2.route('/fraud-detector', methods=['POST'])
def fraud_detector():
    if request.method == 'POST':
        try:
            payment_method = request.form.get('payment_method')
            amount = float(request.form.get('amount'))
            initial_balance = float(request.form.get('initial_balance'))
            final_balance = float(request.form.get('final_balance'))
            balance_diff = abs(initial_balance - final_balance)
            payment_method = np.float64(payment_method)
            input_data = [payment_method, amount, initial_balance, final_balance, balance_diff]
            input_data = [
                payment_method,
                amount,
                initial_balance,
                final_balance,
                balance_diff
            ]

            fraud_prediction = predictor(input_data)
            session['fraud_prediction'] = fraud_prediction
            label = predictor(input_data)
            fraud_code = "Fraud Detected" if label else "No Fraud Detected"
            return jsonify({'fraud_code': fraud_code})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return render_template('index4.html', total_amount=session.get('total_amount', 0), selected_value=1)




if __name__ == '__main__':
    app2.run(debug=True)
