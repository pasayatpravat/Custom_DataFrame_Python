from ie_pandas.DataFrame import DataFrame

import pytest


dict_x = {"name": ["Tom", "Harry", "Dick", "Jerry"], "age": [10, 20, 30, 40]}


df1 = DataFrame(dict_x)


def test_get_row():

    expected_output = [{'name': 'Tom', 'age': 10}]

    actual_output = df1.get_rows(0, 1)

    assert (actual_output == expected_output)
