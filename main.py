import streamlit as st
from PIL import Image
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt


# ---- MAINPAGE ----
st.title(":bar_chart: Footprint Dashboard")
st.markdown("##")

def load_image(img):
	im = Image.open(os.path.join(img))
	return im

menu = st.sidebar.selectbox("Menu",["Home", "About Us"])

st.success("WebApp Loaded Successfully")

st.header("Welcome to Carbon Footprint Calculator !!!")

st.markdown("<h4 style='text-align: center; color: white;'>(Build by Team Kodierer)</h4>", unsafe_allow_html=True)

st.image(load_image('carbon-footprint.jpg'))


df = pd.read_excel(io="Daily Use Appliances Carbon Footprint.xlsx", engine='openpyxl', sheet_name='Sheet1', usecols='A:F', nrows=23,)
l1 = ['Item', 'Power (w)', 'Usage per year (h)', 'Energy use(kWh/ year)', 'Annual cost ($)', 'GHG emissions (kg CO2) / year']

st.sidebar.title("Dashboard")

st.sidebar.title("Visualization Selector")
select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'pie chart'], key='1')

st.sidebar.title("Display period")
select1 = st.sidebar.selectbox('Period', ['Daily', 'Monthly','Yearly'], key='2')

submit = st.sidebar.button('Submit')

if submit:
    if select1 == 'Daily':
        if select == 'pie chart':
            fig = px.pie(df, values=df['GHG emissions (kg CO2) / year'][:], names=df['Item'][:], title='Total Carbon emission')
            st.plotly_chart(fig)
        if select == 'Bar plot':
            fig = go.Figure(data=[go.Bar(name='Item', x=df['Energy use (kWh/ year)'][:], y=df['GHG emissions (kg CO2) / year'][:])])
            st.plotly_chart(fig)
    if select1 == 'Monthly':
        if select == 'pie chart':
            fig = px.pie(df, values=df['GHG emissions (kg CO2) / year'][:], names=df['Item'][:], title='Total Carbon emission')
            st.plotly_chart(fig)
        if select == 'Bar plot':
            fig = go.Figure(data=[go.Bar(name='Item', x=df['Energy use (kWh/ year)'][:], y=df['GHG emissions (kg CO2) / year'][:])])
            st.plotly_chart(fig)
    if select1 == 'Yearly':
        if select == 'pie chart':
            fig = px.pie(df, values=df['GHG emissions (kg CO2) / year'][:], names=df['Item'][:], title='Total Carbon emission')
            st.plotly_chart(fig)
        if select == 'Bar plot':
            fig = go.Figure(data=[go.Bar(name='Item', x=df['Energy use (kWh/ year)'][:], y=df['GHG emissions (kg CO2) / year'][:])])
            st.plotly_chart(fig)

val=0
for i in df['GHG emissions (kg CO2) / year']:
    if(i<100):
        #print("low")
        val=val+1
    elif(i >= 100 and i < 500):
        #print("moderate")
        val=val+2
    else:
        #print("high")
        val=val+3
print(val)
if val < 27:
    st.balloons()
    st.success("Low")
elif val >=27 and val <40:
    st.warning("Moderate")
else:
    st.error("High")

kpi1, kpi2 = st.columns(2)

kpi1.selectbox('Gadgets', ['Water heater', 'Electric furnace (home heating)', 'Air Conditioner', 'Space heater', 'TV, 42", plasma', 'TV, 42", LED', 'Cable TV box on standby', '5 x CFL lightbulbs (18 W)', 'Vaccuum cleaner', 'Clothes dryer', 'Hair Dryer', 'Fridge', 'Coffee Grinder', 'Kettle', 'Oven', 'Toaster Oven', 'Cell phone 10 Wh battery*', 'Desktop computer', 'Laptop 54 Wh battery*', 'WiFi router', 'Game console PS4', 'Game console Xbox One'], key='4')

kpi2.selectbox('Plot Type', ['Bar Plot', 'Pie Chart', 'Bubble'], key='5')



st.balloons()
st.dataframe(df.style.highlight_max(axis=0))
