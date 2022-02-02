from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

st.title("SYSEN 5160 HW 1: Streamlit Examples")

st.header("View a Cities' Temperature")

st.subheader("Enter a Zip Code")

zip = st.text_input("Enter Zip")

data = []

sampl = np.random.uniform(low=0.5, high=13.3, size=(50))
datelist = pd.date_range(datetime.today(), periods=50).tolist()

st.write(sampl)
st.write(datelist)

display = st.checkbox("Display Data")

if display:
    st.line_chart(sampl)

