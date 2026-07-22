import numpy as np
import pandas as pd

from calculations.taguchi_loss import loss_function

def calculate_overhang(data, lsl, usl):
    """
    Calculate chart overhang based on the relationship
    between the data range and specification limits.
    """

    data_min = data.min()
    data_max = data.max()

    lower_distance = abs(lsl - data_min)
    upper_distance = abs(data_max - usl)

    overhang = max(lower_distance, upper_distance)

    # Add a small buffer
    return max(overhang, 1.0)

def calculate_loss_curve(
    lsl,
    usl,
    target,
    tolerance,
    data,
):
    """
    Generate Taguchi loss curve data for a distribution.
    """

    data_min = data.min()
    data_max = data.max()

    # Extend curve to include both specs and data
    x_min = max(
        0,
        min(lsl, data_min)
    )

    x_max = max(
        usl,
        data_max
    )

    # Add small visual padding
    padding = (x_max - x_min) * 0.75

    x_min = max(0, x_min - padding)
    x_max = x_max + padding

    x_values = pd.Series(
        np.linspace(x_min, x_max, 500)
    )

    loss_values = loss_function(
        x_values,
        lsl,
        usl,
        target,
        tolerance,
    )

    df = pd.DataFrame(
        {
            "x": x_values,
            "loss": loss_values,
        }
    )

    # Calculate y-value at the mean
    mean = data.mean()

    if mean < lsl:
        y_at_mean = tolerance * (target - lsl) ** 2
    elif mean > usl:
        y_at_mean = tolerance * (usl - target) ** 2
    else:
        y_at_mean = tolerance * (mean - target) ** 2

    return {
        "df": df,
        "y_at_mean": y_at_mean,
    }

# def calculate_loss_curve(
#     lsl,
#     usl,
#     target,
#     tolerance,
#     mean,
# ):
#     """
#     Generate Taguchi loss curve data for a distribution.
#     """

#     # Generate x-values using spec limits and mean
#     # x_min = min(lsl - 1, mean - 1)
#     # x_max = max(usl + 1, mean + 1)

#     x_min = max(
#         0,
#         min(lsl - overhang, mean - 1)
#     )

#     x_max = max(
#         usl + overhang,
#         mean + 1
#     )

#     x_values = pd.Series(
#         np.arange(x_min, x_max, 0.005)
#     )

#     # Calculate loss curve
#     loss_values = loss_function(
#         x_values,
#         lsl,
#         usl,
#         target,
#         tolerance,
#     )

#     df = pd.DataFrame(
#         {
#             "x": x_values,
#             "loss": loss_values,
#         }
#     )

#     # Calculate y-value at mean
#     if mean < lsl:
#         y_at_mean = tolerance * (target - lsl) ** 2

#     elif mean > usl:
#         y_at_mean = tolerance * (usl - target) ** 2

#     else:
#         y_at_mean = tolerance * (mean - target) ** 2

#     return {
#         "df": df,
#         "y_at_mean": y_at_mean,
#     }