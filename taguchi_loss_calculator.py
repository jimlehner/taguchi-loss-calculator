import pandas as pd
import numpy as np
import plotly.express as px # Interactive charts
import plotly.graph_objects as go
import streamlit as st
from PIL import Image

im = "📉"
st.set_page_config(
    page_title="Expected Loss Calculator",
    page_icon=im,
    initial_sidebar_state='collapsed',
    layout="wide"
)

st.title("Taguchi Loss Calculator")
st.markdown("### A project from [The Broken Quality Initiative](https://www.brokenquality.com/)")

st.markdown(
    """
    The Taguchi loss calculator allows users to calculate the economic loss due to poor quality in accordance with the Taguchi loss function.
    By selecting the tabs below, loss can be calculated for a single measurement or a distribution of measurements.
    """)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("# About the project")
    st.markdown(
        """
        The Taguchi Loss Calculator is part of a larger body of work called [**The Broken Quality Initiative**](https://www.brokenquality.com/). This 
        initiative teaches engineers how to reduce costs and improve quality by understanding variation. The Taguchi loss function plays a seminal role 
        in this task. It serves as a more robust and accurate alternative to the "goalpost" methodology that has dominated industry since the late 19th century.

        To learn more about the Taguchi loss function and build your understanding of variation visit [BrokenQuality.com](https://www.brokenquality.com/taguchi-loss-function).
        """
    )

    st.image("figures/Broken_quality_logo.png", use_container_width=True)

    st.markdown("# About the author")
    st.markdown(
        """
        [Jim Lehner](https://www.linkedin.com/in/jim-lehner/) is a graduate of Worcester Polytechnic Institute (WPI), with an undergraduate degree in mechanical engineering and a graduate degree in 
        manufacturing engineering. His professional experience and personal interests that place him at the confluence of manufacturing, data analytics, mechanical 
        engineering, and quality improvement. This has allowed Jim to reduced costs and improved quality in the automotive, medical device, aerospace, and defense 
        industries. The unifying feature to Jim's success, regardless of the industry, is his hands-on mentality and deep understanding of variation.
        """
    )
    st.markdown("# Contact")
    st.markdown(
        """
        Have questions or want to collaborate? Email James.Lehner@gmail.com or QualityIsBroken@gmail.com
        """
    )

    st.markdown("# The Socials")
    st.markdown(
        """
        [Linkedin](https://www.linkedin.com/in/jim-lehner/)
        [Substack](https://substack.com/@jimlehner)
        [BlueSky](https://bsky.app/profile/lehnro.bsky.social)
        """
    )

    st.markdown("# Website")
    st.markdown(
        """
        [BrokenQuality.com](www.BrokenQuality.com)
        """
    )

# --- TAB SELECTION ---
tab1, tab2, tab3 = st.tabs(["Overview", "Loss for a single measurement", "Loss for a distribution of measurements"])

# --- TAB1: OVERVIEW ---
with tab1:
    st.markdown("## An introduction to the Taguchi loss function")

    st.markdown(
        """
        The Taguchi loss calculator allows users to calculate loss due to poor quality using the Taguchi loss function. This high-fidelity, incremental model of 
        loss due to poor quality is governed by a quadratic function within the specification limits. It states that product of the highest quality is produced as the parabolic vertex (target) 
        with incremental losses incurred as a quality or performance characteristics deviates from the target. These losses increase quadratically until they reach 
        the specification limits, at which point the maximum loss due to poor quality is incurred (see Figure 1). In instances where rework can be performed, a portion of the loss can 
        be recovered. In instances where a part must be scrapped, the full loss is realized.
        """
    )

    _, col_mid, _ = st.columns([0.5, 2, 0.5])

    with col_mid:
        st.image("figures/Fig_2_quadratic_loss_function.png", use_container_width=True, 
                 caption="Figure 1. The Taguchi concept of economic loss due to poor quality is governed by a quadratic loss function within some region close to the target."  )
    
    st.markdown(
        """
        The Taguchi loss function is a practical alternative to the conformance to specification (spec) model of quality that has dominated industry 
        since the late 19th century. As shown in Figure 2, conformance to spec, also called the “goalpost" approach, assumes that all 
        values that fall within the spec limits are good and any that fall outside of them are bad.

        The low fidelity, binary model of loss created by conformance to spec, while a step forward for its time, is a liability today. It 
        promotes efforts that are good enough instead of promoting efforts of continuous improvement that yield products of world-class 
        quality. It constrains the data-rich manufacturing environments of the 21st century to the data-impoverished environments of the 19th.
        """
    )

    _, col_mid, _ = st.columns([0.5, 2, 0.5])

    with col_mid:
        st.image("figures/Fig_1_square_loss_function.png", use_container_width=True,
                caption="Figure 2. The conformance to specification concept of economic loss due to poor quality is governed by a square loss function.")

    st.markdown(
        """
        The Taguchi loss function, while not perfect, is a more robust alternative to the traditional conformance-to-spec approach. It is a more accurate 
        model of loss due to poor quality that reflects the realities of modern manufacturing ecosystems.

        To learn more about the Taguchi loss function visit [BrokenQuality.com/taguchi-loss-function](brokenquality.com/taguchi-loss-function). 
        """
    )

# --- TAB2: LOSS FOR A SINGLE PART ---
with tab2:
    st.markdown("## Instructions")
    st.markdown(
            """
            To calculate the loss due to poor quality for a measurement, provide the Upper Specification Limit (USL), Lower Specification Limit (LSL),
            cost of scrap, and the measured value for the performance or quality characteristic below.
            
            As a default, the USL is 33 units, the LSL is 27 units, the cost of scrap is \$5.00, and the measured quality characteristic
            is 28 units. Given these parameters, the tolerance is 6 units, the target is 30 units, the value for K is \$0.56, and the expected loss is 
            $2.22.

            Note that, although this model uses symmetrical specification limits, the Taguchi loss function can also be applied when working
            with one-sided (asymmetrical) limits.  
            """
        )

    # st.markdown("## Calculations")
    with st.expander("Click to learn more about how the expected loss for a single measurement is calculated"):
        st.markdown(
            """
            For an individual quality or performance characteristic (i.e., one measurement from one part), the Taguchi loss function is written as:
            """
        )

        st.image("figures/EQ_loss_function.png", use_container_width=True)

        st.markdown(
            """
            Here, *L(x)* is the loss function, *K* is a numeric constant expressed in dollars per unit squared, *x* is the measured quality or 
            performance characteristic, and *T* is the target value.

            Of the terms that compose the individual loss function, the numeric constant *K* is the only one that requires calculation. This is 
            achieved using the formula:
            """
        )

        st.image("figures/EQ_numeric_constant_K.png", use_container_width=True)

        st.markdown(
            """
            Here, *C_scrap* is the monetary cost of scrapping a part, *x_scrap* is the value of a quality or performance characteristic that requires 
            a part be scrapped (i.e., the Upper Spec Limit or the Lower Spec Limit), and *T* is the target value for the performance or quality characteristic.
            """
        )

    # st.markdown("## Questions")
    with st.expander("Click to answer questions about the expected loss for a single measurement"):
        answer_1 = st.radio("What is the expected loss due to poor quality when the measured value for the quality characteristic is 29 units?",
                            index=None,
                            options=["$3.00", "$0.00", "$0.56", "$1.50"],
                            key="radio_1"
                            )
        
        if answer_1 is None:
            pass 
        elif answer_1 in ["$3.00", "$0.00", "$1.50"]:
            st.error("Incorrect, try again! ❌")
        else:
            st.success("Correct! As the value of a quality or performance characteristic approaches the target, loss due to poor quality decrease. ✅")

        answer_2 = st.radio("What is the expected loss due to poor quality when the cost of scrap is \$7.50 and the measured value for the quality characteristic is 31.75 units?",
                            index=None,
                            options=["$0.00", "$7.00", "$0.56", "$2.55"],
                            key="radio_2"
                            )
        
        if answer_2 is None:
            pass 
        elif answer_2 in ["$0.00", "$7.00", "$0.56"]:
            st.error("Incorrect, try again! ❌")
        else:
            st.success("Correct! When the cost of scrap is \$7.50 and the measured quality or performance characteristic is 31.75 units, the expected loss is $2.55. ✅")

        answer_3 = st.radio("What is the expected loss due to poor quality when the cost of scrap is \$7.50, the value for the quality characteristic is 31.75 units, " \
        "the USL is 36 units, and the LSL is 25 units?",
                            index=None,
                            options=["$10.00", "$0.39", "$7.50", "$0.56"],
                            key="radio_3"
                            )
        
        if answer_3 is None:
            pass 
        elif answer_3 in ["$10.00", "$7.50", "$0.56"]:
            st.error("Incorrect, try again! ❌")
        else:
            st.success("Correct! When the cost of scrap is \$7.50, the measured quality or performance characteristic is 31.75 units, the USL is 36 and the LSL is 25, " \
                       "the expected loss is $0.39. The wider specification limits increase the process 'elbow room' decreasing the loss. ✅")

    st.divider()

    col1, col2, col3, col4, col5 = st.columns(5)

    USL = col1.number_input(label="Enter Upper Spec Limit (USL)", 
                    min_value=0.00,
                    value=33.00,
                    step=0.01,
                    format="%.2f")
    
    LSL = col2.number_input(label="Enter Lower Spec Limit (LSL)", 
                    min_value=0.00,
                    value=27.00,
                    step=0.01,
                    format="%.2f")
    
    c_scrap = col3.number_input(label="Enter Cost of Scrap ($)", 
                    min_value=0.00,
                    value=5.00,
                    step=0.01,
                    format="%.2f")
    
    characteristic = col4.number_input(label="Enter Value for Quality Characteristic", 
                    min_value=0.00,
                    value=28.00,
                    step=0.01,
                    format="%.2f")

    # Calculate tolerance and target
    Tolerance = USL-LSL
    Target = (Tolerance/2) + LSL

    # Calculate K
    K = c_scrap/(USL - Target)**2

    # Calculate loss
    loss = K * (characteristic - Target) ** 2

    round_value = col5.number_input(label="Enter Rounding Value",
                                    min_value=0,
                                    value=2)
    col1.metric("Tolerance", f"{Tolerance:.{round_value}f}")
    col2.metric("Target", f"{Target:.{round_value}f}")
    col3.metric("K", f"${K:.{round_value}f}")
    col4.metric("Expected Loss", f"${loss:.{round_value}f}")

    show_annotation_1 = col1.checkbox("Show Annotation", value=True)
    show_annotation_2 = col2.checkbox("Show Spec Limit & Target Values", value=False)

    # Create function for loss function
    def loss_function(x_values, LSL, USL, Target, Tolerance):
        x = np.array(x_values)
        loss = np.where(x <= LSL, Tolerance * (Target - LSL)**2,
                np.where(x >= USL, Tolerance * (USL - Target)**2,
                        Tolerance * (x - Target)**2))
        return loss
    
    # Generate X_values using spec limits
    x_min = min(LSL - 1, characteristic - 1)
    x_max = max(USL + 1, characteristic + 1)

    x_values = pd.Series(np.arange(x_min, x_max, 0.05))

    loss_function_values = loss_function(x_values, LSL, USL, Target, Tolerance)

    df = pd.DataFrame({"x": x_values, "loss": loss_function_values})

    # Calculate y value at characteristic value
    if characteristic < LSL:
        y_at_characteristic = Tolerance * (Target - LSL) ** 2
    elif characteristic > USL:
        y_at_characteristic = Tolerance * (USL - Target) ** 2
    else:
        y_at_characteristic = Tolerance * (characteristic - Target) ** 2

    # Create figure
    fig = px.line(df, x="x", y="loss")

    fig.update_traces(line_color="red", line_width=3)
    fig.update_layout(
        showlegend=False,
        height=600, # in pixels
        yaxis_title="Loss Due to Poor Quality ($)",
        xaxis_title="Quality Characteristic"
    )

    if show_annotation_1:
        fig.add_annotation(
            x=characteristic,
            y=y_at_characteristic,
            text=f"Characteristic Value: {characteristic:.{round_value}f}<br>Expected Loss: ${loss:.{round_value}f}",
            showarrow=True,
            arrowcolor="rgba(0,0,0,0)",  # invisible arrow
            ax=0,
            ay=-40,    # reduce this to bring label closer
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
        fig.add_vline(x=USL, annotation_text=f"USL: {USL:.{round_value}f}", **vline_style)
        fig.add_vline(x=LSL, annotation_text=f"LSL: {LSL:.{round_value}f}", **vline_style)
        fig.add_vline(x=Target, annotation_text=f"Target: {Target:.{round_value}f}", **vline_style)
    else:
        fig.add_vline(x=USL, annotation_text="USL", **vline_style)
        fig.add_vline(x=LSL, annotation_text="LSL", **vline_style)
        fig.add_vline(x=Target, annotation_text="Target", **vline_style)

    # Add scatter point at characteristic
    fig.add_scatter(
        x=[characteristic], 
        y=[y_at_characteristic],
        mode="markers",
        zorder=10,
        marker=dict(
            size=30, 
            color="steelblue",
            line=dict(color="black", width=1))
    )


    _, col_mid, _ = st.columns([0.5, 3, 0.5])

    with col_mid:
        st.plotly_chart(fig, use_container_width=True)


# --- TAB3: LOSS FOR A DISTRIBUTION ---
with tab3:
    st.markdown("## Instructions")
    st.markdown(
        """
        To calculate the loss due to poor quality for a distribution of measurements, you can either:
        
        1. Drag and drop a csv file then select the column containing the process data or
        2. Provide the mean and standard deviation that is representative of your process data.
        
        After selecting one of the above options, enter the Upper Specification Limit (USL), Lower Specification Limit (LSL), and cost of scrapping a part. 
        With these values entered, the expected average loss per unit will be calculated.
        
        As a default, the mean is 31.07 units and the standard deviation is 0.69 units, while the USL is 33 units, the LSL is 27 units, and the cost of scrap 
        is \$5.00. Given these parameters, the tolerance is 6 units, the target is 30 units, the value for K is \$0.56, and the average expected loss per unit 
        (E{L(x)}) is $1.87.
        
        Note that, although this model uses symmetrical specification limits, the Taguchi loss function can also be applied with one-sided (asymmetrical) 
        limits.
        """
    )
    # st.markdown("## Calculations")
    with st.expander("Click to learn more about how the expected loss per unit for a distribution is calculated"):
        st.markdown(
            """
            The purpose and point of manufacturing is to produce multiples of the same part that are functionally the same. Thus, calculating 
            the loss due to poor quality for a single measurement is rarely a practical approach in industry. To determine the likelihood that 
            a particular value for a quality or performance characteristic will occur, the distribution of the values of X must be considered. 
            
            If we assume a manufacturing process produced 100 parts, each of these parts will have a unique quality characteristic, X = x, and 
            an associated loss that can be described by L(x). By summing the individual losses for the 100 parts, an average loss per unit of 
            production can be obtained. This is expressed by the formula:

            """
        )

        st.image("figures/EQ_average_taguchi_loss.png", use_container_width=True)

        st.markdown(
            """
            Here, *E{L(x)}* is the expected average loss per unit, *K* is a numeric constant expressed in dollars per unit squared, *X-bar* is 
            the mean of the distribution, *T* is the target value, and *σ* is the standard deviation of the distribution.

            Of the terms that compose this loss function, the numeric constant *K* is the only one that requires calculation. This is 
            achieved using the formula:
            """
        )

        st.image("figures/EQ_numeric_constant_K.png", use_container_width=True)

        st.markdown(
            """
            Here, *C_scrap* is the monetary cost of scrapping a part, *x_scrap* is the value of a quality or performance characteristic when a part is
            scrapped (i.e., the Upper Spec Limit or the Lower Spec Limit), and *T* is the target value for the performance or quality characteristic.
            """
        )

    # st.markdown("## Questions")
    with st.expander("Click to answer questions about the expected loss per unit for a distribution"):
        # Question 1
        answer_1 = st.radio("What is the expected loss per unit (average) when the mean of the distribution is 32.24 units, the standard deviation is 1.12 units, "
                            "the USL is 33 units, the LSL is 27 units, and the cost of scrap is \$5.00?",
                            index=None,
                            options=["$3.45", "$505.56", "$4.45", "$20.93"],
                            key="radio_4"
                            )
        
        if answer_1 is None:
            pass 
        elif answer_1 in ["$3.45", "$1.00", "$505.56"]:
            st.error("Incorrect, try again! ❌")
        else:
            st.success("Correct! As the mean deviates from the target and the standard deviation increases, the expected average loss per unit increases to \$20.93. ✅")

        # Question 3
        answer_3 = st.radio("What is the expected average loss per unit when the mean of the distribution is 30.25 units and the standard deviation is 0.5 units?",
                            index=None,
                            options=["$6.62", "$0.38", "$10.15", "$2.55"],
                            key="radio_6"
                            )
        
        if answer_3 is None:
            pass 
        elif answer_3 in ["$6.62", "$10.15", "$2.55"]:
            st.error("Incorrect, try again! ❌")
        else:
            st.success("Correct! As the mean approaches the target and the standard deviation decreases, the expected average loss per unit also decreases. ✅")

        # Question 4
        answer_4 = st.radio("What is the expected average loss per unit when the mean of the distribution is 30.25 units, the standard deviation is 1.75 units, and "\
                            "the cost of scrap is \$7.50?",
                            index=None,
                            options=["$7.50", "$0.39", "$3.94", "$1.56"],
                            key="radio_7"
                            )
        
        if answer_4 is None:
            pass 
        elif answer_4 in ["$7.50", "$0.39", "$1.56"]:
            st.error("Incorrect, try again! ❌")
        else:
            st.success("Correct! Even though the mean of 31.25 units is close to the target, the large standard deviation increases the expected loss per unit to \$3.94." \
                    "This is why operating both **on-target** and with **minimum variance** are critical to producing products of world-class quality. ✅")

    st.divider()

    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

    if uploaded_file is not None:
        # Use uploaded data
        df = pd.read_csv(uploaded_file)
        column = st.selectbox("Select a column", df.columns)
        data = df[column].dropna()

        mean = data.mean()
        std = data.std()

    else:
        # Manual entry
        st.write("No file uploaded — enter distribution parameters below:")
        
        col1, col2 = st.columns(2)
        with col1:
            mean = st.number_input("Mean", value=31.07, step=0.01, format="%.2f", key="mean")
        with col2:
            std = st.number_input("Standard Deviation", min_value=0.01, value=0.69, step=0.01, format="%.2f", key="std")
        
        # Generate normal distribution
        @st.cache_data
        def generate_data(mean, std):
            np.random.seed(42)
            return np.random.normal(loc=mean, scale=std, size=1000)
        data = generate_data(mean, std)

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    USL_d = col1.number_input(label="Enter Upper Spec Limit (USL)", 
                    min_value=0.00,
                    value=33.00,
                    step=0.01,
                    format="%.2f",
                    key="USL_d")
    
    LSL_d = col2.number_input(label="Enter Lower Spec Limit (LSL)", 
                    min_value=0.00,
                    value=27.00,
                    step=0.01,
                    format="%.2f",
                    key="LSL_d")
    
    c_scrap_d = col3.number_input(label="Enter Cost of Scrap ($)", 
                    min_value=0.00,
                    value=5.00,
                    step=0.01,
                    format="%.2f",
                    key="c_scrap_d")
    
    round_value_2 = col4.number_input(label="Enter Rounding Value",
                                    min_value=0,
                                    value=2,
                                    key="round_value_2")

    # Calculate tolerance and target
    Tolerance_d = USL_d-LSL_d
    Target_d = (Tolerance_d/2) + LSL_d

    # Calculate K
    K_d = c_scrap_d/(USL_d - Target_d)**2

    # Calculate loss
    loss_d = K_d * ((mean - Target_d) ** 2 + (std) ** 2)

    col1.metric("Tolerance", f"{Tolerance_d:.{round_value_2}f}")
    col2.metric("Target", f"{Target_d:.{round_value_2}f}")
    col3.metric("K", f"${K_d:.{round_value_2}f}")
    col4.metric("Average Loss", f"${loss_d:.{round_value_2}f}")

    show_annotation_3 = col1.checkbox("Show Annotation", value=True, key="show_annotation_3")
    show_annotation_4 = col2.checkbox("Show Spec Limit & Target Values", value=False, key="show_annotation_4")
    n_bins = col3.slider("Number of histogram bins", min_value=5, max_value=100, value=30, step=1)
    
    # Generate X_values using spec limits  
    x_min = min(LSL_d - 1, mean - 1)
    x_max = max(USL_d + 1, mean + 1)

    x_values_d = pd.Series(np.arange(x_min, x_max, 0.05))

    loss_function_values_d = loss_function(x_values_d, LSL_d, USL_d, Target_d, Tolerance_d)

    df_distribution = pd.DataFrame({"x": x_values_d, "loss": loss_function_values_d})

    # Calculate y value at characteristic value
    if mean < LSL_d:
        y_at_mean = Tolerance_d * (Target_d - LSL_d) ** 2
    elif mean > USL_d:
        y_at_mean = Tolerance_d * (USL_d - Target_d) ** 2
    else:
        y_at_mean = Tolerance_d * (mean - Target_d) ** 2

    fig = go.Figure()

    # Histogram on secondary axis (renders behind)
    fig.add_trace(go.Histogram(
        x=data,
        opacity=0.5,
        marker_color="steelblue",
        marker_line_color="black",
        marker_line_width=1,
        nbinsx=n_bins,
        yaxis="y2"
    ))

    # Loss function line on primary axis
    fig.add_trace(go.Scatter(
        x=x_values_d, y=loss_function_values_d,
        mode="lines",
        line=dict(color="red", width=3)
    ))

    # Scatter point at mean
    fig.add_trace(go.Scatter(
        x=[mean],
        y=[y_at_mean],
        mode="markers",
        zorder=10,
        marker=dict(size=30, color="steelblue", line=dict(color="black", width=1))
    ))

    fig.update_layout(
        showlegend=False,
        height=500,
        xaxis_title="Quality Characteristic",
        yaxis=dict(showticklabels=True, showgrid=True, zeroline=False, title="Loss Due to Poor Quality ($)"),
        yaxis2=dict(showticklabels=False, showgrid=False, zeroline=False, overlaying="y", side="right")
    )

    vline_style = dict(
        line_dash="dash",
        line_color="black",
        line_width=3,
        annotation_position="top",
        annotation_font_color="black",
        annotation_font_size=16
    )

    if show_annotation_4:
        fig.add_vline(x=USL_d, annotation_text=f"USL: {USL_d:.2f}", **vline_style)
        fig.add_vline(x=LSL_d, annotation_text=f"LSL: {LSL_d:.2f}", **vline_style)
        fig.add_vline(x=Target_d, annotation_text=f"Target: {Target_d:.2f}", **vline_style)
    else:
        fig.add_vline(x=USL_d, annotation_text="USL", **vline_style)
        fig.add_vline(x=LSL_d, annotation_text="LSL", **vline_style)
        fig.add_vline(x=Target_d, annotation_text="Target", **vline_style)

    if show_annotation_3:
        fig.add_annotation(
            x=mean,
            y=y_at_mean,
            text=f"Mean: {round(mean, round_value)}<br>Stdev: {round(std, round_value)}<br>Ave. Loss: ${round(loss_d, round_value)}",
            showarrow=True,
            arrowcolor="rgba(0,0,0,0)",
            ax=0,
            ay=-50,
            font=dict(color="black", size=18),
            bgcolor="white",
            bordercolor="black",
            borderwidth=1,
            align="center"
        )

    _, col_mid, _ = st.columns([0.5, 3, 0.5])

    with col_mid:

        st.plotly_chart(fig, use_container_width=True)



