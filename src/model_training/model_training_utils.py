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
    r2_score,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
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
                               metrics: list,
                               round_precision: int = 2) -> pd.DataFrame:
    """
    Compute regression given metrics

    Args:
        y_predicted: Numpy array containing the predicted values
        y_true: Pandas dataframe containing the true values
        metrics: List of metrics to use to compute the regression metrics
        round_precision: integer used to round precision (Default value = 2)

    Returns:
        computed_metrics: Pandas dataframe containing the computed metrics
    """

    logger.info('compute_regression_metrics - Start')

    # Initialise return DataFrame
    computed_metrics = pd.DataFrame(columns=['Value'])

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


def compute_multi_classification_metrics(y_predicted: np.ndarray,
                                         y_true: pd.DataFrame,
                                         metrics: list,
                                         round_precision: int = 2) -> pd.DataFrame:
    """
    Compute multi classification metrics

    Args:
        y_predicted: Numpy array containing the predicted values
        y_true: Pandas dataframe containing the true values
        metrics: List of metrics to use to compute the multi classification metrics
        round_precision: integer used to round precision (Default value = 2)

    Returns:
        computed_metrics: Pandas dataframe containing the computed metrics
    """

    logger.info('compute_multi_classification_metrics - Start')

    # Initialise return DataFrame
    computed_metrics = pd.DataFrame(columns=['Value'])

    # Fetch the metrics to evaluate
    if 'Accuracy' in metrics:
        # Compute Accuracy
        accuracy = round(accuracy_score(y_true, y_predicted), round_precision)
        computed_metrics.loc['Accuracy'] = accuracy

    if 'Precision' in metrics:
        # Compute Precision
        precision = round(precision_score(y_true, y_predicted, average='micro'), round_precision)
        computed_metrics.loc['Precision'] = precision

    if 'Recall' in metrics:
        # Compute Recall
        recall = round(recall_score(y_true, y_predicted, average='micro'), round_precision)
        computed_metrics.loc['Recall'] = recall

    if 'F1 Score' in metrics:
        # Compute F1 Score
        f1_score_value = round(f1_score(y_true, y_predicted, average='micro'), round_precision)
        computed_metrics.loc['F1 Score'] = f1_score_value

    if 'ROC AUC' in metrics:
        # Compute ROC AUC
        roc_auc_value = round(roc_auc_score(y_true, y_predicted, average='micro'), round_precision)
        computed_metrics.loc['ROC AUC'] = roc_auc_value

    logger.info('compute_multi_classification_metrics - Compute metrics %s', computed_metrics)

    logger.info('compute_multi_classification_metrics - End')

    return computed_metrics
