"""
This test module includes all the fixtures necessary
for running PyTest tests
"""
# Import Standard Libraries
import pathlib
import pytest

# Import Package Modules
from src.general_utils.general_utils import read_configuration

# Read configuration file
configuration = read_configuration(pathlib.Path(__file__).parents[1]
                                   / 'configuration'
                                   / 'test_config.yaml')


@pytest.fixture
def fixture_numerical_data_transformations(
        test_numerical_data_transformations: dict = configuration['test_numerical_data_transformations']
) -> dict:
    """
    Fixture for a Dictionary Numerical Data Transformations with structure:
        <transformation_name>:
            include: <bool>
            module: <string module name>

    Args:
        test_numerical_data_transformations: dict of numerical data transformations

    Returns:
        test_numerical_data_transformations: dict of numerical data transformations
    """

    return test_numerical_data_transformations


@pytest.fixture
def fixture_categorical_data_transformations(
        test_categorical_data_transformations: dict = configuration['test_categorical_data_transformations']
) -> dict:
    """
    Fixture for a Dictionary Categorical Data Transformations with structure:
        <transformation_name>:
            include: <bool>
            module: <string module name>

    Args:
        test_categorical_data_transformations: dict of categorical data transformations

    Returns:
        test_categorical_data_transformations: dict of categorical data transformations
    """

    return test_categorical_data_transformations


@pytest.fixture
def fixture_regression_metrics(
        test_regression_metrics: list = configuration['test_regression_metrics']
) -> list:
    """
    Fixture for regression metrics list

    Args:
        test_regression_metrics: list of regression metrics

    Returns:
        test_regression_metrics: list of regression metrics
    """

    return test_regression_metrics


@pytest.fixture
def fixture_multi_classification_metrics(
        test_multi_classification_metrics: list = configuration['test_multi_classification_metrics']
) -> list:
    """
    Fixture for multi-classification metrics list

    Args:
        test_multi_classification_metrics: list of multi-classification metrics

    Returns:
        test_multi_classification_metrics: list of multi-classification metrics
    """

    return test_multi_classification_metrics


@pytest.fixture
def fixture_label_data_transformations(
        test_label_data_transformations: dict = configuration['test_label_data_transformations']
) -> dict:
    """
    Fixture for a Dictionary Label Data Transformations with structure:
        <transformation_name>:
            include: <bool>
            module: <string module name>

    Args:
        test_label_data_transformations: dict of label data transformations

    Returns:
        test_label_data_transformations: dict of label data transformations
    """

    return test_label_data_transformations
