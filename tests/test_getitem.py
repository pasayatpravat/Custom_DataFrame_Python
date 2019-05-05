from ie_pandas.DataFrame import DataFrame

import pytest
import numpy as np


dict_x = {"name": ["Tom", "Harry", "Dick", "Jerry"], "age": [10, 20, 30, 40]}
df1 = DataFrame(dict_x)


def test_get_row_scenario_1():

    expected_output = np.array([10, 20, 30, 40])

    actual_output = df1["age"]

    assert np.array_equal(actual_output, expected_output)


def test_get_row_error_scenario_1():

    with pytest.raises(ValueError) as excinfo:
        df1["Nationality"]
    assert (
        str(excinfo.value)
        == "Wrong_Column_Name: Column is not present in the DataFrame"
    )
