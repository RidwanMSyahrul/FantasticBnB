import eda 
import prediction
import filtering
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

PAGES = {
    "Exploratory Data Analysis": eda,
    # "Recommender System": prediction,
    "Filtering Data": filtering
}

st.sidebar.title('Pages')
selection = st.sidebar.radio("Choose page", list(PAGES.keys()))
page = PAGES[selection]
page.app()
