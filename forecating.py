from fbprophet import Prophet
import pandas as pd

def forecast_spending(df):
    df_prophet = df[['date', 'amount']].rename(columns={'date': 'ds', 'amount': 'y'})
    model = Prophet()
    model.fit(df_prophet)
    future = model.make_future_dataframe(df_prophet, periods=30)
    forecast = model.predict(future)
    model.plot(forecast)
    return forecast

pip