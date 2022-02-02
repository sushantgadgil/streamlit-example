from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime

st.title("SYSEN 5160 HW 1: Streamlit Examples")

st.sidebar.button("City Temp","Media")


st.header("View a Cities' Temperature")

st.subheader("Enter a Zip Code")

zip = st.text_input("Enter Zip")

data = []

sampl = np.random.uniform(low=0.5, high=20, size=(50))
datelist = pd.date_range(datetime.today(), periods=50).tolist()
disp = st.checkbox("Show Data")

if disp:
    st.dataframe(sampl)
    st.table(datelist)

display = st.checkbox("Display Temperature Data")

if display:
    st.line_chart(sampl)
    st.bar_chart(sampl)

st.header("Images From Your Location")

disp2 = st.checkbox("Show Media")

with st.expander("See Media"):
    st.image("https://picsum.photos/500/300")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    

