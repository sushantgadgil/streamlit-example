from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime
import time

st.set_page_config(
    page_title="SYSEN 5100 HW 1",
    page_icon="random"
)

st.title("SYSEN 5160 HW 1: Streamlit Examples")

st.sidebar.button("City Temp")
st.sidebar.button("Media")



st.header("View a Cities' Temperature")

st.subheader("Enter a Zip Code")

zip = st.text_input("Enter Zip")

data = []

sampl = np.random.uniform(low=0.5, high=20, size=(50))
datelist = pd.date_range(datetime.today(), periods=50).tolist()
disp = st.checkbox("Show Data")


if disp:
    my_bar = st.progress(0)
    for percent_complete in range(100):
         time.sleep(0.01)
         my_bar.progress(percent_complete + 1)
    st.dataframe(sampl)
    st.table(datelist)

display = st.checkbox("Display Temperature Data")

if display:
    st.line_chart(sampl)
    st.bar_chart(sampl)

st.header("Images From Your Location")

with st.expander("See Media"):
    st.image("https://picsum.photos/500/300")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    

