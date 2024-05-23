"""
This test module includes all the tests for the
module src.model_training
"""
# Import Standard Modules
import numpy as np
import pytest

# Import Package Modules
from src.model_training.model_training_utils import (
    compute_regression_metrics,
    compute_multi_classification_metrics
)


@pytest.mark.parametrize('y_predicted, y_true, expected_metrics', [
    ([10, 20, 30], [12, 18, 24], [3.83, 14.67, 3.33, 0.18, 0.39])
])
def test_compute_regression_metrics(y_predicted: np.ndarray,
                                    y_true: np.ndarray,
                                    expected_metrics: np.ndarray,
                                    fixture_regression_metrics: list) -> bool:
    """
    This function tests the function src.model_training.model_training_utils.compute_regression_metrics
    whether the regression metrics are calculated correctly.

    Args:
        y_predicted: np.ndarray of predicted values
        y_true: np.ndarray of true values
        expected_metrics: np.ndarray of expected regression metrics values
        fixture_regression_metrics: list of metrics

    Returns:
    """

    # Apply the function to test and compute the metrics
    metrics = compute_regression_metrics(y_predicted, y_true, fixture_regression_metrics)

    # Reshaping metrics for comparison
    metrics = metrics.values.reshape(1, -1)[0]

    assert np.array_equal(metrics, expected_metrics)


@pytest.mark.parametrize('y_predicted, y_true, expected_metrics', [
    ([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
     [[0, 1, 0], [0, 0, 1], [0, 0, 1], [1, 0, 0], [1, 0, 0]],
     [0.2, 0.2, 0.2, 0.2, 0.4])
])
# TODO: Refactor with the probabilities
def test_compute_multi_classification_metrics(y_predicted: np.ndarray,
                                              y_true: np.ndarray,
                                              expected_metrics: np.ndarray,
                                              fixture_multi_classification_metrics: list) -> bool:
    """
    This function tests the function src.model_training.model_training_utils.compute_multi_classification_metrics
    whether the multi-classification metrics are calculated correctly.

    Args:
        y_predicted: np.ndarray of predicted values
        y_true: np.ndarray of true values
        expected_metrics: np.ndarray of expected multi-classification metrics values
        fixture_multi_classification_metrics: list of metrics

    Returns:
    """

    # Apply the function to test and compute the metrics
    metrics = compute_multi_classification_metrics(y_predicted, y_true, fixture_multi_classification_metrics)

    # Reshaping metrics for comparison
    metrics = metrics.values.reshape(1, -1)[0]

    assert np.array_equal(metrics, expected_metrics)
