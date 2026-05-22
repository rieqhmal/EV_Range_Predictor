# 🏎️ Real-Time EV Digital Twin & Range Predictor

An interactive Digital Twin framework designed to create a real-time virtual replica of an electric vehicle (EV) using NVIDIA Omniverse. This system leverages a trained machine learning model to generate accurate predictions of the vehicle's driving range based on dynamic physics and environmental data. 

## 🚀 Overview

This iteration of the project transitions from a cloud-dependent architecture to a direct local integration between a Web Dashboard and NVIDIA Omniverse. Serving as the primary user interface, an HTML Web application replaces the previously used mobile and database pipelines. A local Python Flask server acts as the communication bridge, significantly reducing latency for real-time digital twin synchronization.

## ✨ Key Features

* **Real-Time ML Inference:** Utilizes a Random Forest Regression model, serialized via Joblib, to process input data and predict energy consumption without retraining.
* **Omniverse Action Graph:** Employs a node-based execution framework to synchronize the 3D rendering pipeline with external web inputs and ML predictions.
* **Local Web Dashboard:** A responsive HTML5/CSS3/JavaScript interface designed like an industrial HMI, allowing bidirectional control of EV parameters (e.g., speed, temperature, road slope).
* **Dynamic 3D Actuation:** Mathematical nodes translate scalar velocity into continuous rotational vectors, forcefully updating the `xformOp:rotateXYZ` attributes to spin the 3D vehicle's wheels in real-time.

## 🏗️ Architecture & Tech Stack

* **Simulation Engine:** NVIDIA Omniverse Kit App Template (USD Composer, PhysX, Omni.UI, Action Graph)
* **Backend Server:** Python 3.10+ running a local Flask server (`app.py`)
* **Machine Learning:** Scikit-Learn, Pandas, NumPy, Joblib
* **Frontend:** HTML5, CSS3, ES6+ JavaScript, Fetch API/WebSockets

## ⚙️ Prerequisites

To run this project locally, you will need:
* **GPU:** Minimum NVIDIA RTX 2060
* **Memory:** Minimum 16 GB RAM and 25 GB free storage
* **Software:** Windows 10/11 or Linux, Python 3.10+, and NVIDIA Omniverse installed via the GitHub developer template.

## 🛠️ Installation & Execution

### 1. Start the Local Server
1. Navigate to the `webapp` directory containing the `app.py` file.
2. Open your terminal and run the Flask server:
   ```bash
   python app.py
