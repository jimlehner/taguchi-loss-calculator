import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from components.markdown_utils import (
    render_markdown_with_images, 
    load_quiz,
    display_quiz
    )

from components.distribution_controls import distribution_inputs, distribution_loss_controls
from components.distribution_data import generate_data
from calculations.distribution_calculations import calculate_distribution_metrics

from components.distribution_controls import distribution_loss_controls
from calculations.distribution_calculations import calculate_distribution_loss
from calculations.distribution_loss_curve import (
    calculate_loss_curve,
    calculate_overhang,
)
from components.distribution_chart import display_distribution_loss_chart
from components.distribution_summary import display_distribution_summary

def display_distribution_measurement():

    st.markdown("## The Economic Loss for a Distribution of Measurements")

    # Instructions
    with st.expander("Click to view instructions"):
            with open("content/distribution_instructions.md", "r", encoding="utf-8") as f:
                st.markdown(f.read())

    # Calculating economic loss
    with st.expander("Click to learn how the economic loss for a distribution of measurements is calculated "):
        with open("content/distribution_calculations.md", "r", encoding="utf-8") as f:
            content = f.read()#st.markdown(f.read())

        image_map = {
            "[FIGURE_1]": "figures/EQ_average_taguchi_loss.png",
            "[FIGURE_2]": "figures/EQ_numeric_constant_K.png",
        }

        render_markdown_with_images(content, image_map, image_width=1200)

    # Quiz questions
    with st.expander(
        "Click to answer questions about the economic loss for a distribution of measurements"
    ):
        display_quiz(
            "content/distribution_questions.md",
            "distribution"
        )

    st.divider()

    inputs = distribution_inputs()
    
    if inputs["source"] == "upload":

        df = pd.read_csv(inputs["file"])

        column = st.selectbox(
            "Select a column",
            df.columns
        )

        data = df[column].dropna()

    else:

        data = generate_data(
            inputs["mean"],
            inputs["std"]
        )

    # Calculate distribution statistics
    distribution_results = calculate_distribution_metrics(data)


    mean = distribution_results["mean"]
    std = distribution_results["std"]
    sigmaX = distribution_results["SigmaX"]
    UPL = distribution_results["UPL"]
    LPL = distribution_results["LPL"]

    # st.divider()


    # Taguchi loss inputs
    (usl, 
     lsl, 
     c_scrap, 
     round_value, 
    #  overhang,
     show_annotation, 
     show_spec_target,
     show_process_limits,
     n_bins) = distribution_loss_controls()

    overhang = calculate_overhang(
            data,
            lsl,
            usl,
            )

    # Calculate Taguchi loss
    loss_results = calculate_distribution_loss(
        usl,
        lsl,
        c_scrap,
        mean,
        std,
        sigmaX,
    )

    target = loss_results["target"]
    tolerance = loss_results["tolerance"]
    k = loss_results["k"]
    average_loss = loss_results["average_loss"]
    loss_on_target_with_variance = loss_results["loss_on_target_with_variance"]
    loss_off_target_predictable = loss_results["loss_off_target_predictable"]
    loss_on_target_predictable = loss_results["loss_on_target_predictable"]

    # Generate Taguchi loss curve

    curve_results = calculate_loss_curve(
        lsl,
        usl,
        target,
        tolerance,
        mean,
    )


    df_distribution = curve_results["df"]

    y_at_mean = curve_results["y_at_mean"]

    # Generate Taguchi loss histogram
    display_distribution_loss_chart(
        data=data,
        df=df_distribution,
        mean=mean,
        y_at_mean=y_at_mean,
        usl=usl,
        lsl=lsl,
        target=target,
        UPL=UPL,
        LPL=LPL,
        std=std,
        average_loss=average_loss,
        n_bins=n_bins,
        round_value=round_value,
        show_annotation=show_annotation,
        show_spec_target=show_spec_target,
        show_process_limits=show_process_limits,
    )

    # The path forward
    # display_distribution_summary(
    #     average_loss=loss_results["average_loss"],
    #     loss_on_target_with_variance=loss_results["loss_on_target_with_variance"],
    #     loss_off_target_predictable=loss_results["loss_off_target_predictable"],
    #     loss_on_target_predictable=loss_results["loss_on_target_predictable"],
    #     round_value=round_value,
    #     )

    st.divider()
    