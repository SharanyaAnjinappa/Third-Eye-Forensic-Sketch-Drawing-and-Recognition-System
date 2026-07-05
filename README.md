# Third-Eye-Forensic-Sketch-Drawing-and-Recognition-System
A web-based forensic face sketch construction and recognition system that enables users to create or upload suspect sketches and compare them with a criminal database using OpenCV and SSIM.
# Third Eye – Forensic Face Sketch Construction and Recognition System

## Overview

**Third Eye** is a web-based forensic face sketch construction and recognition system developed to assist law enforcement agencies in suspect identification. The application allows authorized users to create facial sketches using an interactive drag-and-drop interface or upload an existing sketch for comparison against a criminal database.

The system performs image preprocessing and similarity matching using OpenCV and the Structural Similarity Index (SSIM), then retrieves the details of the closest matching record from the database.

---

## Features

- 🔐 Secure OTP-based user authentication
- 🎨 Interactive face sketch construction using drag-and-drop facial features
- 📤 Upload existing facial sketches for comparison
- 🖼️ Image preprocessing using OpenCV
- 📊 Face matching using Structural Similarity Index (SSIM)
- 🗃️ Criminal database integration using SQLite
- 📄 Displays suspect details including name, age, crime history, address, case ID, and similarity score
- 🌐 Web-based interface built with Flask

---

## Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Image Processing
- OpenCV
- scikit-image (SSIM)
- NumPy

### Database
- SQLite

### Authentication
- OTP verification using SMTP (Gmail)

---

## Installation

### Prerequisites

- Python 3.11.6 or later

Install the required packages:

```bash
pip install flask
pip install opencv-python
pip install numpy
pip install pillow
pip install scikit-image
```

---

## Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Third-Eye-Forensic-Face-Sketch-Recognition.git

cd Third-Eye-Forensic-Face-Sketch-Recognition
```

---

## Create a Virtual Environment (Optional)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

---

## Run the Application

```bash
python app.py
```

---

## Open in Browser

```
http://127.0.0.1:5000/
```

---

## Project Workflow

1. Launch the application.
2. Login using your email.
3. Verify your identity using the OTP.
4. Choose one of the following options:
   - Create a facial sketch
   - Upload an existing sketch
5. The system preprocesses the image.
6. SSIM compares the sketch with images stored in the criminal database.
7. If the similarity score exceeds the threshold, the system displays the best match and criminal details.
8. Otherwise, a "No Match Found" message is displayed.

---

## Project Structure

```
project/
│
├── static/
│   ├── assets/
│   ├── photos/
│   ├── uploads/
│
├── templates/
│   ├── landing.html
│   ├── login.html
│   ├── verify.html
│   ├── start.html
│   ├── Face_Construct.html
│   ├── index.html
│   ├── result.html
│   └── no_match.html
│
├── image_details.db
├── app.py
└── README.md
```

---

## Screenshots

### Landing Page

*(Add screenshot here)*

### Login & OTP Verification

*(Add screenshot here)*

### Face Sketch Construction

*(Add screenshot here)*

### Upload Sketch

*(Add screenshot here)*

### Match Result

*(Add screenshot here)*

### No Match Found

*(Add screenshot here)*

---

## Future Enhancements

- Integrate CNN-based face recognition models.
- Improve recognition accuracy using deep learning.
- Add real-time webcam support.
- Expand the criminal image database.
- Deploy the application on cloud platforms such as AWS or Google Cloud.
- Implement role-based authentication for different users.

---

## Author

**Sharanya A**

B.Tech – Computer Science and Engineering

Dayananda Sagar University
