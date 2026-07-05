import os
import sqlite3
import datetime
from flask import Flask, render_template, request, redirect,url_for, send_from_directory, abort
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import smtplib
from email.mime.text import MIMEText
import random
from flask import flash
import time
app = Flask(__name__, static_folder='static')   
app.secret_key = "secret123"
otp_store = {}
# 🔹 LANDING PAGE
@app.route('/')
def home():
    return render_template('landing.html')
# 🔹 LOGIN PAGE
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        otp = str(random.randint(100000, 999999))
        # store OTP + time
        otp_store[email] = {
            "otp": otp,
            "time": time.time()
        }
        # 📧 SEND EMAIL
        sender_email = "mesharanya.a@gmail.com"
        app_password = "abpf dpjt ngdl fjmc"
        msg = MIMEText(f"Your OTP is: {otp}")
        msg['Subject'] = "OTP Verification"
        msg['From'] = sender_email
        msg['To'] = email
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)
            server.quit()
            flash("OTP sent to Email successfully ✅")
        except Exception as e:
            print("Error:", e)
            flash("Failed to send OTP ❌")
        return render_template('verify.html', email=email)
    return render_template('login.html')
# 🔹 VERIFY OTP
@app.route('/verify', methods=['POST'])
def verify():
    user_otp = request.form['otp']
    for email, data in otp_store.items():
        if data["otp"] == user_otp:
            if time.time() - data["time"] > 60:
                flash("OTP expired ❌ Please resend")
                return redirect('/login')
            flash("Login successful ✅")
            return redirect('/start')
    flash("Invalid OTP ❌")
    return render_template('verify.html', email=email)
UPLOAD_FOLDER = 'static/uploads'
PHOTO_FOLDER = 'static/photos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PHOTO_FOLDER, exist_ok=True)
def create_database():
    conn = sqlite3.connect('image_details.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS image_details (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            dob TEXT NOT NULL,
            address TEXT,
            gender TEXT,
            crime_history TEXT,
            last_seen TEXT,
            case_id TEXT
        )
    ''')
    conn.commit()
    conn.close()
def populate_database(filename, name, age, dob, address, gender, crime_history, last_seen, case_id):
    conn = sqlite3.connect('image_details.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO image_details 
        (filename, name, age, dob, address, gender, crime_history, last_seen, case_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (filename, name, age, dob, address, gender, crime_history, last_seen, case_id))
    conn.commit()
    conn.close()
def add_sample_data():
    populate_database('m-010-01.jpg', 'Rahul Verma', 32, '1992-06-15', 'Delhi, India', 'Male', 'Theft', 'Noida', 'CASE102')
    populate_database('m-015-01.jpg', 'Amit Sharma', 40, '1984-03-22', 'Bangalore, India', 'Male', 'Cyber Crime', 'Hyderabad', 'CASE103')
    populate_database('m-025-01.jpg', 'Rohit Singh', 29, '1995-08-10', 'Pune, India', 'Male', 'Robbery', 'Mumbai', 'CASE104')
    populate_database('m-030-01.jpg', 'Vikram Patel', 35, '1989-01-05', 'Ahmedabad, India', 'Male', 'Drug Trafficking', 'Surat', 'CASE105')
    populate_database('m-035-01.jpg', 'Arjun Kapoor', 38, '1987-05-21', 'Mumbai, India', 'Male',  'Extortion', 'Nagpur', 'CASE106')
    populate_database('m-040-01.jpg', 'James Anderson', 42, '1982-07-30', 'London, UK', 'Male', 'Bank Fraud', 'Manchester, UK', 'CASE301')
    populate_database('m-045-01.jpg', 'Carlos Ramirez', 36, '1988-03-12', 'Madrid, Spain', 'Male', 'Drug Trafficking', 'Barcelona, Spain', 'CASE302')
    populate_database('m-050-01.jpg', 'Wei Zhang', 33, '1991-11-05', 'Beijing, China', 'Male', 'Cyber Crime', 'Shanghai, China', 'CASE303')
    populate_database('m-055-01.jpg', 'Michael Brown', 45, '1979-02-18', 'New York, USA', 'Male', 'Money Laundering', 'Chicago, USA', 'CASE304')
    populate_database('m-060-01.jpg', 'Ahmed Khan', 38, '1986-09-25', 'Lahore, Pakistan', 'Male', 'Extortion', 'Karachi, Pakistan', 'CASE305')
    populate_database('f-006-01.jpg', 'Anjali Mehta', 27, '1997-04-12', 'Delhi, India', 'Female', 'Pickpocketing', 'Delhi', 'CASE201')
    populate_database('f-012-01.jpg', 'Sneha Reddy', 30, '1994-09-18', 'Hyderabad, India', 'Female', 'Fraud', 'Chennai', 'CASE202')
    populate_database('f-018-01.jpg', 'Priya Nair', 34, '1990-11-25', 'Kochi, India', 'Female', 'Cyber Crime', 'Bangalore', 'CASE203')
    populate_database('f-024-01.jpg', 'Kavya Iyer', 26, '1998-02-14', 'Chennai, India', 'Female', 'Robbery', 'Coimbatore', 'CASE204')
    populate_database('f-030-01.jpg', 'Neha Gupta', 31, '1993-07-30', 'Jaipur, India', 'Female', 'Forgery', 'Delhi', 'CASE205')
    populate_database('f-036-01.jpg', 'Emma Watson', 34, '1990-04-15', 'London, UK', 'Female', 'Identity Theft', 'Oxford, UK', 'CASE401')
    populate_database('f-037-01.jpg', 'Maria Garcia', 29, '1995-06-20', 'Barcelona, Spain', 'Female', 'Fraud', 'Madrid, Spain', 'CASE402')
    populate_database('f-038-01.jpg', 'Li Na', 31, '1993-08-10', 'Beijing, China', 'Female', 'Cyber Crime', 'Shenzhen, China', 'CASE403')
    populate_database('f-039-01.jpg', 'Sophia Miller', 37, '1987-12-03', 'Los Angeles, USA', 'Female', 'Robbery', 'San Francisco, USA', 'CASE404')
    populate_database('f-040-01.jpg', 'Ayesha Ali', 28, '1996-01-22', 'Karachi, Pakistan', 'Female', 'Forgery', 'Islamabad, Pakistan', 'CASE405')
def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Image at path {image_path} could not be loaded.")
    img = cv2.resize(img, (300, 300))  # Resize to a standard size
    return img
def calculate_ssim(image1, image2):
    return ssim(image1, image2)
def get_image_details(filename):
    conn = sqlite3.connect('image_details.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name, age, dob, address, gender, crime_history, last_seen, case_id 
        FROM image_details WHERE filename = ?
    """, (filename,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return {
            'name': result[0],
            'age': result[1],
            'dob': result[2],
            'address': result[3],
            'gender': result[4],
            'crime_history': result[5],
            'last_seen': result[6],
            'case_id': result[7] }
    return None
@app.route('/start')
def start_page():
    return render_template('start.html')
@app.route('/upload', methods=['GET'])
def upload_page():
    return render_template('index.html')
@app.route('/create-sketch')
def create_sketch():
    return render_template('Face_Construct.html')
@app.route('/match', methods=['POST'])
def index():
    if 'sketch' not in request.files:
        return "No file part"
    file = request.files['sketch']
    if file.filename == '':
        return "No selected file"
    if file:
        sketch_filename = f"sketch_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        sketch_path = os.path.join(UPLOAD_FOLDER, sketch_filename)
        file.save(sketch_path)
        try:
            sketch = preprocess_image(sketch_path)
        except ValueError as e:
            return str(e)
        best_match = None
        best_similarity = -1
        for filename in os.listdir(PHOTO_FOLDER):
            photo_path = os.path.join(PHOTO_FOLDER, filename)
            if os.path.isfile(photo_path):
                photo = preprocess_image(photo_path)
                similarity = calculate_ssim(sketch, photo)
                if similarity > best_similarity:
                    best_similarity = similarity
                    best_match = filename
        if best_match and best_similarity > 0.6:
            image_details = get_image_details(best_match)
            result = {
                'sketch_path': sketch_filename,
                'photo_path': best_match,
                'similarity': round(best_similarity, 4),
                'details': image_details,
            }
            return render_template('result.html', result=result)
        else:
            return render_template('no_match.html', sketch=sketch_filename)
@app.errorhandler(404)
def not_found_error(error):
    return "Image not found. Please check the path and try again.", 404
if __name__ == "__main__":
    create_database()
    add_sample_data()
    app.run(debug=True)
