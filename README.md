# EV Digital Twin with AI-Based Range Prediction

An intelligent Electric Vehicle (EV) Digital Twin built using NVIDIA Omniverse, Machine Learning, and a real-time web dashboard. This project combines AI-powered EV range prediction with immersive 3D simulation to create a real-time virtual representation of an electric vehicle system.

---

# 📌 Project Overview

This project demonstrates the integration of:

- Machine Learning for EV energy consumption and range prediction
- Real-time Digital Twin simulation using NVIDIA Omniverse
- Interactive HTML dashboard for live parameter control
- Bidirectional communication between the dashboard and Omniverse
- Action Graph pipeline for simulation automation and visualization

The system predicts EV energy consumption and estimated driving range based on parameters such as:

- Speed
- Acceleration
- Battery State
- Battery Voltage
- Battery Temperature
- Road Slope
- Ambient Temperature
- Distance Travelled
- Weather Condition

The prediction results are visualized live inside the Omniverse 3D environment and the web dashboard simultaneously.

---

# 🚀 Features

## ✅ AI-Based EV Range Prediction
- Random Forest Regression model
- Real-time inference using trained `.pkl` model
- Predicts:
  - Energy Consumption (kWh)
  - Estimated Driving Range (km)

## ✅ NVIDIA Omniverse Digital Twin
- Real-time 3D EV simulation
- Interactive Action Graph pipeline
- Procedural wheel animation
- Dynamic UI updates inside viewport

## ✅ Interactive Web Dashboard
- Real-time telemetry visualization
- Adjustable EV parameters
- Live synchronization with Omniverse
- Circular gauges and progress bars

## ✅ Real-Time Communication
- HTTP/WebSocket-based synchronization
- Low-latency local integration
- Continuous dashboard updates

---

# 🏗️ System Architecture

```text
HTML Dashboard
       ⇅
Python Flask Server
       ⇅
NVIDIA Omniverse
       ⇅
Machine Learning Model (.pkl)
```

## Workflow

1. User changes EV parameters on the dashboard
2. Parameters are sent to Omniverse
3. Omniverse passes data into the ML model
4. AI predicts energy consumption and range
5. Results are updated live in:
   - Omniverse Digital Twin
   - Web Dashboard

---

# 🧠 Machine Learning Model

## Model Used
- Random Forest Regressor

## Input Features
- Speed (km/h)
- Acceleration (m/s²)
- Battery State (%)
- Battery Voltage (V)
- Battery Temperature (°C)
- Road Slope (%)
- Ambient Temperature (°C)
- Distance Travelled (km)
- Weather Condition

## Output
- Energy Consumption (kWh)

## Evaluation Metrics
- MAE
- RMSE
- R² Score

---

# 🖥️ Technologies Used

## Programming & Frameworks
- Python 3.10+
- HTML5
- CSS3
- JavaScript (ES6+)

## Machine Learning Libraries
- scikit-learn
- pandas
- numpy
- joblib

## Simulation Platform
- NVIDIA Omniverse
- Omni.UI
- PhysX
- Action Graph

## Development Tools
- Visual Studio Code
- Flask Server

---

# 💻 System Requirements

## Hardware
| Component | Requirement |
|---|---|
| GPU | NVIDIA RTX 2060 or higher |
| CPU | Quad-core Intel/AMD |
| RAM | Minimum 16GB |
| Storage | 25GB free space |

## Software
- Windows 10/11 or Linux
- Python 3.10+
- NVIDIA Omniverse Kit App Template
- Visual Studio Code

---

# 📂 Project Structure

```bash
EV-Digital-Twin/
│
├── app.py
├── model/
│   └── ev_model.pkl
│
├── dashboard/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── omniverse/
│   ├── DTProject.usd
│   ├── action_graph/
│   └── scripts/
│
├── dataset/
│   ├── training_data.csv
│   └── test_data.csv
│
├── assets/
│   └── 3D models
│
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/ev-digital-twin.git
cd ev-digital-twin
```

## 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

## 3. Install NVIDIA Omniverse Kit App Template

GitHub Repository:

https://github.com/NVIDIA-Omniverse/kit-app-template

Follow the installation guide provided by NVIDIA.

---

# ▶️ Running the Project

## Step 1 — Start Flask Server

```bash
python app.py
```

Keep the terminal running.

---

## Step 2 — Launch Omniverse

Open the Omniverse project:

```text
DTProject.usd
```

Press **Play** to start the simulation.

---

## Step 3 — Find Your IPv4 Address

Windows:

```bash
ipconfig
```

Copy your IPv4 address.

---

## Step 4 — Open Dashboard

Open browser:

```text
http://YOUR_IP_ADDRESS:5000
```

Example:

```text
http://192.168.0.5:5000
```

---

# 🎮 Dashboard Features

## Input Controls
- Speed
- Acceleration
- Battery State
- Temperature
- Road Slope
- Weather Condition

## Live Outputs
- Predicted Range
- Energy Consumption
- Battery Health
- Efficiency Score

---

# 🔄 Omniverse Action Graph Pipeline

The Action Graph consists of:

| Node | Function |
|---|---|
| On Tick Node | Synchronization engine |
| Receiver Node | Receives dashboard data |
| ML Inference Node | Executes AI prediction |
| Wheel Spinner Node | Calculates wheel rotation |
| Dashboard UI Node | Updates viewport HUD |
| Write Prim Attribute Nodes | Controls wheel mesh rotation |

---

# 📸 Key Capabilities

- Real-time EV simulation
- AI-powered prediction
- Dynamic 3D visualization
- Interactive dashboard controls
- Live synchronization
- Procedural wheel animation

---

# 🔮 Future Improvements

## Planned Enhancements
- XGBoost / LSTM model support
- Firebase cloud database integration
- Historical analytics dashboard
- Predictive maintenance system
- AR visualization support
- Multi-user collaborative simulation
- Vehicle-specific training datasets

---

# 👨‍💻 Contributors

- Muhamamad Rieqhmal Mukhreez bin Rozmi
- Muhammad Isfahann Syakir bin Shahrum
- Nor Diana binti Aziz

---

# 📜 License

This project is intended for educational and research purposes.

---

# 🙏 Acknowledgements

- NVIDIA Omniverse
- Scikit-learn
- Pandas
- NumPy
- Flask
