"""
This test module includes all the fixtures necessary
for running PyTest tests
"""
# Import Standard Libraries
import pathlib
import pytest
from dynaconf import Dynaconf

# Import Package Modules
from src.general_utils.general_utils import read_configuration

# Read configuration file
# TODO: Remove
configuration = read_configuration(pathlib.Path(__file__).parents[1]
                                   / 'configuration'
                                   / 'test_config.yaml')
config = Dynaconf(settings_files=[pathlib.Path(__file__).parents[1]
                  / 'configuration'
                  / 'test_config.toml'])


@pytest.fixture
def fixture_numerical_data_transformations(
        data_transformations_config: Dynaconf = config
) -> dict:
    """
    Fixture for a Dictionary Numerical Data Transformations with structure:
        <transformation_name>:
            include: <bool>
            module: <string module name>

    Args:
        data_transformations_config: Dynaconf object with numerical data transformations as a dictionary

    Returns:
        test_numerical_data_transformations: dict of numerical data transformations
    """

    # Retrieve data transformations
    data_transformations = data_transformations_config['numerical_data_transformations'].to_dict()

    return data_transformations


@pytest.fixture
def fixture_categorical_data_transformations(
        data_transformations_config: Dynaconf = config
) -> dict:
    """
    Fixture for a Dictionary Categorical Data Transformations with structure:
        <transformation_name>:
            include: <bool>
            module: <string module name>

    Args:
        data_transformations_config: Dynaconf object with numerical data transformations as a dictionary

    Returns:
        test_categorical_data_transformations: dict of categorical data transformations
    """

    # Retrieve data transformations
    data_transformations = data_transformations_config['categorical_data_transformations'].to_dict()

    return data_transformations


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
