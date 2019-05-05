from ie_pandas.DataFrame import DataFrame

import pytest
import numpy as np


def test_init_scenario_1():

    dict_x = {"name": ["Tom", "Harry", "Dick", "Jerry"], "age": [10, 20, 30, 40]}
    df1 = DataFrame(dict_x)

    expected_output = [
        {"name": "Tom", "age": 10},
        {"name": "Harry", "age": 20},
        {"name": "Dick", "age": 30},
        {"name": "Jerry", "age": 40},
    ]

    actual_output = df1.get_rows(0, 4)

    # assert np.array_equal(actual_output, expected_output)
    assert actual_output == expected_output


def test_init_error_scenario_1():

    with pytest.raises(ValueError) as excinfo:
        dict_x = [["Tom", "Harry", "Dick", "Jerry"], [10, 20, 30, 40]]
        df1 = DataFrame(dict_x)
    assert str(excinfo.value) == "Wrong_Input_Type: Only dictionary is acceptable"


def test_init_error_scenario_2():

    with pytest.raises(ValueError) as excinfo:
        dict_x = {"name": ("Tom", "Harry", "Dick", "Jerry"), "age": (10, 20, 30, 40)}
        df1 = DataFrame(dict_x)
    assert (
        str(excinfo.value)
        == "Wrong_Input_Type: Only dictionaryof list or Numpy array is acccepted"
    )


def test_init_error_scenario_3():

    with pytest.raises(ValueError) as excinfo:
        dict_x = {"name": ["Tom", "Harry", "Dick", "Jerry"], "age": [None, 20, 30, 40]}
        df1 = DataFrame(dict_x)
    assert (
        str(excinfo.value)
        == "Wrong_Data_Type: Only integer, float,boolean and string are accepted"
    )


def test_init_error_scenario_4():

    with pytest.raises(ValueError) as excinfo:
        dict_x = {"name": ["Tom", "Harry", "Dick", "Jerry"], "age": [10, 20, "30", 40]}
        df1 = DataFrame(dict_x)
    assert str(excinfo.value) == "All the values in a column should be the same type"
