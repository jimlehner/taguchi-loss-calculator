import plotly.express as px
import streamlit as st


def display_loss_chart(
    df,
    characteristic,
    y_at_characteristic,
    loss,
    usl,
    lsl,
    target,
    round_value,
    show_annotation_1,
    show_annotation_2,
):
    fig = px.line(
        df,
        x="x",
        y="loss"
    )

    fig.update_traces(
        line_color="red",
        line_width=3
    )

    fig.update_layout(
        showlegend=False,
        height=500,
        yaxis_title="Economic Loss ($)",
        xaxis_title="Quality Characteristic"
    )

    if show_annotation_1:
        fig.add_annotation(
            x=characteristic,
            y=y_at_characteristic,
            text=(
                f"Measured Value: {characteristic:.{round_value}f}"
                f"<br>Expected Loss: ${loss:.{round_value}f}"
            ),
            showarrow=True,
            arrowcolor="rgba(0,0,0,0)",
            ax=0,
            ay=-40,
            font=dict(color="black", size=18),
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
            align="center"
        )

    vline_style = dict(
        line_dash="dash",
        line_color="black",
        line_width=3,
        annotation_position="top",
        annotation_font_color="black",
        annotation_font_size=18
    )

    if show_annotation_2:
        fig.add_vline(
            x=usl,
            annotation_text=f"USL: {usl:.{round_value}f}",
            **vline_style
        )
        fig.add_vline(
            x=lsl,
            annotation_text=f"LSL: {lsl:.{round_value}f}",
            **vline_style
        )
        fig.add_vline(
            x=target,
            annotation_text=f"Target: {target:.{round_value}f}",
            **vline_style
        )

    else:
        fig.add_vline(
            x=usl,
            annotation_text="USL",
            **vline_style
        )
        fig.add_vline(
            x=lsl,
            annotation_text="LSL",
            **vline_style
        )
        fig.add_vline(
            x=target,
            annotation_text="Target",
            **vline_style
        )

    fig.add_scatter(
        x=[characteristic],
        y=[y_at_characteristic],
        mode="markers",
        marker=dict(
            size=30,
            color="steelblue",
            line=dict(color="black", width=1)
        )
    )

    _, col_mid, _ = st.columns([0.5, 3, 0.5])

    with col_mid:
        st.plotly_chart(
            fig,
            use_container_width=True
        )