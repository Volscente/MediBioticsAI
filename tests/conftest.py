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
        data_transformations: dict of numerical data transformations
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
        data_transformations: dict of categorical data transformations
    """

    # Retrieve data transformations
    data_transformations = data_transformations_config['categorical_data_transformations'].to_dict()

    return data_transformations


@pytest.fixture
def fixture_regression_metrics(
        metrics_config: Dynaconf = config
) -> list:
    """
    Fixture for regression metrics list

    Args:
        metrics_config: Dynaconf object with list of metrics

    Returns:
        metrics: list of regression metrics
    """

    # Retrieve data transformations
    metrics = metrics_config['default']['regression_metrics'].to_list()

    return metrics


@pytest.fixture
def fixture_multi_classification_metrics(
        metrics_config: Dynaconf = config
) -> list:
    """
    Fixture for multi-classification metrics list

    Args:
        metrics_config: Dynaconf object with list of metrics

    Returns:
        metrics: list of multi-classification metrics
    """

    # Retrieve data transformations
    metrics = metrics_config['default']['multi_classification_metrics'].to_list()

    return metrics
