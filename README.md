# 🦠 COVID-19 Impact Analysis Dashboard (Streamlit Version)

**Role:** Data Analyst  
**Dataset:** [Kaggle - COVID-19 Clean Complete Dataset](https://www.kaggle.com/datasets/imdevskp/corona-virus-report)

## 🔎 Project Summary

Analyzed COVID-19 time series data for 15+ countries and presented the findings in an interactive Streamlit dashboard:

- KPI Summary (Confirmed, Deaths, Recovered, Active)
- Correlation heatmap of key indicators
- Time series trend of confirmed cases per country

## 📁 Files

- `app.py`: Streamlit dashboard app
- `covid_19_clean_complete.csv`: Dataset (upload manually from Kaggle)

## ▶️ How to Run

1. Make sure you have Streamlit installed:
```bash
pip install streamlit pandas matplotlib seaborn
```

2. Place the dataset CSV file in the same folder as `app.py`.

3. Run the app:
```bash
streamlit run app.py
```
