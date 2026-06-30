# ==============================
# Student Performance Predictor
# Train ML Model
# ==============================

# Import Libraries
import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ==============================
# Load Dataset
# ==============================

df = pd.read_csv("data/students.csv")

print("First 5 Rows")
print(df.head())

# ==============================
# Explore Dataset
# ==============================

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# ==============================
# Data Visualization
# ==============================

plt.scatter(df["Hours_Studied"], df["Final_Marks"])

plt.xlabel("Hours Studied")
plt.ylabel("Final Marks")
plt.title("Hours Studied vs Final Marks")

plt.show()

# ==============================
# Select Features (X)
# ==============================

X = df[[
    "Hours_Studied",
    "Sleep_Hours",
    "Attendance",
    "Previous_Marks"
]]

# ==============================
# Select Target (y)
# ==============================

y = df["Final_Marks"]

# ==============================
# Split Dataset
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

# ==============================
# Create Linear Regression Model
# ==============================

model = LinearRegression()

# ==============================
# Train Model
# ==============================

model.fit(X_train, y_train)

print("\nModel Trained Successfully!")

# ==============================
# Make Predictions
# ==============================

y_pred = model.predict(X_test)

print("\nPredicted Marks:")
print(y_pred)

# ==============================
# Compare Predictions
# ==============================

comparison = pd.DataFrame({
    "Actual Marks": y_test.values,
    "Predicted Marks": y_pred
})

print("\nComparison Table")
print(comparison)

# ==============================
# Evaluate Model
# ==============================

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation")

print("Mean Absolute Error :", mae)
print("Mean Squared Error  :", mse)
print("R2 Score            :", r2)


# ==============================
# Predict New Student
# ==============================

new_student = pd.DataFrame({
    "Hours_Studied": [7],
    "Sleep_Hours": [8],
    "Attendance": [94],
    "Previous_Marks": [78]
})

prediction = model.predict(new_student)

print("\nNew Student Details")

print("Hours Studied :", 7)
print("Sleep Hours   :", 8)
print("Attendance    :", 94)
print("Previous Marks:", 78)

print("\nPredicted Final Marks:", round(prediction[0], 2))

# ==============================
# Save Trained Model
# ==============================

os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/student_model.pkl")

print("\n✅ Model saved successfully!")