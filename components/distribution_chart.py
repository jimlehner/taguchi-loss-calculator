import streamlit as st
import plotly.graph_objects as go


def display_distribution_loss_chart(
    data,
    df,
    mean,
    y_at_mean,
    usl,
    lsl,
    target,
    UPL,
    LPL,
    std,
    average_loss,
    n_bins,
    round_value,
    show_annotation,
    show_spec_target,
    show_process_limits,
):
    """
    Display histogram with Taguchi loss curve.
    """

    fig = go.Figure()


    # Histogram
    fig.add_trace(
        go.Histogram(
            x=data,
            opacity=0.5,
            marker_color="steelblue",
            marker_line_color="black",
            marker_line_width=1,
            nbinsx=n_bins,
            yaxis="y2",
        )
    )


    # Loss curve
    fig.add_trace(
        go.Scatter(
            x=df["x"],
            y=df["loss"],
            mode="lines",
            line=dict(
                color="red",
                width=3
            )
        )
    )


    # Mean point
    fig.add_trace(
        go.Scatter(
            x=[mean],
            y=[y_at_mean],
            mode="markers",
            marker=dict(
                size=30,
                color="steelblue",
                line=dict(
                    color="black",
                    width=1
                )
            )
        )
    )


    fig.update_layout(
        showlegend=False,
        margin=dict(t=20,b=0),
        height=500,
        xaxis_title="Quality Characteristic",
        yaxis=dict(
            showticklabels=True,
            showgrid=True,
            zeroline=False,
            title="Loss Due to Poor Quality ($)"
        ),
        yaxis2=dict(
            showticklabels=False,
            showgrid=False,
            zeroline=False,
            overlaying="y",
            side="right"
        )
    )


    spec_line_style = dict(
        line_dash="dash",
        line_color="black",
        line_width=3,
        annotation_position="top",
        annotation_font_color="black",
        annotation_font_size=16,
    )


    process_line_style = dict(
        line_dash="dash",
        line_color="red",
        line_width=3,
        annotation_position="bottom",
        annotation_font_color="black",
        annotation_font_size=16,
    )


    # Specification limits
    if show_spec_target:

        fig.add_vline(
            x=usl,
            annotation_text=f"USL: {usl:.{round_value}f}",
            **spec_line_style
        )

        fig.add_vline(
            x=lsl,
            annotation_text=f"LSL: {lsl:.{round_value}f}",
            **spec_line_style
        )

        fig.add_vline(
            x=target,
            annotation_text=f"Target: {target:.{round_value}f}",
            **spec_line_style
        )

    else:

        fig.add_vline(
            x=usl,
            annotation_text="USL",
            **spec_line_style
        )

        fig.add_vline(
            x=lsl,
            annotation_text="LSL",
            **spec_line_style
        )

        fig.add_vline(
            x=target,
            annotation_text="Target",
            **spec_line_style
        )


    # Mean annotation
    if show_annotation:

        fig.add_annotation(
            x=mean,
            y=y_at_mean,
            text=(
                f"Mean: {mean:.{round_value}f}"
                f"<br>Stdev: {std:.{round_value}f}"
                f"<br>Ave. Loss: ${average_loss:.{round_value}f}"
            ),
            showarrow=True,
            arrowcolor="rgba(0,0,0,0)",
            ax=0,
            ay=-50,
            font=dict(
                color="black",
                size=18
            ),
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
            align="center"
        )


    # Process limits
    if show_process_limits:

        fig.add_vline(
            x=UPL,
            annotation_text=f"UPL: {UPL:.{round_value}f}",
            **process_line_style
        )

        fig.add_vline(
            x=LPL,
            annotation_text=f"LPL: {LPL:.{round_value}f}",
            **process_line_style
        )


    _, col_mid, _ = st.columns([0.5, 3, 0.5])

    with col_mid:
        st.plotly_chart(
            fig,
            use_container_width=True
        )