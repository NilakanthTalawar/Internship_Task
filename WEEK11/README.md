# 🎓 Smart Attendance System using Face Recognition

<p align="center">

<!-- SVG Badge Icons -->

<img src="https://img.shields.io/badge/Python-3.10-blue.svg"/>
<img src="https://img.shields.io/badge/Streamlit-UI-red.svg"/>
<img src="https://img.shields.io/badge/OpenCV-FaceDetection-green.svg"/>
<img src="https://img.shields.io/badge/FaceRecognition-AI-orange.svg"/>
<img src="https://img.shields.io/badge/Status-Active-success.svg"/>

</p>

---

## 📌 Overview

The **Smart Attendance System** is an AI-powered application that automatically records attendance using **Face Recognition technology**.

Instead of manual attendance systems, the application detects and recognizes student faces through a **webcam** and logs attendance automatically.

The system is built using **Python, OpenCV, Face Recognition, and Streamlit**, making it simple, fast, and efficient for educational institutions.

---

## ✨ Features

✔ Student Registration
✔ Capture Student Face Images
✔ Train Face Recognition Model
✔ Automatic Face Detection
✔ Real-time Face Recognition
✔ Automatic Attendance Logging
✔ Attendance Viewer Dashboard
✔ Clean Streamlit Interface

---

## 🧠 How It Works

The system follows this workflow:

```
Student enters details
        ↓
Capture Face Images (50 frames)
        ↓
Train Face Recognition Model
        ↓
Start Attendance System
        ↓
Face Recognition via Webcam
        ↓
Attendance stored in CSV file
```

---

## 🏗️ Project Structure

```
smart_attendence_sys/
│
├── app.py
│
├── backend
│   ├── capture_faces.py
│   ├── train_model.py
│   └── recognize_face.py
│
├── dataset
│   └── student_images
│
├── models
│   └── face_model.pkl
│
├── attendance
│   └── attendance.csv
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Musa-04/smart_attendence_sys
cd smart-attendance-system
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the browser:

```
http://localhost:8501
```

---

## 🧑‍🎓 Usage Guide

### 1️⃣ Register Student

Enter the following details:

* Student Name
* USN
* Roll Number
* Class

Click **Capture Faces** to capture **50 face images**.

---

### 2️⃣ Train Model

Click **Train Model** to train the facial recognition system.

During training, the terminal will display logs like:

```
Processing: image_1.jpg
Processing: image_2.jpg
Processing: image_3.jpg
...
Model updated successfully
```

---

### 3️⃣ Start Attendance

Click **Start Attendance**.

The webcam will start detecting faces and mark attendance automatically.

---

### 4️⃣ View Attendance

Click **View Attendance** to display the attendance records stored in:

```
attendance/attendance.csv
```

Example:

```
Name,Time
Mustafeez,09:05:11
Rahul,09:06:03
```

---

## 🛠️ Technologies Used

| Technology       | Purpose                  |
| ---------------- | ------------------------ |
| Python           | Backend Programming      |
| OpenCV           | Face Detection           |
| face_recognition | Face Encoding            |
| Streamlit        | Web UI                   |
| NumPy            | Numerical Operations     |
| Pandas           | Attendance Data Handling |

---

## 📊 Future Improvements

Planned enhancements for the system:

* Login Authentication System
* Student Database (SQLite / MySQL)
* Attendance Analytics Dashboard
* Real-time Camera Feed inside UI
* Cloud Deployment
* Mobile Access

---

## 👨‍💻 Author

**Mustafeez**

Computer Science Student
Passionate about **AI, Computer Vision, and Software Development**

---

## 📜 License

This project is created for **educational and research purposes**.

---

<p align="center">

⭐ If you like this project, consider giving it a **star** on GitHub!

</p>
