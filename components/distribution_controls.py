import streamlit as st


def distribution_inputs():

    uploaded_file = st.file_uploader(
        "Upload a CSV file",
        type="csv"
    )

    if uploaded_file is not None:

        return {
            "source": "upload",
            "file": uploaded_file,
        }

    st.write(
        "No file uploaded — enter distribution parameters below:"
    )

    col1, col2 = st.columns(2)

    with col1:
        mean = st.number_input(
            "Mean",
            value=31.07,
            step=0.01,
            format="%.2f",
            key="mean"
        )

    with col2:
        std = st.number_input(
            "Standard Deviation",
            min_value=0.01,
            value=0.69,
            step=0.01,
            format="%.2f",
            key="std"
        )

    return {
        "source": "manual",
        "mean": mean,
        "std": std,
    }

import streamlit as st


def distribution_loss_controls():

    col1, col2, col3, col4 = st.columns(4)

    usl = col1.number_input(
        "Enter Upper Spec Limit (USL)",
        min_value=0.00,
        value=33.00,
        step=0.01,
        format="%.2f",
        key="USL_dist",
        help="Upper Specification Limit defined by the customer."
    )

    lsl = col2.number_input(
        "Enter Lower Spec Limit (LSL)",
        min_value=0.00,
        value=27.00,
        step=0.01,
        format="%.2f",
        key="LSL_dist",
        help="Lower Specification Limit defined by the customer."
    )

    c_scrap = col3.number_input(
        "Enter Cost of Scrap ($)",
        min_value=0.00,
        value=5.00,
        step=0.01,
        format="%.2f",
        key="c_scrap_dist",
    )

    round_value = col4.number_input(
        "Enter Rounding Value",
        min_value=0,
        value=2,
        key="round_value_dist",
    )


    show_annotation = col1.checkbox(
        "Show Annotation",
        value=True,
        key="show_annotation_dist"
    )

    show_spec_target = col2.checkbox(
        "Show Spec & Target Values",
        value=False,
        key="show_spec_target_dist"
    )

    show_process_limits = col3.checkbox(
        "Show Process Limits",
        value=False,
        key="show_process_limits_dist"
    )

    n_bins = col4.slider(
        "Number of histogram bins",
        min_value=5,
        max_value=100,
        value=30,
        step=1,
        key="histogram_bins_dist"
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
        round_value,
        # overhang,
        show_annotation,
        show_spec_target,
        show_process_limits,
        n_bins,
    )