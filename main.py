import pandas as pd
import os
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

menu = st.sidebar.selectbox("Menu",["Home", "About Us"])

st.success("WebApp Loaded Successfully")
st.header("Welcome to Carbon Footprint Calculator !!!")
st.markdown("<h4 style='text-align: center; color: white;'>(Build by Team Kodierer)</h4>", unsafe_allow_html=True)

def load_image(img):
    im = Image.open(os.path.join(img))
    return im
st.image(load_image("reduce+carbon+footprint+with+The+Chicago+Greenbox.jpg"))


st.write('Climate change is the result of increasing levels of greenhouse gas (GHG) emissions, primarily referenced in terms of carbon dioxide (CO2) emissions. The longer we delay action on climate change, the worse its effects will be. Every person, business, organization, and government can help reduce greenhouse gas emissions, protect our environment, and ensure the health of our climate by carbon footprint reduction.')
st.write('Your carbon footprint is the total greenhouse gas emissions caused both directly and indirectly by your activities—and this includes all the things you buy, use, and consume. Every person, organization, product, and event has a carbon footprint. Typically a person’s carbon footprint is represented as the sum total of all of their direct and indirect carbon emissions over the course of a year.   ')
st.write('The smaller your carbon footprint, the better for the planet and the future. A bigger footprint means that your activities release more greenhouse gasses and had a bigger negative impact on the environment.')
data = pd.read_excel(io="Daily Use Appliances Carbon Footprint.xlsx", engine='openpyxl', sheet_name='Sheet1', usecols='A:F', nrows=23,)


st.sidebar.title("Visualization Selector")
st.sidebar.markdown("Select the Charts/Plots accordingly:")
select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart','Bubble chat'], key='1')

st.sidebar.title("Display period")
st.sidebar.markdown("Select the period:")
select1 = st.sidebar.selectbox('Period', ['Daily', 'Monthly','Yearly'], key='2')

submit = st.sidebar.button('Submit')
if submit:
    st.title("Dashboard")
    if select1 == 'Daily':
        if select == 'Pie chart':
            fig = px.pie(data, values=data['GHG emissions (kg CO2) / year'][:], names=data['Item'][:], title='Total Carbon emission')
            st.plotly_chart(fig)
        if select == 'Bar plot':
            fig = go.Figure(data=[go.Bar(name='Item', x=data['Energy use (kWh/ year)'][:], y=data['GHG emissions (kg CO2) / year'][:])])
            st.plotly_chart(fig)
        if select == 'Bubble chat':
            fig = go.Figure(data=[go.Scatter(x=['Energy use (kWh/ year)'],y=['GHG emissions (kg CO2) / year'],mode='markers',marker=dict(color=['red'],showscale=True))])
            st.plotly_chart(fig)
        
    if select1 == 'Monthly':
        if select == 'Pie chart':
            fig = px.pie(data, values=data['GHG emissions (kg CO2) / year'][:], names=data['Item'][:], title='Total Carbon emission')
            st.plotly_chart(fig)
        if select == 'Bar plot':
            fig = go.Figure(data=[go.Bar(name='Item', x=data['Energy use (kWh/ year)'][:], y=data['GHG emissions (kg CO2) / year'][:])])
            st.plotly_chart(fig)
        if select == 'Bubble chat':
            fig = go.Figure(data=[go.Scatter(x=['Energy use (kWh/ year)'],y=['GHG emissions (kg CO2) / year'],mode='markers',marker=dict(color=['red'],showscale=True))])
            st.plotly_chart(fig)
            
    if select1 == 'Yearly':
        if select == 'Pie chart':
            fig = px.pie(data, values=data['GHG emissions (kg CO2) / year'][:], names=data['Item'][:], title='Total Carbon emission')
            st.plotly_chart(fig)
        if select == 'Bar plot':
            fig = go.Figure(data=[go.Bar(name='Item', x=data['Energy use (kWh/ year)'][:], y=data['GHG emissions (kg CO2) / year'][:])])
            st.plotly_chart(fig)
        if select == 'Bubble chat':
            fig = go.Figure(data=[go.Scatter(x=['Energy use (kWh/ year)'],y=['GHG emissions (kg CO2) / year'],mode='markers',marker=dict(color=['red'],showscale=True))])
            st.plotly_chart(fig)
    
    val=0
    for i in data['GHG emissions (kg CO2) / year']:
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
        st.success("Low")
        st.balloons()
        st.write("THE BEST TIME TO PLANT A TREE WAS 20 YEARS AGO, THE SECOND BEST TIME IS NOW.LET'S PLANT THE TREE,AND MAKE THIS WORLD POLLUTION FREE.")
    elif(val >=27 and val <40):
        st.warning("Moderate")
        st.markdown("<h4><ul><li>When you buy new appliances, upgrade to energy-efficient models. In the United States, look for the EPA’s ENERGY STAR label. Energy-efficient appliances generally cost a little more upfront, but the long-term savings are astonishing. If you switched to energy-efficient appliances in your home, you could save $11,000 on your energy bills and save about 130,000 pounds of greenhouse gas emissions over the lifetime of the products.</li><li>If every home in the U.S. used energy-efficient appliances, we would eliminate 175 million tons of greenhouse gas emissions and collectively save $15 billion in energy costs every year. If all Americans just switched to energy-efficient refrigerators, the U.S. would need 30 fewer power plants than we currently use.</li><li>If you’re not using a device, don’t just turn it off, unplug it. Flipping the switch on a power strip works as well, and is a simple solution if you have a bunch of computer or entertainment devices that all share an outlet.</h4></li></ul>",unsafe_allow_html=True)
        st.write("THE BEST TIME TO PLANT A TREE WAS 20 YEARS AGO, THE SECOND BEST TIME IS NOW.LET'S PLANT THE TREE,AND MAKE THIS WORLD POLLUTION FREE.")
    else:
        st.error("High")
        st.markdown("<h4><ul><li>Change incandescent light bulbs (which waste 90 percent of their energy as heat) to light emitting diodes (LEDs). Though LEDs cost more, they use a quarter of the energy and last up to 25 times longer.</li><li>Switch lights off when you leave the room and unplug your electronic devices when they are not in use.</li><li>Turn your water heater down to 120˚F. This can save about 550 pounds of CO2 a year.</li><li>Installing a low-flow showerhead to reduce hot water use can save 350 pounds of CO2. Taking shorter showers helps, too.</li><li>Even better, generate your own green energy! The sun will continue to shine for billions of years and provides free heat and light. Install some solar panels on your roof to harvest this natural, abundant energy. Solar panels can cost a little money upfront, but federal and state governments often offer tax incentives for the carbon offsets created by renewable energy.</li><li>Drive less. Walk, take public transportation, carpool, rideshare or bike to your destination when possible. This not only reduces CO2 emissions, it also lessens traffic congestion and the idling of engines that accompanies it.</li></ul>",unsafe_allow_html=True)
        st.write("THE BEST TIME TO PLANT A TREE WAS 20 YEARS AGO, THE SECOND BEST TIME IS NOW.LET'S PLANT THE TREE,AND MAKE THIS WORLD POLLUTION FREE.")
    
    st.selectbox('Gadgets', ['Water heater', 'Electric furnace (home heating)', 'Air Conditioner', 'Space heater', 'TV, 42", plasma', 'TV, 42", LED', 'Cable TV box on standby', '5 x CFL lightbulbs (18 W)', 'Vaccuum cleaner', 'Clothes dryer', 'Hair Dryer', 'Fridge', 'Coffee Grinder', 'Kettle', 'Oven', 'Toaster Oven', 'Cell phone 10 Wh battery*', 'Desktop computer', 'Laptop 54 Wh battery*', 'WiFi router', 'Game console PS4', 'Game console Xbox One'], key='4')
    st.dataframe(data.style.highlight_max(axis=0))

nam = st.text_input("Enter Your Suggestion(if you have any),This will help other users.")
su = st.button('Submit', key='3')
if su:
    st.success("Thank you for the Suggestions")
