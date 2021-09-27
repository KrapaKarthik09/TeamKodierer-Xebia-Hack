import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
st.title('Carbon Footprint Tracker')
data = pd.read_csv('assets/carbon.csv')
st.sidebar.title("Dashboard")

st.sidebar.title("Visualization Selector")
select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'pie chart'], key='1')

st.sidebar.title("Display period")
select1 = st.sidebar.selectbox('Period', ['Daily', 'Monthly','Yearly'], key='1')

submit = st.sidebar.button('Submit')

if submit:
    if select1 == 'Daily':
        if select == 'pie chart':
            fig = px.pie(data, values=data['GHG emissions (kg CO2) / year'][:], names=data['Item'][:], title='Total Carbon emission')
            st.plotly_chart(fig)
        if select == 'Bar plot':
            fig = go.Figure(data=[go.Bar(name='Item', x=data['Energy use (kWh/ year)'][:], y=data['GHG emissions (kg CO2) / year'][:])])
            st.plotly_chart(fig)
    if select1 == 'Monthly':
        if select == 'pie chart':
            fig = px.pie(data, values=data['GHG emissions (kg CO2) / year'][:], names=data['Item'][:], title='Total Carbon emission')
            st.plotly_chart(fig)
        if select == 'Bar plot':
            fig = go.Figure(data=[go.Bar(name='Item', x=data['Energy use (kWh/ year)'][:], y=data['GHG emissions (kg CO2) / year'][:])])
            st.plotly_chart(fig)
    if select1 == 'Yearly':
        if select == 'pie chart':
            fig = px.pie(data, values=data['GHG emissions (kg CO2) / year'][:], names=data['Item'][:], title='Total Carbon emission')
            st.plotly_chart(fig)
        if select == 'Bar plot':
            fig = go.Figure(data=[go.Bar(name='Item', x=data['Energy use (kWh/ year)'][:], y=data['GHG emissions (kg CO2) / year'][:])])
            st.plotly_chart(fig)

