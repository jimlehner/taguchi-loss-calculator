# Taguchi Loss Calculator

An interactive web application for calculating economic loss due to poor quality using the Taguchi loss function. Built as part of [The Broken Quality Initiative](https://www.brokenquality.com/).

---

## Overview

Try the live app at [taguchi-loss-calculator.streamlit.app](https://taguchi-loss-calculator.streamlit.app).

The Taguchi loss function is a high-fidelity, incremental model of economic loss due to poor quality. Unlike the traditional conformance-to-specification ("goalpost") approach — which treats all values within spec limits as equally "good" — the Taguchi loss function states that loss increases quadratically as a quality or performance characteristic deviates from the target value.

This app allows users to:
- Calculate the expected loss for a single measurement
- Calculate the expected average loss per unit for a distribution of measurements
- Visualize the loss function alongside a histogram of process data
- Test their understanding with interactive questions

---

## Features

- **Single measurement calculator** — calculate loss for one measurement given USL, LSL, cost of scrap, and the measured value
- **Distribution calculator** — calculate expected average loss per unit given a mean and standard deviation, or by uploading a CSV file
- **Interactive charts** — Plotly visualizations of the loss function with annotations for the characteristic value, spec limits, and target
- **Interactive questions** — multiple choice questions with instant feedback for both calculators
- **Configurable rounding** — adjustable decimal places for all displayed values

---

## Installation

### Requirements

```
streamlit
pandas
numpy
plotly
Pillow
```

Install dependencies:

```bash
pip install streamlit pandas numpy plotly Pillow
```

### Running the App

```bash
streamlit run taguchi_loss_calculator.py
```

---

## File Structure

```
├── taguchi_loss_calculator.py     # Main application file
├── requirements.txt               # Python dependencies
└── figures/                       # Images used in the app
    ├── Broken_quality_logo.png
    ├── Fig_1_square_loss_function.png
    ├── Fig_2_quadratic_loss_function.png
    ├── EQ_loss_function.png
    ├── EQ_numeric_constant_K.png
    └── EQ_average_taguchi_loss.png
```

---

## How to Use

### Tab 1: Overview
Provides an introduction to the Taguchi loss function and how it compares to the traditional conformance-to-specification approach.

### Tab 2: Loss for a Single Measurement
Enter the following parameters to calculate the expected loss for a single measurement:

| Input | Description | Default |
|---|---|---|
| USL | Upper Specification Limit | 33.00 |
| LSL | Lower Specification Limit | 27.00 |
| Cost of Scrap | Cost to scrap a nonconforming part | $5.00 |
| Quality Characteristic | The measured value | 28.00 |

The app calculates and displays the tolerance, target, numeric constant K, and expected loss. A chart of the loss function is shown with the measured value plotted as a point on the curve.

### Tab 3: Loss for a Distribution of Measurements
Provide process distribution parameters in one of two ways:

1. **Upload a CSV file** — select the column containing the process data
2. **Manual entry** — enter the mean and standard deviation directly

Then enter USL, LSL, and cost of scrap to calculate the expected average loss per unit. A histogram of the data is overlaid with the loss function curve.

---

## Formulas

### Loss for a Single Measurement

```
L(x) = K × (x - T)²
```

### Numeric Constant K

```
K = C_scrap / (x_scrap - T)²
```

### Expected Average Loss per Unit

```
E{L(x)} = K × [(X̄ - T)² + σ²]
```

Where:
- `L(x)` is the loss for a single measurement
- `E{L(x)}` is the expected average loss per unit
- `K` is the numeric constant ($/unit²)
- `x` is the measured quality or performance characteristic
- `T` is the target value
- `X̄` is the mean of the distribution
- `σ` is the standard deviation of the distribution
- `C_scrap` is the cost of scrapping a nonconforming part
- `x_scrap` is the spec limit (USL or LSL)

---

## About

This app is part of [The Broken Quality Initiative](https://www.brokenquality.com/), a body of work that teaches engineers how to reduce costs and improve quality by understanding variation.

To learn more about the Taguchi loss function, visit [BrokenQuality.com/taguchi-loss-function](https://www.brokenquality.com/taguchi-loss-function).

**Author:** [Jim Lehner](https://www.linkedin.com/in/jim-lehner/)
**Contact:** James.Lehner@gmail.com | QualityIsBroken@gmail.com
