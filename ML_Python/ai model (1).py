import joblib
import pandas as pd

# --- 1. LOAD THE MODEL ---
MODEL_PATH = "EV_Energy_Consumption_model.pkl"
try:
    model = joblib.load(MODEL_PATH)
    print("✅ Model loaded successfully!")
except FileNotFoundError:
    print(f"❌ Error: '{MODEL_PATH}' not found. Run your training script first.")
    exit()

# --- 2. GET USER INPUT VIA TERMINAL ---
print("\n--- EV Energy Consumption Predictor ---")
print("Enter the car details below:")

try:
    speed = float(input("Speed (km/h): "))
    acceleration = float(input("Acceleration (m/s²): "))
    battery_state = float(input("Battery State of Charge (%): "))
    battery_voltage = float(input("Battery Voltage (V): "))
    battery_temp = float(input("Battery Temperature (°C): "))
    slope = float(input("Slope (%): "))
    temp = float(input("Ambient Temperature (°C): "))
    distance = float(input("Distance Travelled (km): "))
    weather_condition = float(input("Weather Condition (1=Clear, 2=Rainy, 3=Snowy, 4=Foggy): "))


    # --- 3. FORMAT DATA FOR THE MODEL ---
    # The columns must match your training features EXACTLY
    input_data = pd.DataFrame([{
        'Speed_kmh': speed,
        'Acceleration_ms2': acceleration,
        'Battery_State_%': battery_state,
        'Battery_Voltage_V': battery_voltage,
        'Battery_Temperature_C': battery_temp,
        'Slope_%': slope,
        'Temperature_C': temp,
        'Distance_Travelled_km': distance,
        'Weather_Condition': weather_condition
    }])


    # --- 4. PREDICT ---
    prediction = model.predict(input_data)
    
    print("-" * 30)
    print(f"🚀 Predicted Energy Consumption: {prediction[0]:.2f} kWh")
    print("-" * 30)

except ValueError:
    print("❌ Error: Please enter numbers only.")