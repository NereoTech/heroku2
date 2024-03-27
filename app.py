[14:32] Yanis MEZABER
import streamlit as st

import pandas as pd

import plotly.express as px

from src.process_data import col_date, col_donnees, main_process, fic_export_data

import logging

import os

import glob
 
logging.basicConfig(level=logging.INFO)
 
LAG_N_DAYS: int = 7
 
os.makedirs("data/raw/", exist_ok=True)

os.makedirs("data/interim/", exist_ok=True)
 
for file_path in glob.glob("data/raw/*json"):

    try:

        os.remove(file_path)

    except FileNotFoundError as e:

        logging.warning(e)
 
st.title("Data Visualization App")
 
@st.cache_data(ttl=15 * 60)

def load_data():

    main_process()

    data = pd.read_csv(fic_export_data, parse_dates=[col_date])

    return data
 
df = load_data()
 
st.subheader("Line Chart of Numerical Data Over Time")

numerical_column = col_donnees

fig = px.line(df, x=col_date, y=col_donnees, title="Consommation en fonction du temps")

st.plotly_chart(fig)
 
# Calculating average consumption per day of the week

df['Day_of_Week'] = df[col_date].dt.day_name()

average_consumption_per_day = df.groupby('Day_of_Week')[col_donnees].mean().reset_index()
 
# Creating a bar chart for average consumption per day of the week

st.subheader("Average Consumption per Day of the Week")

fig_bar = px.bar(average_consumption_per_day, x='Day_of_Week', y=col_donnees, title='Moyenne de consommation par jour de la semaine')

st.plotly_chart(fig_bar)
