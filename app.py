import streamlit as st
import pandas as pd
from ingestion.parser import load_and_clean_data
from analysis.feature_engineering import engineer_features
from analysis.clustering import cluster_spending
from analysis.anomaly_detection import detect_anomalies
from analysis.forecasting import forecast_spending
from recommendations.engine import generate_recommendations

st.title('Personal Finance Tracker')

# File Upload
uploaded_file = st.file_uploader("Upload your transaction CSV", type="csv")
if uploaded_file is not None:
    df = load_and_clean_data(uploaded_file)
    df = engineer_features(df)
    df = cluster_spending(df)
    anomalies = detect_anomalies(df)
    forecast = forecast_spending(df)
    recommendations = generate_recommendations(df)

    st.subheader('Transaction Data')
    st.write(df)

    st.subheader('Anomalies')
    st.write(anomalies)

    st.subheader('Forecast')
    st.write(forecast)

    st.subheader('Recommendations')
    for rec in recommendations:
        st.write(f"- {rec}")
