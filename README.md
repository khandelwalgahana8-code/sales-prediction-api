# Sales Prediction API

A Machine Learning API built with FastAPI.

## Features
- Predict sales based on advertising spend
- FastAPI backend
- Trained ML model using Scikit-Learn

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## API Endpoint

POST /predict

Request:

```json
{
  "AdSpend": 5000
}
```

Response:

```json
{
  "predicted_sales": 25000
}
```
