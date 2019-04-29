NAME:

ie_pandas


DESCRIPTION:


This open source project / package is created specifically for an assignment for the Advanced Python class of the Master in Big Data and Business Analytics at IE School of Human Sciences and Technology (Madrid). The goal of this open source project is to create a Python library which contains a simplified DataFrame object. 


Since the assignment requirements stated that our new library could not depend on pandas, dask, array or any other library with a similar functionality, we were only allowed to depend our library on Numpy, which is a highly efficient numerical computing library for Python. 


FUNCTIONALITIES:


The library contains these basic functionalities with the necessary tests:


* Support for int, float (numerical) and bool, string (non-numerical) columns.


* Dictionary-style access to columns (`df["col_name"]`), which should return NumPy arrays in all cases, and should allow modification (read and write).


* Creation from a dictionary of lists (resembling the columns) and dictionary of NumPy arrays.


* Method .get_row(index) that returns a list of values corresponding to the row.


* Methods .sum(), .median(), .min() and .max() that, ignoring the non-numerical columns, return a list of values corresponding to applying the function to each numerical column.

INSTALLATION:

from ie_pandas import DataFrame



SUPPORT:

For questions about installation or any other remarks, please find below the email adresses of the creators of this library:
- Pravat Pasayat : 
- Alberto Lombatti: a.lombatti@student.ie.edu
- Alvaro Romero Villa: aromerovilla@student.ie.edu
- Camille Chauliac: camille.chauliac@student.ie.edu

CONTRIBUTING:

How to contribute to our project: 
 * Fork it (https://github.com/yourname/yourproject/fork)
 * Create your feature branch (git checkout -b feature/fooBar)
 * Commit your changes (git commit -am 'Add some fooBar')
 * Push to the branch (git push origin feature/fooBar)
 * Create a new Pull Request

AUTHORS:

- Pravat Pasayat
- Alberto Lombatti
- Alvaro Romero Villa
- Camille Chauliac

ACKNOWLEDGMENTS:

We would like to thank our 'Advance Python' Professor, Mr. Juan Luis Cano, for his entertaining way of teaching classes and for helping us to understand what Python is all about. He was the one with this amazing idea of creating a new Python library and thanks to him, we now know more about how development works. 
