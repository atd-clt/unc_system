import streamlit as st

import plotly.graph_objs as go
import pandas as pd
import numpy as np
import datetime as dt
import altair as alt

st.image(
    "https://d6xcmfyh68wv8.cloudfront.net/learn-content/uploads/2022/06/shutterstock_544579708-770x515.jpg",
    width=500,
)

st.title("Salary")

st.markdown(
        """
    Beyond capital expenses, the larger cost to the UNC System is employee salary.
    """
)

@st.cache
def load_data(nrows):
    df = pd.read_csv('salary_data_export.csv')
    lowercase = lambda x: str(x).lower()
    df.rename(lowercase, axis='columns', inplace=True)
    return df

df = load_data(55000)


scatter = alt.Chart(df).mark_point().encode(x='age',y='employee annual base salary')
st.altair_chart(scatter, use_container_width=True)