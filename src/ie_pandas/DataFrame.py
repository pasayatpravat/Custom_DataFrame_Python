import numpy as np


class DataFrame:
    def __init__(self, data):
        """This is the consuctor of the class that takes a disctionary 'data' as an argument
            and creates a DataFrame with the data."""

        # Check that the input data is of type dictionary

        if not isinstance(data, dict):
            raise ValueError("Wrong_Input_Type: Only dictionary is acceptable")

        else:

            # Create a list that contains the length of dictionary values

            length = []
            for i in data.values():
                length.append(len(i))

        # Only letting list and numpy array to be set as values in the
        # dictionary

        for i in data.values():

            if isinstance(i, (list, np.ndarray)):
                pass

            else:
                raise ValueError(
                    "Wrong_Input_Type: Only dictionary of list or Numpy array is acccepted"
                )

        # making sure that all columns are of same length

        if len(set(length)) > 1:
            raise ValueError(
                "Wrong_Input_Length: Columns with unequal length are not accepted"
            )

        else:

            for i in data.values():
                if all(
                    isinstance(
                        x,
                        (
                            int,
                            float,
                            str,
                            bool,
                            np.int_,
                            np.float_,
                            np.chararray,
                            np.bool_,
                        ),
                    )
                    for x in i
                ):
                    pass
                else:
                    raise ValueError(
                        "Wrong_Data_Type: Only integer, float, boolean and string are accepted"
                    )

        # Making sure that all values in a column are of the same type
        for i in data.values():
            class_type = []
            for value in i:
                class_type.append(type(value))

            if len(set(class_type)) > 1:
                raise ValueError(
                    "All the values in a column should be the same")
            else:
                self.data = data
                self.keys = data.keys()
                values = []
                for v in data.values():
                    values.append(v)
                self.values = values

    def __getitem__(self, column_name):
        """ This function take a string 'column_name' as an argument
            and returns the values of that column from the DataFrame"""
        # Check if the column is present for the DataFrame
        if column_name in self.keys:
            return np.array(self.data[column_name])
        else:
            # Throw an error if column isn't present for the DataFrame
            raise ValueError(
                "Wrong_Column_Name: Column is not present in the DataFrame"
            )

    def __setitem__(self, column_name, value):
        """ This function takes a string 'column_name' and a list 'value' as arguments
            and modify/overwrite the column values"""
        # Check if the column is present for the DataFrame
        if column_name in self.keys:
            # Check if the value we want to set to the column is provided in
            # list format
            if isinstance(value, list):
                # Check if the value is provided for all the rows
                if len(self.data[column_name]) == len(value):
                    # Check if all the values provided in the list is one of
                    # the permitted datatypes
                    if all(
                        isinstance(
                            x,
                            (
                                int,
                                float,
                                str,
                                bool,
                                np.int_,
                                np.float_,
                                np.chararray,
                                np.bool_,
                            ),
                        )
                        for x in value
                    ):
                        # Set the value for the column
                        self.data[column_name] = value
                    else:
                        # Throw an error if any value provided in the list
                        # doesn't have a permitted datatype
                        raise ValueError(
                            "Wrong_Datatype: Only integer, float, boolean and string are accepted"
                        )

                else:
                    # Throw an error if the value isn't provided for all the
                    # rows
                    raise ValueError(
                        "Wrong_Input_Length: Value should be given for all the rows"
                    )
            else:
                # Throw an error if the value we want to set to the column
                # isn't provided in list format
                raise ValueError("Wrong_Input_Type: Only list is acceptable")
        else:
            # Throw an error if column isn't present for the DataFrame
            raise ValueError(
                "Wrong_Column_Name: Column is not present in the DataFrame"
            )

    def get_rows(self, index_start, index_end=None):
        """ This method takes integer values 'index_start' and 'index_end' as arguments
            and returns the specific rows."""
        # Initialize the result that we have to return
        result_list = []

        # If the user has not given the end index then assume that we have to
        # fetch only the start index
        if index_end is None:
            index_end = index_start + 1

        # Check if the input indexs are integer
        if isinstance(index_start, int) and isinstance(index_end, int):
            # Iterate over set of indexes/rows
            for index in range(index_start, index_end):
                # Initiate a dictionary, where we will store the data belonging
                # to a row
                row_dictionary = dict()
                # Iterate over all the columns of a particular row
                for key in self.keys:
                    # Set the values in the dictionary
                    row_dictionary[key] = (self.data[key])[index]

                # Add the row value dictionary to the list
                result_list.append(row_dictionary)
            # Return the output
            return result_list
        else:
            # Throw an error saying that only integer indexes are accepted
            raise ValueError(
                "Wrong_Input_Type: Only integer value is acceptable")

    def sum(self):
        """ This method returns a List of dictionary that contains the sum of numeric columns"""
        # Initialize the variables
        sum_list = []
        sum_dictionary = dict()

        # Iterate over all the columns
        for key in self.keys:
            # Check if the column contains numeric values
            if all(isinstance(x, (int, float, np.int_, np.float_))
                    for x in self.data[key]):
                sum_dictionary[key] = np.sum(self.data[key])
            else:
                # If the column contains non-numeric values, ignore it from the
                # calculation
                pass

        # Add the output to a list
        sum_list.append(sum_dictionary)
        # Return the output in form of a list
        return sum_list

    def median(self):
        """ This method returns a List of dictionary that contains the median of numeric columns"""
        # Initialize the variables
        median_list = []
        median_dictionary = dict()

        # Iterate over all the columns
        for key in self.keys:
            # Check if the column contains numeric values
            if all(isinstance(x, (int, float, np.int_, np.float_))
                    for x in self.data[key]):
                median_dictionary[key] = np.median(self.data[key])
            else:
                # If the column contains non-numeric values, ignore it from the
                # calculation
                pass

        # Add the output to a list
        median_list.append(median_dictionary)
        # Return the output in form of a list
        return median_list

    def min(self):
        """ This method returns a List of dictionary that contains the minimum value of numeric columns"""
        # Initialize the variables
        min_list = []
        min_dictionary = dict()

        # Iterate over all the columns
        for key in self.keys:
            # Check if the column contains numeric values
            if all(isinstance(x, (int, float, np.int_, np.float_))
                    for x in self.data[key]):
                min_dictionary[key] = np.min(self.data[key])
            else:
                # If the column contains non-numeric values, ignore it from the
                # calculation
                pass

        # Add the output to a list
        min_list.append(min_dictionary)
        # Return the output in form of a list
        return min_list

    def max(self):
        """ This method returns a List of dictionary that contains the maximum value of numeric columns"""
        # Initialize the variables
        max_list = []
        max_dictionary = dict()

        # Iterate over all the columns
        for key in self.keys:
            # Check if the column contains numeric values
            if all(isinstance(x, (int, float, np.int_, np.float_))
                    for x in self.data[key]):
                max_dictionary[key] = np.max(self.data[key])
            else:
                # If the column contains non-numeric values, ignore it from the
                # calculation
                pass

        # Add the output to a list
        max_list.append(max_dictionary)
        # Return the output in form of a list
        return max_list

    def column_names(self):
        """ This method returns the name of columns of the DataFrame"""
        # Initialize the column name list
        column_names = []
        # Iterate over the column names present as the keys of the dataframe
        for key in self.keys:
            # Add it to the list
            column_names.append(str(key))
        # Return the output
        return column_names

    # This function will give you the first row of the DataFrame

    def tail(df):

        # First weare creating and empty DataFrame

        l = []

# We createaforloop to collect all the column names that we have in our
# DataFrame

        for i in df.column_names():
            a = i
            l.append(a)

            # We print our list of columns

        print(l)

        q = []

# Anotherforloop to extract the first row of out DataFrame

        for i in l:
            a = df[i][-1]
            q.append(a)

# Printingourdataframe

        print(q)

# Oncethisfunction is done, we have the name of the columns with the last row
    def head(df):
        l = []
        for i in df1.column_names():
            a = i
            l.append(a)
        q = []
        for i in range(4):
            for w in l:
                a = df1[w][i]
                q.append(a)
            ab = {l[0]: q[0], l[1]: q[1], l[2]: q[2]}
            print(ab)
            del q
            q = []
