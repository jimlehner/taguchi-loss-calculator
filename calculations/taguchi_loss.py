import numpy as np
import pandas as pd

def calculate_taguchi_loss(USL, LSL, c_scrap, characteristic):
    tolerance = USL - LSL
    target = (USL + LSL) / 2
    K = c_scrap / (USL - target) ** 2
    loss = K * (characteristic - target) ** 2

    return {
        "tolerance": tolerance,
        "target": target,
        "K": K,
        "expected_loss": loss,
    }


def loss_function(x_values, lsl, usl, target, tolerance):
    """
    Calculate Taguchi loss across a range of values.
    """

    x = np.array(x_values)

    loss = np.where(
        x <= lsl,
        tolerance * (target - lsl) ** 2,
        np.where(
            x >= usl,
            tolerance * (usl - target) ** 2,
            tolerance * (x - target) ** 2,
        ),
    )

    return loss

def generate_loss_curve(
    lsl,
    usl,
    characteristic,
    target,
    k,
    overhang=None
):
    """
    Generate x-values and loss values for the Taguchi loss curve.
    """
    if overhang is None:
        overhang=1
        
    # x_min = min(lsl - 1, characteristic - 1)
    # x_max = max(usl + 1, characteristic + 1)

    x_min = min(lsl - overhang, characteristic - 1)
    x_max = max(usl + overhang, characteristic + 1)

    x_values = pd.Series(
        np.arange(x_min, x_max, 0.05)
    )

    loss_values = loss_function(
        x_values,
        lsl,
        usl,
        target,
        k,
    )

    df = pd.DataFrame(
        {
            "x": x_values,
            "loss": loss_values,
        }
    )

    return df


def calculate_loss_at_characteristic(
    lsl,
    usl,
    characteristic,
    target,
    k,
):
    """
    Calculate the loss value at the measured characteristic value.
    """

    if characteristic < lsl:
        return k * (target - lsl) ** 2

    elif characteristic > usl:
        return k * (usl - target) ** 2

    else:
        return k * (characteristic - target) ** 2