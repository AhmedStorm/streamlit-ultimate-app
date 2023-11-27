import streamlit as st
from math import *
st.header("Shape Calculations")
shape = st.selectbox("Choose a shape",["Circle","Rectangle"])
if shape == 'Circle':
    radius = st.number_input("Enter Radius:", min_value=0., step=0.01)
    area = pi * (radius**2)
    perimeter = 2*pi*radius


if shape == 'Rectangle':
    width = st.number_input("Enter width:", min_value=0., step=0.01)
    height = st.number_input("Enter height:", min_value=0., step=0.01)
    area = width * height
    perimeter = 2* (width + height)

button = st.button("Calculate Area and Perimeter")
if button:
    st.write("Area= ",area)
    st.write("Perimeter= ",perimeter)