from ie_pandas.DataFrame import DataFrame
import pytest


def test_min():
    dict_x = {"name": ["Tom", "Harry", "Dick", "Jerry"], 
              "age": [10, 20, 30, 40], "cars": [1, 2, 3, 4]}

    df1 = DataFrame(dict_x)

    expected_output = [{'age': 10, 'cars': 1}]

    actual_output = df1.min()

    assert actual_output == expected_output
