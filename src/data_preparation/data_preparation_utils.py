"""
The module contains utility function for the Data Preparation pipeline
"""
# Import Standard Libraries
import os
import pathlib
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

# Import Package Modules
from src.logging_module.logging_module import get_logger


# Setup logger
logger = get_logger(os.path.basename(__file__).split('.')[0],
                    pathlib.Path(__file__).parents[1] /
                    'logging_module' /
                    'log_configuration.yaml')


def build_numerical_data_pipeline_steps(numerical_data_transformations: dict) -> list:
    """
    Build numerical data transformations steps based on
    the configuration in 'numerical_data_transformations'

    Args:
        numerical_data_transformations: Dictionary of numerical data transformations configuration

    Returns:
        numerical_data_pipeline_steps: List of numerical data transformation steps
    """

    logger.info('build_numerical_data_pipeline_steps - Start')

    # Initialise numerical data pipeline steps list
    numerical_data_pipeline_steps = []

    logger.info('build_numerical_data_pipeline_steps - Building steps')

    # 1. Check feature engineering step
    if numerical_data_transformations['feature_engineering']['include']:
        pass
    else:
        logger.info('build_numerical_data_pipeline_steps - Skipping Feature Engineering step')

    # 2. Check imputation step
    if numerical_data_transformations['imputation']['include']:

        # Retrieve imputation module to use
        imputation_module = numerical_data_transformations['imputation']['module']

        logger.info('build_numerical_data_pipeline_steps - Adding %s Imputation step',
                    imputation_module)

        # Switch the imputation technique to apply
        match imputation_module:
            case 'SimpleImputer':
                numerical_data_pipeline_steps.append(
                    ('imputation',
                     SimpleImputer(strategy='median', copy=False))
                )
    else:
        logger.info('build_numerical_data_pipeline_steps - Skipping Imputation step')

    # 3. Check standardisation step
    if numerical_data_transformations['standardization']['include']:
        pass
    else:
        logger.info('build_numerical_data_pipeline_steps - Skipping Standardisation step')

    # 4. Check normalization step
    if numerical_data_transformations['normalization']['include']:
        pass
    else:
        logger.info('build_numerical_data_pipeline_steps - Skipping Normalization step')

    logger.info('build_numerical_data_pipeline_steps - End')

    return numerical_data_pipeline_steps

