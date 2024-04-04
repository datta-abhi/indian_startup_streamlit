import numpy as np
import pandas as pd
import streamlit as st
from data_analysis import *

df = pd.read_csv('startup_funding.csv')

startups = get_startup_list(df)
investors = get_investor_list(df)

st.sidebar.title('Startup Funding Analysis')

options = st.sidebar.selectbox('Select from Menu',['Overall Analysis','Startup Overview','Investor Overview'])

if options == 'Overall Analysis':
    st.title('Overall Analysis')

elif options == 'Startup Overview':
    st.title('Startup Analysis')
    name = st.sidebar.selectbox('Select Startup',startups)

    btn_s = st.sidebar.button('Find Startup details')
    if btn_s:
        st.subheader(name)

elif options == 'Investor Overview':
    st.title('Investor Analysis')
    name = st.sidebar.selectbox('Select Investor', investors)

    btn_i = st.sidebar.button('Find Investor details')
    if btn_i:
        st.subheader(name)