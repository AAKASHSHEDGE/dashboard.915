import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cufflinks as cf 
import plost



st.set_page_config(layout='wide', initial_sidebar_state='expanded')
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    
st.sidebar.header('Dashboard `version 2`')

st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('Q1', 'Q2','Q3','Q4'))

st.sidebar.subheader('line chart parameter')
time_color = st.sidebar.selectbox('Color by', ('Amazon', 'Apple','Facebook','Google'))

st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data', ['Amazon', 'Apple','Facebook','Google'], ['Amazon', 'Apple','Facebook','Google'])
plot_height = st.sidebar.slider('Specify plot height', 200, 900, 250)

#row 1
st.header("STOCK PRICE")
st.markdown('## Metrics')
col1, col2, col3,col4= st.columns(4)
col1.metric("Amazon", "3384.179 ₹", "-0.02%")
col2.metric("Apple", "179.26 ₹", "0.04%")
col3.metric("Facebook", "342.29 ₹", "0.01%")
col4.metric("Google","2930.59 ₹" , "0.04%" )

#row2
c1, c2 = st.columns((5,4))
with c1 :
    st.markdown("## DATASET")
    df = pd.read_csv("stockprice5.csv")
    st.write(df)
with c2:
    sto = pd.read_csv("Sto.csv")
    
    st.markdown('## Donut chart')
    st.markdown("#### 2021 Profit & Loss In Percentage")
    plost.donut_chart(
        data=sto,
        theta=donut_theta,
        color='company',
        legend='bottom', 
        use_container_width=True)
    

#row3
stocks = pd.read_csv('stockprice5.csv',parse_dates=['Date'])
st.markdown("## Line Chart")
st.markdown('#### Closing price by date')
st.line_chart(stocks , x = 'Date',y = time_color)

#row4
st.line_chart(stocks, x = 'Date', y = plot_data, height = plot_height)

#row5
st.header("Scatter Plot")
c1, c2 = st.columns((4,4))
with c1 :
    st.markdown("### Apple v/s facebook")
    fig, ax =plt.subplots()
    ax.scatter(stocks['Apple'],stocks['Facebook'])
    st.pyplot(fig)
with c2 :
    st.markdown("### Amazon v/s Google")
    fig, ax =plt.subplots()
    ax.scatter(stocks['Amazon'],stocks['Google'])
    st.pyplot(fig)


#row6
st.header("Bar Chart")
st.bar_chart(stocks ,x = 'Date' , y = plot_data ,height = plot_height)    

labels = ['Amazon','Apple','Facebook','Google']
fig , ax = plt.subplots()
ax.boxplot(stocks.iloc[:,0])
st.pyplot

