import pandas as pd


def calculate_distribution_metrics(data):
    """
    Calculate distribution statistics and process limits.
    """

    mean = data.mean()
    std = data.std()

    moving_range = abs(data.diff())
    ave_mR = moving_range.mean()

    sigmaX = ave_mR / 1.128

    upl = mean + (2.660 * ave_mR)
    lpl = mean - (2.660 * ave_mR)

    return {
        "mean": mean,
        "std": std,
        "mR": moving_range,
        "ave_mR": ave_mR,
        "SigmaX": sigmaX,
        "UPL": upl,
        "LPL": lpl,
    }

def calculate_distribution_loss(
    usl,
    lsl,
    c_scrap,
    mean,
    std,
    sigmaX,
):
    """
    Calculate Taguchi loss components for a distribution.
    """

    tolerance = usl - lsl
    target = (usl + lsl) / 2

    k = c_scrap / (usl - target) ** 2

    average_loss = k * (
        (mean - target) ** 2 + std ** 2
    )

    loss_on_target_with_variance = k * std ** 2

    loss_off_target_predictable = k * (
        (mean - target) ** 2 + sigmaX ** 2
    )

    loss_on_target_predictable = k * sigmaX ** 2


    return {
        "tolerance": tolerance,
        "target": target,
        "k": k,
        "average_loss": average_loss,
        "loss_on_target_with_variance": loss_on_target_with_variance,
        "loss_off_target_predictable": loss_off_target_predictable,
        "loss_on_target_predictable": loss_on_target_predictable,
    }