"""
The module contains object classes for the Data Preparation pipelines and components
"""
# Import Standard Libraries
import pathlib

# Import Package Modules
from src.logging_module.logging_module import get_logger


class HealthcareDataPreparation:
    """
    The class implements a Training Data Preparation pipeline,
    which involves standard data preparation techniques
    like imputation, normalisation and standardisation.

    Attributes:
        logger: logging.Logger object for log messages
        data_transformations: Dictionary of data preparation transformations to apply
        numerical_features: List of numerical feature names
        categorical_features: List of categorical feature names
        numerical_data_pipeline_steps: List of numerical data pipeline steps
        categorical_data_pipeline_steps: List of categorical data pipeline steps
    """

    def __init__(self,
                 data_transformations: dict,
                 features: dict):
        """
        The constructor of the TrainingDataPreparation object
        initialise the data preparation transformation
        dictionary and numerical and categorical features list.

        Args:
            data_transformations: Dictionary of data preparation transformations to apply
            features: Dictionary of features list 'numerical' and 'categorical'
        """
        # Setup logger
        self.logger = get_logger(__class__.__name__,
                                 pathlib.Path(__file__).parents[1] /
                                 'logging_module' /
                                 'log_configuration.yaml')