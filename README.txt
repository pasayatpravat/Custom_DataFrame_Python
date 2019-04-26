NAME:

ie_pandas

DESCRIPTION:


This open source project/package is created specifically for an assignment for the Advanced Python class of the Master in Big data and 
business analytics at IE University (Madrid). The goal of this open source project is to create a Python library which contains a 
simplified DataFrame object. 


Since the assignment requirements stated that our new library could not depend on pandas, dask, array or any other library with a similar functionality, we were only allowed to depend our library on Numpy, which is a highly efficient numerical computing library for Python. 


FUNCTIONALITIES:


The library contains these basic functionalities with the necessary tests:


* Support for int, float (numerical) and bool, string (non-numerical) columns.


* Dictionary-style access to columns (`df["col_name"]`), which should return NumPy arrays in all cases, and should allow modification (read and write).


* Creation from a dictionary of lists (resembling the columns) and dictionary of NumPy arrays.


* Method .get_row(index) that returns a list of values corresponding to the row.


* Methods .sum(), .median(), .min() and .max() that, ignoring the non-numerical columns, return a list of values corresponding to applying the function to each numerical column.




INSTALLATION:





...
