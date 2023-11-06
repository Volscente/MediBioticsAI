"""
This test module includes all the tests for the
module src.general.general_utils
"""
# Import Standard Modules
import pytest

# Import Package Modules
from src.general_utils.general_utils import read_configuration


@pytest.mark.parametrize('test_config_file, test_config, expected_value', [
    ('config.yaml', 'test_value', 1),
])
def test_read_configuration(test_config_file: str,
                            test_config: str,
                            expected_value: int):
    """
    Test the function src.general_utils.general_utils.read_configuration
    by reading test configuration entries

    Args:
        test_config_file: String configuration file name
        test_config: String configuration entry key
        expected_value: String configuration expected value

    Returns:
    """

    # Read configuration file
    config = read_configuration(test_config_file)

    assert config[test_config] == expected_value


@pytest.mark.parametrize('test_config_file, expected_error', [
    ('wrong_config.yaml', FileNotFoundError)
])
def test_read_configuration_exception(test_config_file: str,
                                      expected_error: FileNotFoundError):
    """
    Test the exceptions to the function src.general_utils.general_utils.read_configuration

    Args:
        test_config_file: String wrong configuration file name
        expected_error: Exception instance

    Returns:
    """

    with pytest.raises(expected_error):

        read_configuration(test_config_file)