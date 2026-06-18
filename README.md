# 📈 Sales Prediction API using Machine Learning & FastAPI

## Overview

Sales forecasting is one of the most important tasks for businesses. Accurate predictions help companies optimize marketing budgets, manage inventory efficiently, and make data-driven decisions.

This project demonstrates a complete Machine Learning workflow, from model training to deployment as a REST API using FastAPI.

The API predicts expected sales based on advertising expenditure and returns the forecast instantly through a simple endpoint.

---

## Features

* Machine Learning-based sales prediction
* REST API built with FastAPI
* Trained and serialized model using Joblib
* Interactive API documentation with Swagger UI
* JSON-based request and response handling
* Lightweight and beginner-friendly implementation
* Easy to deploy and extend

---

## Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy
* Joblib

### Development Tools

* VS Code
* Git
* GitHub

---

## Project Structure

```bash
sales-prediction-api/
│
├── app.py
├── train_model.py
├── sales_prediction_model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

| File                       | Purpose                  |
| -------------------------- | ------------------------ |
| app.py                     | FastAPI application      |
| train_model.py             | Model training script    |
| sales_prediction_model.pkl | Saved trained model      |
| requirements.txt           | Project dependencies     |
| README.md                  | Project documentation    |
| .gitignore                 | Ignore unnecessary files |

---

## Machine Learning Workflow

### Data Collection

The dataset contains historical information relating advertising expenditure to generated sales.

Example:

| Ad Spend | Sales |
| -------- | ----- |
| 1000     | 5000  |
| 2000     | 9000  |
| 3000     | 13000 |

---

### Data Preprocessing

The dataset is cleaned and prepared before training:

* Missing value handling
* Feature selection
* Data transformation
* Model-ready formatting

---

### Model Training

A regression model is trained to learn the relationship between advertising spend and sales revenue.

Example:

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
```

---

### Model Serialization

After training, the model is saved using Joblib.

```python
import joblib

joblib.dump(model, "sales_prediction_model.pkl")
```

This allows predictions without retraining every time.

---

## API Endpoints

### Home Endpoint

```http
GET /
```

Response:

```json
{
  "message": "Sales Prediction API is running"
}
```

---

### Prediction Endpoint

```http
POST /predict
```

Request Body:

```json
{
  "AdSpend": 5000
}
```

Response:

```json
{
  "PredictedSales": 24785.65
}
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/sales-prediction-api.git
```

### Move Into Project Directory

```bash
cd sales-prediction-api
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```text
http://127.0.0.1:8000/redoc
```

---

## Testing with Swagger UI

1. Open `/docs`
2. Click POST `/predict`
3. Click "Try it out"
4. Enter:

```json
{
  "AdSpend": 5000
}
```

5. Click Execute

The API will return the predicted sales value.

---

## Example Use Cases

* Retail sales forecasting
* Marketing budget planning
* Revenue estimation
* Business analytics dashboards
* Learning FastAPI deployment
* Learning ML model serving

---

## Future Improvements

* Multiple input features
* Real-world datasets
* Model performance metrics
* Database integration
* Docker containerization
* Cloud deployment
* Authentication and authorization
* Frontend dashboard integration

---

## Learning Outcomes

Through this project, I learned:

* Machine Learning model training
* Regression algorithms
* Model serialization using Joblib
* FastAPI fundamentals
* REST API development
* JSON request/response handling
* API documentation using Swagger
* Git and GitHub project management

---

## Author

**Gahana**
