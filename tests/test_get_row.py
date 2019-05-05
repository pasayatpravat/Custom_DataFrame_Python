from ie_pandas.DataFrame import DataFrame

import pytest


dict_x = {"name": ["Tom", "Harry", "Dick", "Jerry"], "age": [10, 20, 30, 40]}
df1 = DataFrame(dict_x)


def test_get_row_scenario_1():

    expected_output = [{"name": "Tom", "age": 10}, {"name": "Harry", "age": 20}]

    actual_output = df1.get_rows(0, 2)

    assert actual_output == expected_output


def test_get_row_scenario_2():

    expected_output = [{"name": "Tom", "age": 10}]

    actual_output = df1.get_rows(0)

    assert actual_output == expected_output


def test_get_row_error_scenario_1():

    with pytest.raises(ValueError) as excinfo:
        df1.get_rows("0", "1")
    assert str(excinfo.value) == "Wrong_Input_Type: Only integer value is acceptable"


def test_get_row_error_scenario_2():

    with pytest.raises(ValueError) as excinfo:
        df1.get_rows(0, "1")
    assert str(excinfo.value) == "Wrong_Input_Type: Only integer value is acceptable"


def test_get_row_error_scenario_3():

    with pytest.raises(ValueError) as excinfo:
        df1.get_rows("0", 1)
    assert str(excinfo.value) == "Wrong_Input_Type: Only integer value is acceptable"


def test_get_row_error_scenario_4():

    with pytest.raises(ValueError) as excinfo:
        df1.get_rows("0")
    assert str(excinfo.value) == "Wrong_Input_Type: Only integer value is acceptable
