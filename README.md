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

<img width="1916" height="964" alt="Screenshot 2026-04-27 170635" src="https://github.com/user-attachments/assets/0d1a8bb0-1b6d-4b8d-9030-bfe0c0ab253f" />

### Login & OTP Verification
<img width="821" height="405" alt="image" src="https://github.com/user-attachments/assets/25ec39e5-ab61-4664-b95d-6f1e4cd0dd8a" />

<img width="1908" height="960" alt="Screenshot 2026-04-27 171036" src="https://github.com/user-attachments/assets/2962bffb-067c-4b16-8f3b-bae54024bf7a" />


### Face Sketch Construction

<img width="1914" height="954" alt="Screenshot 2026-04-27 172749" src="https://github.com/user-attachments/assets/e8674ad2-261b-4a74-a0a6-06080d6954f0" />

### Upload Sketch
<img width="1915" height="962" alt="Screenshot 2026-04-27 173353" src="https://github.com/user-attachments/assets/d40a4cd8-3e08-4ff7-8542-5dfad7f12852" />

### Match Result
<img width="1894" height="960" alt="Screenshot 2026-04-27 174032" src="https://github.com/user-attachments/assets/c90087dc-9cd8-4214-9938-9dd8891a501c" />


### No Match Found

<img width="1906" height="950" alt="Screenshot 2026-04-27 173441" src="https://github.com/user-attachments/assets/ee008a1a-350c-4796-8b9c-292f8f8b4ca0" />


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
