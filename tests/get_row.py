from ie_pandas.DataFrame import DataFrame

import pytest


dict_x = {"name": ["Tom", "Harry", "Dick", "Jerry"], "age": [10, 20, 30, 40]}


df1 = DataFrame(dict_x)


def test_get_row(df):


    expected_output = [{'name': 'Henry', 'age': 20}]
        
    actual_output = df1.get_rows(0,1)

    asset (actual_output == expected_output)
    
    
