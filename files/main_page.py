import streamlit as st

# data manipulation
import pandas as pd
import numpy as np


st.title('The University of North Carolina System')

st.image("UNC System Map.jpg")

with st.expander("Click here to learn more about the UNC System"):

    st.write("")

    st.markdown(
        """
    The University of North Carolina is the multi-campus public university system for the state of North Carolina.  It encompasses 16 universities and 1 residential high school for gifted students, the NC School of Science and Mathematics.
    """
    )
    st.write("")

    st.markdown(
        """
    The UNC System is a treasured public institution dedicated to serving the people of North Carolina through world-class teaching, research, and community engagement. Today, nearly 250,000 students are enrolled in our 16 universities across the state and at the NC School of Science and Mathematics.
    """
    )

    st.markdown(
        """
    Navigate this app by using the page tabs on the left handside.
    """
    )

    st.write("")


@st.cache
def load_data(nrows):
    df = pd.read_csv('salary_data_export.csv')
    lowercase = lambda x: str(x).lower()
    df.rename(lowercase, axis='columns', inplace=True)
    return df

data_load_state = st.text('Loading data...')
df = load_data(55000)
data_load_state.text("Done! (using st.cache)")

#create a checkbox called 'Show raw data'
#if checked, it will right the data, otherwise, it will not
if st.checkbox('Import Data'):
    st.subheader('2022 UNC System Salary')
    st.write("This data was produced on 11.15.2022.")  
    st.text ("An update can be dataset found below:")
    st.write("https://uncdm.northcarolina.edu/salaries/index.php")
    st.text ("Search table: Click in the table and use hotkeys (Ctrl + F or ⌘ Cmd + F) to bring up the search bar")
    st.write(df)

