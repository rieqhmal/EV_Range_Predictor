# 🏎️ Real-Time EV Telemetry & Digital Twin Dashboard

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![MQTT](https://img.shields.io/badge/MQTT-HiveMQ-yellow.svg)
![Firebase](https://img.shields.io/badge/Firebase-Hosting%20%7C%20DB-orange.svg)
![Omniverse](https://img.shields.io/badge/NVIDIA-Omniverse-brightgreen.svg)
![Machine Learning](https://img.shields.io/badge/Scikit--Learn-ML-red.svg)

A full-stack Internet of Things (IoT) and Digital Twin project that streams live electric vehicle (EV) physics data from a 3D simulation into a real-time predictive machine learning model, broadcasting the results to a modern web dashboard.

## 🚀 Overview

This project bridges the gap between high-fidelity 3D simulation and real-world IoT telemetry. Using **NVIDIA Omniverse** as the simulation engine, live physics data (speed, acceleration, battery state, environment) is fed into a custom **Scikit-Learn** machine learning model to dynamically predict energy consumption and remaining range.

The predictions are published via **HiveMQ (MQTT)** to a **Firebase-hosted** web dashboard, providing a sub-second, real-time monitoring interface.

## ✨ Key Features

* **Real-Time ML Inference in 3D:** Custom Python OmniGraph nodes process continuous physics streams and predict energy consumption without dropping simulation frame rates (utilizing thread-limiting optimizations).
* **High-Throughput IoT Pipeline:** Integrates a secure MQTT broker (HiveMQ Cloud) to handle bi-directional telemetry data.
* **Smart WebSocket Management:** The web client utilizes the browser's native `Page Visibility API` to intelligently connect/disconnect from the MQTT broker, saving bandwidth and battery when the tab is inactive.
* **Modern Web Dashboard:** Features smooth data transitions, rolling number animations, and a live spline chart for historical energy monitoring.

## 🏗️ Architecture & Tech Stack

1. **Simulation Engine:** NVIDIA Omniverse (OmniGraph, Python Scripting)
2. **Machine Learning:** Python, Scikit-Learn, Pandas, Joblib
3. **IoT / Messaging:** HiveMQ Cloud (MQTT over WebSockets, TLS)
4. **Frontend Dashboard:** HTML/JS/CSS, Chart.js (or equivalent), MQTT.js
5. **Backend / Hosting:** Google Firebase (Hosting & Realtime DB/Firestore)

## ⚙️ Prerequisites

To run this project locally, you will need:
* **NVIDIA Omniverse** (Create or Code) with the OmniGraph extension enabled.
* **Python 3.10+** (Ensure `paho-mqtt`, `scikit-learn`, and `pandas` are installed in your Omniverse Python environment).
* A free **HiveMQ Cloud** cluster (for the MQTT broker).
* A **Firebase** project setup for hosting.

## 🛠️ Installation & Setup

### 1. The Machine Learning Model
1. Place the `EV_Energy_Consumption_model.pkl` file in your designated local directory.
2. Update the `model_path` variable inside the Omniverse script node to point to this file.

### 2. NVIDIA Omniverse Configuration
1. Open the `.usd` stage provided in the `omniverse/` folder.
2. Navigate to the **Action Graph**.
3. Ensure the custom Python Script Node has the correct HiveMQ broker URL, port (8883/8884), username, and password.

### 3. Web Dashboard Setup
1. Navigate to the `web/` directory.
2. Update the MQTT connection variables in `app.js` with your HiveMQ WebSocket credentials.
3. Deploy to Firebase:
   ```bash
   firebase login
   firebase init
   firebase deploy --only hosting
