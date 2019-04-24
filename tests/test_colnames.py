from ie_pandas.DataFrame import DataFrame
import pytest


def test_colnames():
    dict_x = {"name": ["Tom", "Harry", "Dick", "Jerry"], "age": [10, 20, 30, 40]}

    df1 = DataFrame(dict_x)

    expected_output = ["name", "age"]

    actual_output = df1.column_names()

    assert actual_output == expected_output
