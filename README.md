# 🎓 Student Performance Predictor

A Machine Learning web application that predicts a student's final exam score based on their study habits and academic performance.

Built with **Python, Flask, Scikit-learn, and Pandas**, this project demonstrates the complete machine learning workflow—from data preprocessing and model training to deployment through a web application.

---

## 🚀 Features

* 📈 Predicts a student's final marks using Machine Learning
* 📝 User-friendly web interface built with Flask
* ⚡ Instant predictions based on user inputs
* 🎯 Uses a trained Linear Regression model
* 💾 Loads the trained model using Joblib

---

## 📊 Input Parameters

The prediction is based on the following features:

* 📚 Hours Studied
* 😴 Sleep Hours
* 🏫 Attendance Percentage
* 📖 Previous Marks

---

## 🤖 Machine Learning Model

**Algorithm:** Linear Regression

### Workflow

* Data Collection
* Data Preprocessing
* Train-Test Split
* Model Training
* Model Evaluation
* Model Serialization using Joblib
* Deployment with Flask

### Evaluation Metrics

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

---

## 🛠️ Tech Stack

| Category             | Technologies  |
| -------------------- | ------------- |
| Programming Language | Python        |
| Backend              | Flask         |
| Machine Learning     | Scikit-learn  |
| Data Processing      | Pandas, NumPy |
| Frontend             | HTML, CSS     |
| Model Storage        | Joblib        |

---

## 📂 Project Structure

```text
Student-Performance-Predictor/
│
├── app.py
├── model.pkl
├── train_model.py
├── student_data.csv
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/maithilipandey/student-performance-predictor.git
```

Navigate to the project folder:

```bash
cd student-performance-predictor
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🎯 Future Improvements

* Add multiple ML algorithms for comparison
* Improve prediction accuracy with larger datasets
* Store prediction history in a database
* User authentication
* Deploy on Render or Railway
* Interactive charts for performance analysis

---

## 📚 Learning Outcomes

Through this project, I learned:

* Building an end-to-end Machine Learning pipeline
* Training and evaluating regression models
* Deploying ML models using Flask
* Data preprocessing and feature engineering
* Integrating Machine Learning with web development

---

## 👩‍💻 Author

**Maithili Pandey**

If you found this project useful, feel free to ⭐ the repository!

