import streamlit as st


def display_distribution_summary(
    average_loss,
    loss_on_target_with_variance,
    loss_off_target_predictable,
    loss_on_target_predictable,
    round_value,
):
    """
    Display a summary of the economic loss scenarios.
    """

    with st.expander("Click for a summary of the economic loss"):

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Average Loss\n(Current Operation)",
            f"${average_loss:.{round_value}f}",
            help="The expected loss for the current process based on its mean and variation.",
        )

        col2.metric(
            "On Target\n(Current Variation)",
            f"${loss_on_target_with_variance:.{round_value}f}",
            help="Expected loss if the process mean were centered on the target while the current variation remained unchanged.",
        )

        col3.metric(
            "Current Mean\n(Predictable Variation)",
            f"${loss_off_target_predictable:.{round_value}f}",
            help="Expected loss if the process retained its current mean but variation were reduced to the predictable level estimated from the moving range.",
        )

        col4.metric(
            "On Target\n(Predictable Variation)",
            f"${loss_on_target_predictable:.{round_value}f}",
            help="Expected loss for a process that is both centered on target and operating predictably.",
        )