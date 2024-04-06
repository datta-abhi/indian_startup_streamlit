import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from data_analysis import *

df = pd.read_csv('startup_cleaned.csv')
df = df.sort_values('Date',ascending = False)

startups = get_startup_list(df)
investors = get_investor_list(df)

def load_investor_details(investor):
    st.header(investor)

    # most recent investments
    st.subheader('Most Recent Investments')
    recent_inv = df[df['Investor'].str.contains(investor)][['Date','Startup','Vertical','City','Round','Amount']].head()
    st.dataframe(recent_inv)

    col1,col2 = st.columns(2)

    # biggest investment
    with col1:
        st.subheader('Biggest Investment')
        biggest_inv = df[df['Investor'].str.contains(investor)].groupby('Startup')['Amount'].sum().sort_values(ascending = False).head(3)

        fig,ax = plt.subplots()
        ax.bar(x = biggest_inv.index,height = biggest_inv.values)
        st.pyplot(fig)

    # Vertical split
    with col2:
        st.subheader('Investment Vertical')
        verticals = df[df['Investor'].str.contains(investor)].groupby('Vertical')['Amount'].sum()

        fig1, ax1 = plt.subplots()
        ax1.pie(verticals,labels = verticals.index,autopct = '%0.0f')
        st.pyplot(fig1)


def load_overall_analysis():

    #total Amount Invested
    total = np.round(df['Amount'].sum()/1000)


    # Top 10 most funded startups
    max_funding = df.groupby('Startup')['Amount'].sum().sort_values(ascending = False).head(10)

    #average ticket size
    avg_funding = np.round(df.groupby('Startup')['Amount'].sum().mean(),1)

    # nos of Startups
    nos_startups = df['Startup'].nunique()

    col1,col2,col3 = st.columns(3)

    with col1:
        st.metric('Total',str(total) + ' Thousand Cr')
    with col2:
        st.metric('Average',str(avg_funding)+ 'Cr')
    with col3:
        st.metric('Funded Starups',nos_startups)

    st.subheader("Top 10 most Funded Startups")
    fig2, ax2 = plt.subplots()
    ax2.bar(x=max_funding.index, height=max_funding.values)
    plt.xticks(rotation=45)
    st.pyplot(fig2)


st.set_page_config(layout= 'wide')
st.sidebar.title('Startup Funding Analysis')

options = st.sidebar.selectbox('Select from Menu',['Overall Analysis','Startup Overview','Investor Overview'])

if options == 'Overall Analysis':
    st.title('Overall Analysis')
    btn_o = st.sidebar.button('Show Overall Analysis')
    if btn_o:
        load_overall_analysis()


elif options == 'Startup Overview':
    st.title('Startup Analysis')
    name_startup = st.sidebar.selectbox('Select Startup',startups)

    btn_s = st.sidebar.button('Find Startup details')
    if btn_s:
        st.subheader(name_startup)

elif options == 'Investor Overview':
    st.title('Investor Analysis')
    name_investor = st.sidebar.selectbox('Select Investor', investors)

    btn_i = st.sidebar.button('Find Investor details')
    if btn_i:
        load_investor_details(name_investor)