# 🔥 Calorie Burnt Predictor AI System

A production-ready Machine Learning application that predicts the number of calories burned during exercise using physiological and workout-related features.

This project demonstrates the complete AI/ML lifecycle, including data preprocessing, feature engineering, model training, model explainability, API development, database integration, frontend development, testing, containerization, and deployment.

---

# 📌 Project Overview

The objective of this project is to build an intelligent calorie prediction system that estimates calories burned during exercise based on user information and workout metrics.

The system uses Machine Learning to analyze patterns in exercise data and generate accurate calorie-burn predictions.

### Input Features

* Gender
* Age
* Height
* Weight
* Duration
* Heart Rate
* Body Temperature

### Output

* Predicted Calories Burned

---

# 🏗️ System Architecture

```text
User
   │
   ▼
Streamlit Frontend
   │
   ▼
FastAPI Backend
   │
   ▼
Prediction Pipeline
   │
   ▼
XGBoost Model
   │
   ▼
PostgreSQL Database
```

---

# 🚀 Features

* End-to-End Machine Learning Pipeline
* Data Cleaning and Preprocessing
* Feature Engineering
* Model Training and Evaluation
* XGBoost Prediction Model
* FastAPI REST API
* PostgreSQL Integration
* Streamlit Frontend
* Docker Containerization
* Docker Compose Orchestration
* Automated Testing with Pytest
* GitHub Version Control
* CI/CD Ready Architecture

---

# 🧠 Machine Learning Workflow

## Data Collection

Exercise and calorie datasets were collected and merged for training.

## Data Analysis

Performed:

* Missing Value Analysis
* Duplicate Detection
* Statistical Analysis
* Correlation Analysis

## Feature Engineering

Created additional features and prepared data for model training.

## Models Evaluated

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor
* XGBoost Regressor

## Final Model

XGBoost Regressor was selected as the final model due to superior performance.

---

# 🛠️ Technology Stack

### Programming

* Python

### Data Science

* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* SHAP

### Backend

* FastAPI
* Uvicorn

### Frontend

* Streamlit

### Database

* PostgreSQL
* SQLAlchemy

### Testing

* Pytest

### DevOps

* Docker
* Docker Compose
* GitHub Actions

### MLOps

* MLflow
* DVC

---

# 📂 Project Structure

```text
calorie-burnt-predictor/
│
├── app/
├── src/
├── frontend/
├── tests/
├── data/
├── models/
│
├── Dockerfile
├── Dockerfile.streamlit
├── docker-compose.yml
├── requirements.txt
├── README.md
│
└── .github/
```

---

# ⚙️ Local Installation

## Clone Repository

```bash
git clone https://github.com/The-Techie-Girl/calorie-burnt-predictor.git

cd calorie-burnt-predictor
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Backend

```bash
uvicorn app.main:app --reload
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Frontend

```bash
streamlit run frontend/streamlit_app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# 🐳 Docker Setup

Build Containers

```bash
docker compose build
```

Start Containers

```bash
docker compose up
```

Stop Containers

```bash
docker compose down
```

---

# 🔌 API Endpoints

## Home

```http
GET /
```

## Prediction

```http
POST /predict
```

Example Request:

```json
{
  "Gender": "male",
  "Age": 25,
  "Height": 175,
  "Weight": 70,
  "Duration": 30,
  "Heart_Rate": 120,
  "Body_Temp": 38.5
}
```

---

# ✅ Testing

Run all tests:

```bash
pytest
```

Current Test Coverage:

* API Tests
* Model Loading Tests
* Prediction Pipeline Tests

---

# 📊 Future Improvements

* Cloud Deployment
* User Authentication
* Real-Time Monitoring
* MLflow Experiment Tracking
* DVC Data Versioning
* Model Explainability Dashboard
* Kubernetes Deployment

---

# 👩‍💻 Author

GitHub: https://github.com/The-Techie-Girl

---

# ⭐ Project Goal

This project was built as a portfolio-ready AI/ML Engineering project demonstrating:

* Machine Learning
* Backend Development
* Frontend Development
* Databases
* Testing
* Docker
* MLOps
* Deployment
