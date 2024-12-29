from flask import Flask, request, redirect, render_template, url_for, flash
from pymongo import MongoClient
import hashlib
from werkzeug.security import check_password_hash, generate_password_hash

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'hydradrop' 

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/") # Default port: 27017

"""
Once MongoDB is running in your terminal, run these commands in Mongo shell in Mongo Compass GUI
to create database and collections for user data and addresses that we are accessing below:
use water_delivery_db
db.createCollection('users')
db.createCollection('addresses')
"""
db = client['water_delivery_db'] 
users_collection = db['users']
addresses_collection = db['addresses']

# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Retrieve data from the form
        fname = request.form['fname']
        password = request.form['password']
        email = request.form['email']
        number = request.form['number']
        
        # Hash the password for security
        hashed_password = generate_password_hash(password)
        
        # Check if user already exists
        if users_collection.find_one({"phone": number}):
            flash("Phone number already registered. Please log in.")
            return redirect(url_for('login'))

        # Create the user and address documents
        user_data = {
            'name': fname,
            'email': email,
            'phone': number,
            'password': hashed_password
        }
        address_data = {
            'phone': number,
            'name': fname,
            'address': ''
        }
        
        # Insert into MongoDB
        try:
            users_collection.insert_one(user_data)
            addresses_collection.insert_one(address_data)
            flash("Registration successful! Please log in.")
            return redirect(url_for('login'))
        except Exception as e:
            flash(f"An error occurred: {e}")
            return redirect(url_for('register'))
    
    return render_template('register.html')  # Render registration page

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get data from the form
        phno = request.form['phno']
        pswd = request.form['pswd']
        
        # Query MongoDB to find the user
        user = users_collection.find_one({"phone": phno})
        
        # Check if the user exists and the password matches
        if user and check_password_hash(user['password'], pswd):
            flash("Login successful!")
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password. Please try again.")
            return redirect(url_for('login'))
    
    return render_template('login.html')  # Render login page

# Route to display the home page
@app.route('/home')
def home():
    return render_template('home.html')  # Render the home.html template

if __name__ == '__main__':
    app.run(debug=True)