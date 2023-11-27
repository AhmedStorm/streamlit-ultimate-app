import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


st.header("Data Analysis")
file = st.file_uploader("Upload a File",type="csv")

if file:
    df = pd.read_csv(file)
    new = df.columns.to_list()
    col = st.slider("SELECT ROWS TO BE SHOWN",min_value=0,max_value=len(df),value=10)
    columns2show= st.multiselect(label="COLUMNS TO SHOW:",options=new,default=new)
    numerical_columns = df.select_dtypes(include=np.number).columns.to_list()
    tab1, tab2 = st.tabs(["Scatter Plot","Histogram"])
    with tab1:
        st.write(df[:col][columns2show])

        col1, col2 , col3 = st.columns(3)
        with col1:
            x_column = st.selectbox("Column X",numerical_columns)
        with col2:
            y_column = st.selectbox("Column Y",numerical_columns)
        with col3:
            color = st.selectbox("Color",df.columns)
        figure_out = px.scatter(df,x=x_column, y=y_column,color=color)
        st.plotly_chart(figure_out)

    with tab2:
        histogram_feature = st.selectbox('Select feature to histogram', numerical_columns)
        fig_hist = px.histogram(df, x=histogram_feature)
        st.plotly_chart(fig_hist)