import pandas as pd
import os

# Load data from a file if it exists, otherwise start fresh
def load_data():
    if os.path.exists('progress_data.csv'):
        df = pd.read_csv('progress_data.csv', index_col=0)
    else:
        df = pd.DataFrame(columns=['Name'])
    return df

# Save data to a file
def save_data(df):
    df.to_csv('progress_data.csv')
