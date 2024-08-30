v1.0.4
------
- [x] Add module `src/model_training`
- [x] Add class `ModelTrainer` in `src/model_training/model_training.py`
- [x] Add function `compute_regression_metrics` in `src/model_training/model_training_utils.py`
- [x] Add Fixture `fixture_regression_metrics`
- [x] Add PyTest `test_compute_regression_metrics` in `tests/test_model_training.py`
- [x] Add function `bundle_and_fit_pipeline` in `src/model_training/model_training.ModelTrainer`
- [x] Add function `compute_multi_classification_metrics` in `src/model_training/model_training_utils.py`
- [x] Add Fixture `fixture_multi_classification_metrics`
- [x] Add PyTest `test_compute_multi_classification_metrics` in `tests/test_model_training.py`
- [x] Add function `evaluate_pipeline ` in `src/model_training/model_training.ModelTrainer`
- [x] Update Notebook `model_training.ipynb` in `notebooks/healthcare_classification`

v1.0.3
------
- [x] Add encode label into `notebooks/healthcare_classification/model_training.ipynb`

v1.0.2
------
- [x] Add `HealthcareDataPreparation` class in `src/data_preparation/data_preparation.py` module
- [x] Add `data_preparation_utils` in `src/data_preparation/data_preparation.py`
- [x] Add `build_numerical_data_pipeline_steps` in `src/data_preparation/data_preparation_utils.py`
- [x] Add `build_categorical_data_pipeline_steps` in `src/data_preparation/data_preparation_utils.py`
- [x] Add `conftests.py` in `tests`
- [x] Add PyTest `test_build_numerical_data_pipeline_steps` in `tests`
- [x] Add PyTest `test_build_categorical_data_pipeline_steps` in `tests`
- [x] Add Fixture `fixture_numerical_data_transformations`
- [x] Add Fixture `fixture_categorical_data_transformations`
- [x] Add script `pylint_lint.sh` in `scripts`
- [x] Add script `pylint_lint.sh` in `scripts`
- [x] Add function `build_training_data_preparation_pipeline` in class `HealthcareDataPreparation`
- [x] Add Notebook `model_training.ipynb` in `notebooks/healthcare_classification`

v1.0.1
------
- [x] Add `just jupy` command
- [x] Add `General EDA plots` in `notebooks/healthcare_classification/healthcare_dataset_eda.ipynb`
- [x] Add `Numerical Feature Distribution` plot in `notebooks/healthcare_classification/healthcare_dataset_eda.ipynb`
- [x] Add `Count Unique Values per Categorical Feature` plot in `notebooks/healthcare_classification/healthcare_dataset_eda.ipynb`
- [x] Add `Count Values per Relevant Categorical Feature` plot in `notebooks/healthcare_classification/healthcare_dataset_eda.ipynb`
- [x] Add `Label Distribution` plot in `notebooks/healthcare_classification/healthcare_dataset_eda.ipynb`
- [x] Add EDA conclusions

v0.1.5
------
- [x] Add `just lint_sql` command 
- [x] Refactor the PyLint commands in `justfile` and `pull_request_workflow.yml`

v0.1.4
------
- [x] Create the `pull_request_workflow.yml`

v.0.1.3
------
- [x] Add `general_utils/general_utils.py`
- [x] Define the `read_configuration` function
- [x] Add `tests/test_general_utils.py`
- [x] Define the `test_read_configuration`
- [x] Define the `test_read_configuration_exception`

v.0.1.2
------
- [x] Create justfile
- [x] Implement `pylint` just command
- [x] Implement `help`
- [x] Add read from `.env`

v.0.1.1
------
- [x] Update `.gitignore`
- [x] Create `logging_module`
- [x] Create `log_configuration.yaml`
- [x] Test `logging_module`
- [x] Test exceptions `logging_module`
- [x] Check test executions with `pytest` shell command