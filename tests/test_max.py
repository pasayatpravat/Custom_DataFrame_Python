from ie_pandas.DataFrame import DataFrame
import pytest


def test_max():
    dict_x = {
        "name": [
            "Tom", "Harry", "Dick", "Jerry"], "age": [
            10, 20, 30, 40], "cars": [
                1, 2, 3, 4]}

    df1 = DataFrame(dict_x)

    expected_output = [{'age': 40, 'cars': 4}]

    actual_output = df1.max()

    assert actual_output == expected_output
