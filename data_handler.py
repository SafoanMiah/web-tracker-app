import pandas as pd
import os
import glob
import plotly.io as pio

SNAPSHOT_DIR = 'historical'

os.makedirs(SNAPSHOT_DIR, exist_ok=True)

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

def calculate_total_scores(df):
    score_cols = [col for col in df.columns if col != 'Name']
    for col in score_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df['Total Score'] = df[score_cols].sum(axis=1)
    return df

