import streamlit as st


def display_taguchi_metrics(
    tolerance,
    target,
    k,
    expected_loss,
    round_value,
):
    """
    Display Taguchi loss calculation results.
    """
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    col1.metric(
        "Tolerance",
        f"{tolerance:.{round_value}f}",
        help=(
            "The tolerance is calculated by subtracting the Lower Specification "
            "Limit (LSL) from the Upper Specification Limit (USL)."
        )
    )

    col2.metric(
        "Target",
        f"{target:.{round_value}f}",
        help=(
            "The target is the ideal value of the performance or quality "
            "characteristic."
        )
    )

    col3.metric(
        "K",
        f"${k:.{round_value}f}",
        help=(
            "K is the numeric constant expressed in dollars per unit squared "
            "used in the Taguchi loss function."
        )
    )

    col4.metric(
        "Expected Loss",
        f"${expected_loss:.{round_value}f}",
        help=(
            "The expected loss is the estimated economic cost of producing a "
            "product or delivering a service that deviates from the target value."
        )
    )

    show_annotation = col5.checkbox(
            "Show Annotation",
            value=True,
            help="Displays the characteristic value and expected loss of the measured quality" \
            "or performance characteristic on the figure."
        )
    
    show_spec_target_values = col6.checkbox(
        "Show Spec & Target Values",
        value=True,
        help="Displays the values associated with the specifcation limits and target on the " \
        "figure."
        )

    return show_annotation, show_spec_target_values