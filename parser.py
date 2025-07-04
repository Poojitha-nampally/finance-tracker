import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['date'], dayfirst=True)
    df.drop_duplicates(inplace=True)
    df.fillna({'category': 'Unknown'}, inplace=True)
    return df