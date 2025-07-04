def generate_recommendations(df):
    recommendations = []
    if df['amount'].mean() > 100:
        recommendations.append("Consider reducing discretionary spending.")
    if df['anomaly'].sum() > 0:
        recommendations.append("Review flagged transactions for anomalies.")
    return recommendations