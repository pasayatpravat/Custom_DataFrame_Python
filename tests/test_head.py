from ie_pandas.DataFrame import DataFrame

import pytest


#Creating a test for the Head() function

def test_head():
    
    #This is the DataFrame that we are going to use
    
    dict_x = {"name": ["Tom", "Harry", "Dick", "Jerry"], "age": [10, 20, 30, 40], "salary":[50, 60, 70, 80], "adress":['a', 'b', 'c', 'd']}

    df1 = DataFrame(dict_x)

    l = []
    
    for i in df1.column_names():
        
        a = i
        
        l.append(a)
    

    q = []
    
    for i in l:
        
        a = df1[i][0]
        
        q.append(a)
    
    
    expected_output1 = ['name', 'age', 'salary', 'adress']
    
    actual_output1 = l

    expected_output2 = ['Tom', 10, 50, 'a']
    
    actual_output2 = q
    
    #With the Assert we are checking that everything is correct
    
    assert actual_output1 == expected_output1
    
    assert actual_output2 == expected_output2
