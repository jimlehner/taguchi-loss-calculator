import pandas as pd
import numpy as np
import plotly.express as px # Interactive charts
import plotly.graph_objects as go
import streamlit as st
from PIL import Image

from components.sidebar import display_sidebar
from components.additional_resources import display_resources
from components.single_measurement import display_single_measurement
from components.distribution_measurement import display_distribution_measurement
from components.overview import display_overview

# Css styling
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css("styles.css")

im = "📉"
st.set_page_config(
    page_title="Expected Loss Calculator",
    page_icon=im,
    initial_sidebar_state='collapsed',
    layout="wide"
)

# --- HEADER ---
st.title("Taguchi Loss Calculator")
st.markdown("### A web app for calculating the economic loss due to poor quality from [The Broken Quality Initiative](https://www.brokenquality.com/)")

st.markdown(
    """
    The Taguchi loss calculator allows users to calculate the economic loss due to poor quality in accordance with the Taguchi loss function.
    By selecting the tabs below, loss can be calculated for a single measurement or a distribution of measurements.
    """)

# --- SIDEBAR ---
display_sidebar()

# --- TAB SELECTION ---
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Loss for a Single Measurement", "Loss for a Distribution of Measurements", "Additional Resources"])

# --- TAB1: OVERVIEW ---
with tab1:
    display_overview()


# --- TAB2: LOSS OF A SINGLE MEASUREMENT ---
with tab2:
    display_single_measurement()

# --- TAB3: LOSS FOR A DISTRIBUTION ---
with tab3:
    display_distribution_measurement()

# --- TAB4: ADDITIONAL RESOURCES ---
with tab4:
    display_resources()