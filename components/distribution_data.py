import numpy as np
import pandas as pd
import streamlit as st


@st.cache_data
def generate_data(mean, std):
    np.random.seed(42)

    return pd.Series(
        np.random.normal(
            loc=mean,
            scale=std,
            size=1000,
        )
    )