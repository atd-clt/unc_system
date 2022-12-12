import streamlit as st
import numpy as np # for working with arrays
import pandas as pd # data processing and analysis (e.g. pd.read_csv)
import seaborn as sns #visualisation
import altair as alt #visualisation
import matplotlib as plt #visualisation

#enable altair to plot all the data
alt.data_transformers.disable_max_rows()
alt.themes.enable('fivethirtyeight')

st.image(
    "https://www.augusta.edu/hr/relations/university-employee-relations/images/employee2.jpg",
    width=500,
)

st.title("Employees")

st.markdown(
        """
    With close to 48,000 employees, the UNC System is one of North Carolina’s largest employers.
    """
)

@st.cache
def load_data(nrows):
    df = pd.read_csv('salary_data_export.csv')
    lowercase = lambda x: str(x).lower()
    df.rename(lowercase, axis='columns', inplace=True)
    return df

df = load_data(55000)

st.write('Understanding Employees Distribution Amongst Campuses')


st.write(df['institution name'].value_counts())


age = alt.Chart(df).mark_bar().encode(
    alt.X("age:Q", bin=True),
    y='count()', 
)


st.write('Understanding Age distribution Amongst Employees')

st.write(age)

