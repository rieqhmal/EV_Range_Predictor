import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# --- CONFIG ---
DATASET_PATH = 'EV_Energy_Consumption_Dataset_TrainingTest.csv'
MODEL_OUTPUT_PATH = "EV_Energy_Consumption_model.pkl"


# --- 1. LOAD DATA ---
print("[INFO] Loading dataset...")
try:
    df = pd.read_csv(DATASET_PATH).copy()
except FileNotFoundError:
    print(f"Error: '{DATASET_PATH}' not found.")
    exit()

# --- 2. DATA CLEANING ---
# Use the actual column names from your CSV
features = [
    'Speed_kmh', 'Acceleration_ms2', 'Battery_State_%', 'Battery_Voltage_V', 
    'Battery_Temperature_C', 'Slope_%', 'Temperature_C', 
    'Distance_Travelled_km', 'Weather_Condition'
]
target = 'Energy_Consumption_kWh' 

# Step A: Convert to numeric
for col in features + [target]:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Step B: Remove rows with missing data
initial_count = len(df)
df = df.dropna(subset=features + [target])
print(f"[INFO] Removed {initial_count - len(df)} rows with missing data.")

X = df[features]
y = df[target]

# --- 3. TRAIN/TEST SPLIT (80/20) ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"[INFO] Training set size: {len(X_train)} | Testing set size: {len(X_test)}")

# --- 4. PIPELINE SETUP ---
preprocessor = ColumnTransformer(
    transformers=[("num", "passthrough", features)],
    remainder="drop"
)

model_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1))
])

# --- 5. TRAIN & EVALUATE ---
print("[INFO] Training model...")
model_pipeline.fit(X_train, y_train)

y_pred = model_pipeline.predict(X_test)

print("\n--- PERFORMANCE (INTERNAL TEST SET) ---")
print(f"Mean Absolute Error (MAE): {mean_absolute_error(y_test, y_pred):.2f} km")
print(f"R2 Score: {r2_score(y_test, y_pred):.4f}")

# --- 6. SAVE ---
joblib.dump(model_pipeline, MODEL_OUTPUT_PATH)
print(f"[SUCCESS] Model saved to {MODEL_OUTPUT_PATH}")

# --- 7. 20% TESTING ---

# --- 1. RUN PREDICTIONS ON THE 20% TEST SET ---
y_pred = model_pipeline.predict(X_test)

# --- 2. CALCULATE METRICS ---
mae1 = mean_absolute_error(y_test, y_pred)
rmse1 = np.sqrt(mean_squared_error(y_test, y_pred))
r21 = r2_score(y_test, y_pred)

print("\n--- FINAL TEST SET PERFORMANCE (20%) ---")
print(f"Mean Absolute Error (MAE): {mae1:.2f} km")
print(f"Root Mean Squared Error (RMSE): {rmse1:.2f} km")
print(f"R2 Score (Accuracy): {r21:.4f}")

# --- 3. VISUALIZATION 1: ACTUAL VS. PREDICTED (Scatter Plot) ---
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.6, color='#2ca02c', edgecolors='k')
# Add the 1:1 reference line
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--', lw=2)

plt.xlabel("Actual Range (km)", fontsize=12)
plt.ylabel("Predicted Range (km)", fontsize=12)
plt.title("Actual vs. Predicted EV Range (Testing Set)", fontsize=14)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.show()

# --- CONFIG ---
EXTERNAL_TEST_PATH = 'External_EV_Car_Test_real.csv'
MODEL_PATH = "EV_Energy_Consumption_model.pkl"

# --- 8. EXTERNAL TESTING ---

# --- 1. LOAD THE TRAINED MODEL ---
print("[INFO] Loading the saved model...")
try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    print(f"Error: '{MODEL_PATH}' not found. Please run the training script first.")
    exit()

# --- 2. LOAD & CLEAN THE NEW DATASET ---
print(f"[INFO] Loading external test set: {EXTERNAL_TEST_PATH}")
try:
    df_new = pd.read_csv(EXTERNAL_TEST_PATH).copy()
except FileNotFoundError:
    print(f"Error: '{EXTERNAL_TEST_PATH}' not found.")
    exit()

# Features must match the training script exactly
features = ['Speed_kmh', 'Acceleration_ms2', 'Battery_State_%', 'Battery_Voltage_V', 
            'Battery_Temperature_C', 'Slope_%', 'Temperature_C', 
            'Distance_Travelled_km', 'Weather_Condition']
target = 'Energy_Consumption_kWh'  # Make sure this matches the column in your new dataset

# Step A: Convert to numeric
for col in features + [target]:
    df_new[col] = pd.to_numeric(df_new[col], errors='coerce')

# Step B: Remove incomplete rows (The "Remove Data" part)
initial_count = len(df_new)
df_new = df_new.dropna(subset=features + [target])
print(f"[INFO] Removed {initial_count - len(df_new)} rows with missing data from test set.")

X_new = df_new[features]
y_new = df_new[target]

# --- 3. PREDICT & EVALUATE ---
print("[INFO] Running predictions on new data...")
y_pred_new = model.predict(X_new)

# Results
print("\n--- EXTERNAL TEST SET PERFORMANCE ---")
print(f"Mean Absolute Error (MAE): {mean_absolute_error(y_new, y_pred_new):.2f} km")
print(f"Root Mean Squared Error (RMSE): {np.sqrt(mean_squared_error(y_test, y_pred)):.2f} km")
print(f"R2 Score (Accuracy): {r2_score(y_new, y_pred_new):.4f}")

# --- 4. VISUALIZATION ---
plt.figure(figsize=(10, 6))
plt.scatter(y_new, y_pred_new, alpha=0.6, color='#9467bd', edgecolors='k')
plt.plot([y_new.min(), y_new.max()], [y_new.min(), y_new.max()], color='red', linestyle='--', lw=2)

plt.xlabel("Actual Range (km)")
plt.ylabel("Predicted Range (km)")
plt.title(f"Performance on {EXTERNAL_TEST_PATH}")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()