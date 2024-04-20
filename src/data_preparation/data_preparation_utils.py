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

