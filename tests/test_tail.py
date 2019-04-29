from ie_pandas.DataFrame import DataFrame

import pytest


# Creating a test for the tail() function

def test_tail():

    # This is the DataFrame that we are going to use

    dict_x = {"name": ["Tom", "Harry", "Dick", "Jerry"],
              "age": [10, 20, 30, 40],
              "salary": [50, 60, 70, 80],
              "adress": ['a', 'b', 'c', 'd']}

    df1 = DataFrame(dict_x)

    f = []
    for i in df1.column_names():
        a = i
        f.append(a)

    q = []
    for i in f:
        a = df1[i][-1]
        q.append(a)

    expected_output1 = ['name', 'age', 'salary', 'adress']

    actual_output1 = f

    expected_output2 = ['Jerry', 40, 80, 'd']

    actual_output2 = q

    # With the Assert we are checking that everything is correct

    assert actual_output1 == expected_output1

    assert actual_output2 == expected_output2
