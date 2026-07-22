import streamlit as st


def single_measurement_controls():

    col1, col2, col3, col4, col5 = st.columns(5)

    usl = col1.number_input(
        "Enter Upper Spec Limit (USL)",
        min_value=0.00,
        value=33.00,
        step=0.01,
        format="%.2f",
        help=(
            "The Upper Specification Limit (USL) is the largest acceptable value "
            "for the quality or performance characteristic as defined by the customer."
        )
    )

    lsl = col2.number_input(
        "Enter Lower Spec Limit (LSL)",
        min_value=0.00,
        value=27.00,
        step=0.01,
        format="%.2f",
        help=(
            "The Lower Specification Limit (LSL) is the smallest acceptable value "
            "for the quality or performance characteristic as defined by the customer."
        )
    )

    c_scrap = col3.number_input(
        "Enter Cost of Scrap ($)",
        min_value=0.00,
        value=5.00,
        step=0.01,
        format="%.2f",
        help="The cost of scrap is the cost incurred for scrapping a part."
    )

    characteristic = col4.number_input(
        "Enter Measured Value",
        min_value=0.00,
        value=28.00,
        step=0.01,
        format="%.2f",
        help=(
            "The measured value is the value for the quality or performance "
            "characteristic for which the economic loss is being calculated."
        )
    )

    round_value = col5.number_input(
        "Enter Rounding Value",
        min_value=0,
        value=2,
        help=(
            "The rounding value determines the number of decimal places used "
            "in the calculations and displayed on the chart."
        )
    )

    # overhang = st.slider(
    #     "Chart Overhang",
    #     min_value=0.0,
    #     max_value=5.0,
    #     value=1.0,
    #     step=0.1,
    # )

    return (
        usl,
        lsl,
        c_scrap,
        characteristic,
        round_value,
        # overhang
    )

    