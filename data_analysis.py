import numpy as np
import pandas as pd

# df = pd.read_csv('startup_cleaned.csv')

def get_startup_list(df):
    startup_list = sorted(df['Startup'].unique().tolist())
    return startup_list

def get_investor_list(df):
    investor_list = sorted(set(df['Investor'].str.split(',').sum()))
    return investor_list

