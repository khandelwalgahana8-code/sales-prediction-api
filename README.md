# 🚀 Sales Intelligence Dashboard

An AI-powered Sales Prediction and Business Intelligence Dashboard built using FastAPI, Machine Learning, HTML/CSS/JavaScript, and Chart.js.

This application predicts future sales based on advertising spend and provides actionable business insights, ROI analysis, growth forecasts, risk assessment, and strategic recommendations through an interactive dashboard.

📌 Overview

Businesses often struggle to understand how advertising investments impact revenue. This project leverages Machine Learning to estimate sales performance based on advertising spend and transforms raw predictions into meaningful business intelligence.

The system combines:

Machine Learning Prediction Engine
FastAPI REST API
Interactive Analytics Dashboard
Revenue Forecasting
Business Recommendations
Real-Time Data Visualization
✨ Features
🔮 Sales Prediction

Predict expected sales based on advertising spend using a trained Machine Learning model.

📊 Interactive Dashboard

Modern analytics dashboard displaying:

Predicted Sales
ROI Score
Growth Potential
Risk Assessment
💡 Business Insights

Automatically generates insights based on predicted performance.

Example:

Advertising efficiency is excellent. Revenue growth potential is strong and scalable.

📈 Revenue Projection

Projects future sales if advertising budgets increase.

Example:

Current Sales: ₹25,000

Projected Sales (+20% Budget):
₹30,000
🎯 Strategic Recommendations

Generates actionable recommendations such as:

Increase marketing budget
Scale successful campaigns
Improve audience targeting
Optimize conversion funnels
Focus on customer retention
📉 Growth Forecast Visualization

Interactive sales trend visualization using Chart.js.

Shows how sales may change as advertising investment increases.

🌙 Dark / Light Mode

Professional dashboard experience with:

Light Theme
Dark Theme
Responsive Design
🏗️ Project Architecture
User Input
    │
    ▼
Frontend Dashboard
(HTML + CSS + JS)
    │
    ▼
FastAPI Backend
    │
    ▼
Machine Learning Model
(Joblib)
    │
    ▼
Sales Prediction
    │
    ▼
Business Intelligence Engine
    │
    ▼
Dashboard Results
🛠️ Technology Stack
Backend
Python
FastAPI
Uvicorn
Joblib
Scikit-Learn
Pandas
Frontend
HTML5
CSS3
JavaScript
Chart.js
Machine Learning
Linear Regression
Model Serialization with Joblib
📂 Project Structure
sales-prediction-api/

│
├── app.py
├── sales_prediction_model.pkl
├── requirements.txt
├── README.md
│
├── frontend/
│   └── index.html
│
└── screenshots/
⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/khandelwalgahana8-code/sales-prediction-api.git

cd sales-prediction-api
2️⃣ Create Virtual Environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run FastAPI Server
uvicorn app:app --reload

5️⃣ Launch Frontend

Open:

frontend/index.html

or

http://127.0.0.1:5500/index.html

using VS Code Live Server.

📡 API Endpoint
Predict Sales

POST

/predict
Request
{
  "AdSpend": 5000
}
Response
{
  "predicted_sales": 25420.57
}
📊 Sample Dashboard Output
Predicted Sales
₹25,420

ROI Score
82/100

Growth Potential
HIGH

Risk Level
LOW
Business Insight
Advertising efficiency is excellent.
Revenue growth potential is strong and scalable.
Recommendations
✓ Increase budget by 15%

✓ Scale top campaigns

✓ Expand targeting

✓ Improve retention

✓ Launch promotions
🎯 Business Applications

This solution can be adapted for:

Marketing Analytics
Sales Forecasting
Budget Optimization
Campaign Performance Tracking
Revenue Planning
Decision Support Systems
Startup Growth Analysis
🔮 Future Enhancements
Multi-Factor Prediction

Current:

Ad Spend

Future:

TV Spend
Radio Spend
Social Media Spend
Region
Seasonality
Competitor Activity
Advanced Analytics
Forecast Next Month Sales
Trend Detection
Customer Segmentation
AI Insights
PDF Reports
Cloud Deployment
User Authentication
📈 Performance Benefits
Feature	Benefit
ML Prediction	Revenue Forecasting
ROI Analysis	Budget Optimization
Growth Forecast	Strategic Planning
Risk Assessment	Better Decision Making
Dashboard Analytics	Executive Insights
🚀 Future Vision

Transform this project into a complete AI-powered Business Intelligence Platform capable of:

Predictive Analytics
Revenue Forecasting
Marketing Intelligence
Strategic Planning
Executive Reporting

for startups, enterprises, and marketing teams.

👨‍💻 Author

Gahana Khandelwal

GitHub:

sales-prediction-api Repository
