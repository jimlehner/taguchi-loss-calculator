import streamlit as st
import pandas as pd
import numpy as np

from components.markdown_utils import (
    render_markdown_with_images, 
    load_quiz,
    display_quiz
    )
from components.taguchi_chart import display_loss_chart
from components.single_measurement_controls import single_measurement_controls
from components.single_measurement_metrics import display_taguchi_metrics

from calculations.taguchi_loss import (
    calculate_taguchi_loss, 
    loss_function,
    generate_loss_curve,
    calculate_loss_at_characteristic
)

def display_single_measurement():

    st.markdown("## The Economic Loss of a Single Measurement")

    # Instructions
    with st.expander("Click to view instructions"):
        with open("content/single_measurement_instructions.md", "r", encoding="utf-8") as f:
            st.markdown(f.read())

    # Calculating economic loss
    with st.expander("Click to learn how the economic loss for a single measurement is calculated "):
        with open("content/single_measurement_calculations.md", "r", encoding="utf-8") as f:
            content = f.read()#st.markdown(f.read())

        image_map = {
            "[FIGURE_1]": "figures/EQ_loss_function.png",
            "[FIGURE_2]": "figures/EQ_numeric_constant_K.png",
        }

        render_markdown_with_images(content, image_map, image_width=1200)

    # Quiz questions
    # from components.quiz import display_quiz


    with st.expander(
        "Click to answer questions about the economic loss of a single measurement"
    ):
        display_quiz(
            "content/single_measurement_questions.md",
            "single_measurement"
        )

    st.divider()

    # Taguchi loss function controls
    usl, lsl, c_scrap, characteristic, round_value = single_measurement_controls()

    # Calculate taguchi loss 
    results = calculate_taguchi_loss(
        usl,
        lsl,
        c_scrap,
        characteristic,
    )

    # Show taguchi metrics
    show_annotation, show_spec_target_values = display_taguchi_metrics(
        results["tolerance"],
        results["target"],
        results["K"],
        results["expected_loss"],
        round_value,
    )

    df = generate_loss_curve(
        lsl,
        usl,
        characteristic,
        results["target"],
        results["K"],
        # overhang=None
    )

    y_at_characteristic = calculate_loss_at_characteristic(
        lsl,
        usl,
        characteristic,
        results["target"],
        results["K"],
    )
    
    # Display loss function as a figure
    display_loss_chart(
        df,
        characteristic,
        y_at_characteristic,
        results["expected_loss"],
        usl,
        lsl,
        results["target"],
        round_value,
        show_annotation,
        show_spec_target_values,
    )