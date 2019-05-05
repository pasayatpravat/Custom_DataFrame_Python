from ie_pandas.DataFrame import DataFrame

import pytest
import numpy as np


dict_x = {"name": ["Tom", "Harry", "Dick", "Jerry"], "age": [10, 20, 30, 40]}
df1 = DataFrame(dict_x)


def test_get_row_scenario_1():

    df1["age"] = [11, 21, 31, 41]
    expected_output = np.array([11, 21, 31, 41])

    actual_output = df1["age"]

    assert np.array_equal(actual_output, expected_output)


def test_set_row_error_scenario_1():

    with pytest.raises(ValueError) as excinfo:
        df1["Nationality"] = ["IND", "USA", "ESP", "NED"]
    assert (
        str(excinfo.value)
        == "Wrong_Column_Name: Column is not present in the DataFrame"
    )


def test_set_row_error_scenario_2():

    with pytest.raises(ValueError) as excinfo:
        df1["age"] = (11, 21, 31, 41)
    assert str(excinfo.value) == "Wrong_Input_Type: Only list is acceptable"


def test_set_row_error_scenario_3():

    with pytest.raises(ValueError) as excinfo:
        df1["age"] = [11, 21, 31]
    assert (
        str(excinfo.value)
        == "Wrong_Input_Length: Value should begiven for all the rows"
    )


def test_set_row_error_scenario_4():

    with pytest.raises(ValueError) as excinfo:
        df1["age"] = [None, 21, 31, 41]
    assert (
        str(excinfo.value)
        == "Wrong_Datatype: Only integer, float,boolean and string are accepted"
    )
