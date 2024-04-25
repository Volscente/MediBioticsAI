"""
The module contains object classes for the Model Training pipelines and components
"""
# Import Standard Libraries
import pathlib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Import Package Modules
from src.logging_module.logging_module import get_logger


class ModelTrainer:
    """
    The class implements a Model Training pipeline,
    which involves standard model training pipeline bundle,
    estimator fit and evaluation.

    Attributes:
        logger: logging.Logger object for log messages
        model_name: String name of the model to be trained
        model: Regressor model to be fitted and evaluated
        data_pipeline: ColumnTransformer with required data preparation steps
        pipeline: Scikit-learn Pipeline object that bundles the model and data_pipeline
    """

    def __init__(self,
                 model_name: str,
                 model: LinearRegression,
                 data_pipeline: ColumnTransformer):
        """
        The constructor of the ModelTrainer object.

        Args:
            model_name: String name of the model to be trained
            model: Regressor model to be fitted and evaluated
            data_pipeline: ColumnTransformer with required data preparation steps
        """
        # Setup logger
        self.logger = get_logger(__class__.__name__,
                                 pathlib.Path(__file__).parents[1] /
                                 'logging_module' /
                                 'log_configuration.yaml')

        self.logger.info('__init__ - Initialise object attributes')

        # Initialise attributes
        self.model_name = model_name
        self.model = model
        self.data_pipeline = data_pipeline
        self.pipeline = None

    def bundle_and_fit_pipeline(self,
                                x: pd.DataFrame,
                                y: pd.DataFrame):
        """
        Bundles the data pipeline and model into a Pipeline and perform the training

        Args:
            x: Pandas Dataframe of features values
            y: Pandas Dataframe of labels values

        Returns:
        """
        self.logger.info('bundle_and_fit_pipeline - Start')

        self.logger.info('bundle_and_fit_pipeline - Bundle the pipeline')

        # Bundle the data_pipeline and the model together into a Pipline object
        self.pipeline = Pipeline([
            ('data_preprocessing', self.data_pipeline),
            (self.model_name, self.model)
        ])

        self.logger.info('bundle_and_fit_pipeline - Fit the pipeline')

        # Train the pipeline
        self.pipeline.fit(x, y)

        self.logger.info('bundle_and_fit_pipeline - End')
