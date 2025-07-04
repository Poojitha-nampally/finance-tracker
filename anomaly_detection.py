from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(df):
    features = df[['amount_scaled', 'day_of_week', 'hour']]
    model = IsolationForest(contamination=0.02, random_state=42)
    df['anomaly'] = model.fit_predict(features)
    anomalies = df[df['anomaly'] == -1]
    return anomalies