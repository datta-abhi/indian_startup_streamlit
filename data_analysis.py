import numpy as np
import pandas as pd

# df = pd.read_csv('startup_funding.csv')

def get_startup_list(df):
    startup_list = df['Startup Name'].unique().tolist()
    return startup_list

def get_investor_list(df):
    investor_list = df['Investors Name'].unique().tolist()
    return investor_list
