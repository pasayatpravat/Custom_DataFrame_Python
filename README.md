##NAME:

ie_pandas


##DESCRIPTION:

This open source project / package is created specifically for an assignment for the Advanced Python class of the Master in Big Data and Business Analytics at IE School of Human Sciences and Technology (Madrid). The goal of this open source project is to create a Python library which contains a simplified DataFrame object. 


Since the assignment requirements stated that our new library could not depend on pandas, dask, array or any other library with a similar functionality, we were only allowed to depend our library on Numpy, which is a highly efficient numerical computing library for Python. 


##FUNCTIONALITIES:

The library contains these basic functionalities with the necessary tests:

1. CREATION OF DATAFRAME (__init__)

	* Creation from a dictionary of lists (resembling the columns) and dictionary of NumPy arrays
	
		dict_x = {"name": ["Tom", "Harry", "Dick", "Jerry"], "age": [10, 20, 30, 40]}
		df1 = DataFrame(dict_x)
	
	* Support for int, float (numerical) and bool, string (non-numerical) columns.
	
		Any other datatype will cause an error.
	
	* Values entered for different column should have same lenght, else error will be generated.
	
	* A single column should contain values from a single datatype, else error will be generated.
	
	
2. DATAFRAME COLUMN ACCESS (__getitem__)

	* Dictionary-style access to columns (df["col_name"]), which returns NumPy arrays in all cases.

		df1['age']		# Result is [10, 20, 30, 40]


3. DATAFRAME MODIFICATION (__setitem__)

	* Modification can be done to the DataFrame by accessing it through Dictionary-style. 
	
		df1['age'] = [11, 21, 31, 41]


4. DATAFRAME ROW SELECTION (get_row)

	* Method 'get_row(index_start, index_end)' returns a list of values corresponding to the row(s).
	
		Here the 'index_end' is optional. If the user doesn't enter the 'index_end', then only one row corresponding to the 'index_start' is selected.
		
		df1.get_row(0, 4)	# Selects row 0, 1, 2 and 3
		
	* If the 'index_start' and/or the 'index_end' don't contain integer values, error is generated.
	

5. SUM, MEDIAN, MIN, MAX OF DATAFRAME COLUMNS (sum, median, min, max)

	* Methods sum() calculate the sums the all the values of numerical columns and skips through the non-numeric columns.
	
		df1.sum()		# Result is [{'age': 100}]
		
		
	* Methods median() calculate the median values of all the of numerical columns and skips through the non-numeric columns.
	
		df1.median()		# Result is [{'age': 25.0}]
		
		
	* Methods min() calculate the min values of all the of numerical columns and skips through the non-numeric columns.
	
		df1.min()		# Result is [{'age': 10}]	
		
		
	* Methods max() calculate the max values of all the of numerical columns and skips through the non-numeric columns.
	
		df1.max()		# Result is [{'age': 40}]


5. DATAFRAME COLUMN NAMES (column_names)

	* Methods column_names() returns all the column names of the Dataframe.
	
		df1.column_names()		# Result is ['name', 'age']
		

##INSTALLATION:

	* The source code is currently hosted on GitHub at: https://github.com/pasayatpravat/ie_pandas
	
	* Dependencies
		numpy
		matplotlib
		pytest
		
		Incase above dependent libraries are not present, you can install these by doing
		
			pip install <libraryName>
		
	* In the ie_pandas directory (same one where you found this file after cloning the git repo), execute:
	
			python setup.py install
		
		or for installing in development mode:
		
			python setup.py develop
			
		Alternatively, you can use pip if you want all the dependencies pulled in automatically (the -e option is for installing it in development mode):
		
			pip install -e .
			
	* Installing with PyPi
	
		pip install ie_pandas
		
	* Installing via Miniconda
	
		* create a new conda environment
		
			conda create -n <name_of_my_env> python
			
		* put your self inside this environment run
		
			source activate name_of_my_env
			
			activate name_of_my_env					# On windows
			
		* install pandas
		
			conda install pandas
			
			To install a specific pandas version:
			
			conda install pandas=0.1.dev0
			
				
	* Access DataFrame
	
		from ie_pandas.DataFrame import DataFrame
		
		
	* Running the Tests (inside the ie_pandas folder)
		
		pytest


##SUPPORT:

For questions about installation or any other remarks, please find below the email adresses of the creators of this library:

	- Pravat Pasayat : pasayat.pravat@student.ie.edu
	- Alberto Lombatti: a.lombatti@student.ie.edu
	- Alvaro Romero Villa: aromerovilla@student.ie.edu
	- Camille Chauliac: camille.chauliac@student.ie.edu


##CONTRIBUTING:

How to contribute to our project: 

	* Fork the master repository (https://github.com/pasayatpravat/ie_pandas.git) to your github remote account
 
	* Clone the master repository to your local machine.
		git clone https://github.com/pasayatpravat/ie_pandas.git
	
	* Go to the local github directory.
		cd <directoryPath>
		
	* Add your fork as a remote
		git remote add <GitHub_UserName> <Forked_repository_URL>
		
	* Initialize the repository
		git init
		
	* Create a new branch 
		git checkout -b <branchName>
		
	* Add/Modify/Remove files in the repository.
	
	* Commit your changes.
		git add <filePath/fileName>
		git commit -m <"comment">
		
	* Push up your changes/branch to your forked repository. 
		git push <GitHub_UserName> <branchName>
		
	* Go to your GitHub remote repository and create a pull request.


##AUTHORS:

	- Pravat Pasayat
	- Alberto Lombatti
	- Alvaro Romero Villa
	- Camille Chauliac
	

##ACKNOWLEDGMENTS:

We would like to thank our 'Advance Python' Professor, *Mr. Juan Luis Cano*, for his entertaining way of teaching classes and for helping us to understand what Python is all about. He was the one with this amazing idea of creating a new Python library and thanks to him, we now know more about how development works. 
