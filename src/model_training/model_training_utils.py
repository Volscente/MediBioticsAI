"""
The module contains utility function for the Model Training pipeline
"""
# Import Standard Libraries
import os
import pathlib
import pandas as pd
import numpy as np
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    mean_absolute_percentage_error,
    r2_score
)

# Import Package Modules
from src.logging_module.logging_module import get_logger

# Setup logger
logger = get_logger(os.path.basename(__file__).split('.')[0],
                    pathlib.Path(__file__).parents[1] /
                    'logging_module' /
                    'log_configuration.yaml')


def compute_regression_metrics(y_predicted: np.ndarray,
                               y_true: pd.DataFrame,
                               metrics: list) -> pd.DataFrame:
    """
    Compute regression given metrics

    Args:
        y_predicted: Numpy array containing the predicted values
        y_true: Pandas dataframe containing the true values
        metrics: List of metrics to use to compute the regression metrics

    Returns:
        computed_metrics: Pandas dataframe containing the computed metrics
    """

    logger.info('compute_regression_metrics - Start')

    # Initialise return DataFrame
    computed_metrics = pd.DataFrame(columns=['Value'])

    # Set round precision
    round_precision = 4

    # Fetch the metrics to evaluate
    if 'RMSE' in metrics:
        # Compute RMSE
        rmse = round(mean_squared_error(y_true, y_predicted) ** 0.5, round_precision)
        computed_metrics.loc['RMSE'] = rmse

    if 'MSE' in metrics:
        # Compute MSE
        mse = round(mean_squared_error(y_true, y_predicted), round_precision)
        computed_metrics.loc['MSE'] = mse

    if 'MAE' in metrics:
        # Compute MAE
        mae = round(mean_absolute_error(y_true, y_predicted), round_precision)
        computed_metrics.loc['MAE'] = mae

    if 'MAPE' in metrics:
        # Compute MAPE
        mape = round(mean_absolute_percentage_error(y_true, y_predicted), round_precision)
        computed_metrics.loc['MAPE'] = mape

    if 'R2 Score' in metrics:
        # Compute R2 Score
        r2_score_value = round(r2_score(y_true, y_predicted), round_precision)
        computed_metrics.loc['R2 Score'] = r2_score_value

    logger.info('compute_regression_metrics - Compute metrics %s', computed_metrics)

    logger.info('compute_regression_metrics - End')

    return computed_metrics