# 🔒 SecureUPI – Smart UPI Payment System with Fraud Detection

SecureUPI is a **Flask-based web application** that demonstrates a secure digital payment workflow integrated with fraud detection. The project simulates an online shopping experience where users can browse products, add items to a cart, generate UPI QR codes for payment, and verify transactions before completing payment.

The application includes a fraud detection module that analyzes transaction details such as payment type, transaction amount, account balance, and balance differences to identify potentially fraudulent transactions.

---

## ✨ Features

- 🛒 E-commerce shopping interface
- 💳 Secure UPI payment simulation
- 📱 Dynamic QR code generation
- 🔍 Transaction fraud detection
- 📦 Shopping cart management
- 👤 User information collection (Email & Address)
- 🌐 Responsive Flask web application

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- Pandas
- NumPy
- Scikit-learn
- QRCode

---

## 🚀 Project Workflow

1. Browse available products.
2. Add products to the shopping cart.
3. Enter customer details.
4. Generate a UPI QR code for payment.
5. Enter transaction details.
6. Validate the transaction using the fraud detection module.
7. Complete the payment if the transaction is safe.

---

## 📂 Project Structure

```
UPI/
│── app.py
│── app2.py
│── model.py
│── static/
│   ├── dataset/
│   ├── images/
│   └── *.css
│── templates/
│── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/SecureUPI.git
cd SecureUPI
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🔮 Future Enhancements

- 🤖 Machine Learning–based fraud detection
- 💰 Payment gateway integration
- 🔐 User authentication & authorization
- 📊 Admin dashboard
- 📈 Transaction history & analytics
- 📧 Email/SMS notifications

---


## ⚠️ Disclaimer

This project was developed for educational purposes to demonstrate secure digital payment workflows and fraud detection concepts. It is not intended for production use.
