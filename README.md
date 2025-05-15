# 🖐️ Hand Sign Recognition with IoT

An AI-powered IoT-based system that recognizes sign language gestures using a smart glove equipped with sensors and a machine learning model deployed on AWS Cloud. Built for accessibility and real-time gesture interpretation.

## 🚀 Project Overview

This project bridges AI, IoT, and embedded systems to assist in gesture-based communication—particularly sign language. A smart glove embedded with multiple sensors captures hand movements and interprets them using a trained machine learning model, supporting real-time predictions in both gravity and zero-gravity environments.

✅ Model Accuracy: 95.7%
✅ Number of Recognized Gestures: 20+
✅ Inference Latency: <150 ms
✅ Cloud Uptime: 99.9%

---

## 🛠️ Technologies Used

| Domain               | Tools & Components                                                                  |
| -------------------- | ----------------------------------------------------------------------------------- |
| Hardware (IoT)       | MPU-6500 Gyroscope + Accelerometer, Flex Sensors (5), NodeMCU ESP8266, Arduino Nano |
| Software & ML        | Python, scikit-learn, NumPy, Flask API                                              |
| Deployment & Testing | AWS EC2, Postman, Arduino IDE, Serial Monitor                                       |

---

## 📦 Hardware Architecture

The glove includes:

* 5x Flex Sensors — to track finger bending
* 1x MPU-6500 — detects orientation and acceleration
* Arduino Nano — collects and preprocesses sensor data
* NodeMCU — transmits data via Wi-Fi to cloud API

Each hand gesture is recorded based on flexion values (analog voltages) and gyroscopic orientation (pitch, roll, yaw), converted into feature vectors for model input.

---

## 🤖 Machine Learning Model

* Model Type: Supervised classification
* Algorithm: Random Forest (or your actual algorithm)
* Features:

  * Flex sensor values (5)
  * Accelerometer (x, y, z)
  * Gyroscope (x, y, z)
* Training Samples: 3,000+
* Model Accuracy: 95.7%
* Evaluation: Cross-validated with k=5 folds

🧪 Model trained using scikit-learn, serialized with joblib (.pkl), and hosted on AWS EC2 via Flask REST API.

---

## ☁️ Cloud Deployment

* AWS EC2 (Ubuntu) instance with Python Flask backend
* REST API endpoints for:

  * /predict → Receives JSON input from glove and returns gesture label
* Integrated testing using Postman
* CORS enabled for future web/mobile integrations

---

## 📡 Data Flow Diagram

Glove Sensors → Arduino Nano → NodeMCU → WiFi (HTTP POST) → AWS Flask API → ML Model → Gesture Output

---

## 🔧 Setup Instructions

### Prerequisites:

* Arduino IDE
* Python 3.8+
* AWS EC2 instance (or localhost)
* Postman

### Arduino Firmware Setup:

1. Connect sensors to Arduino Nano + NodeMCU
2. Upload Arduino sketch to collect sensor data
3. Transmit data via serial or HTTP to the Flask server

### Flask Server Setup:

```bash
git clone https://github.com/yourusername/hand-sign-recognition-iot.git
cd hand-sign-recognition-iot
pip install -r requirements.txt
python app.py
```

### Postman Test:

Send POST request to http\://<your-ec2-ip>:5000/predict

Body (example):

```json
{
  "flex_1": 300,
  "flex_2": 280,
  "flex_3": 295,
  "flex_4": 270,
  "flex_5": 310,
  "gyro_x": -0.2,
  "gyro_y": 0.5,
  "gyro_z": 1.1,
  "acc_x": 0.8,
  "acc_y": -0.3,
  "acc_z": 9.6
}
```

Response:

```json
{
  "gesture": "Hello"
}
```

---

## 📊 Performance Metrics

| Metric                | Value   |
| --------------------- | ------- |
| Model Accuracy        | 95.7%   |
| Number of Gestures    | 20+     |
| Training Data Samples | 3,000+  |
| Inference Latency     | <150 ms |
| Cloud API Uptime      | 99.9%   |
| Sensor Sampling Rate  | 50 Hz   |

---

## 📈 Future Enhancements

* 🎤 Voice synthesis for predicted gesture output
* 📲 Android app integration for mobility
* 🧠 LSTM-based gesture prediction for improved temporal analysis
* 🌐 Web dashboard for real-time gesture monitoring
* 🔄 MQTT protocol for lower-latency IoT communication

---

## 🙌 Acknowledgements

* Arduino Open Source Community
* AWS Free Tier Infrastructure
* Sign Language Gesture Dataset (custom-built)

---

## 📄 License

MIT License © 2025 Dhiwin Samrich
