from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

model = joblib.load("sales_prediction_model.pkl")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    AdSpend: float

@app.post("/predict")
def predict(data: InputData):
    prediction = model.predict([[data.AdSpend]])
    return {"predicted_sales": float(prediction[0])}