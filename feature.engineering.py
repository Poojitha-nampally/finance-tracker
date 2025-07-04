from sklearn.preprocessing import StandardScaler

def engineer_features(df):
    df['day_of_week'] = df['date'].dt.dayofweek
    df['hour'] = df['date'].dt.hour
    df['amount_scaled'] = StandardScaler().fit_transform(df[['amount']])
    return df