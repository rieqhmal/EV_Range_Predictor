from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# This dictionary stores our data in memory
data_store = {
    "inputs": {
        "Speed_kmh": 0.0, 
        "Acceleration_ms2": 0.0, 
        "Battery_State_%": 0.0,
        "Battery_Voltage_V": 0.0, 
        "Battery_Temperature_C": 0.0, 
        "Slope_%": 0.0,
        "Temperature_C": 0.0, 
        "Distance_Travelled_km": 0.0, 
        "Weather_Condition": 0,
        "Total_Battery_Capacity_kWh": 0.0 # Added this since your script uses it
    },
    "outputs": {
        "Predicted_Range_km": 0.0,
        "Energy_Consumption_kWh": 0.0
    }
}

@app.route('/')
def index():
    # This serves your HTML page
    return render_template('index.html')

@app.route('/api/data', methods=['GET', 'POST'])
def data_api():
    if request.method == 'POST':
        req_data = request.json
        if 'inputs' in req_data:
            data_store['inputs'].update(req_data['inputs'])
        if 'outputs' in req_data:
            data_store['outputs'].update(req_data['outputs'])
        return jsonify({"status": "success"})
    
    # If it's a GET request, send the current data
    return jsonify(data_store)

if __name__ == '__main__':
    # Runs the server on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)