class DataFrame:
    def __init__(self, df):
        
        #checking the type to make sure it is a dicitonary
        if type(df) != dict:
            raise ValueError("Wrong input type, Only dictionaries are acceptable")

        else:
            l = []
            for i in df.values():
                l.append(len(i))

        #Only letting list and numpy array to be set as values in the dictionary
        for i in df.values():
            if isinstance(i, (list,numpy.ndarray)):
                pass
            else:
                raise ValueError(
                    " Only dictionaries of list or Numpy array are acccepted"
                )
         
        # making sure that all columns are of same length
        if len(set(l)) > 1:
            raise ValueError("Columns with unequal length are not accepted")

        else:
            for i in df.values():
                if all(isinstance(x, (int, float, str, bool,numpy.int_,numpy.float_,numpy.chararray,numpy.bool_)) for x in i):
                    pass
                else:
                    raise ValueError(
                        "Wrong data type, Only integer, float, boolean and string are accepted"
                    )
        # Making sure that all values in a column are of the same type
        for i in df.values():
            l = []
            for value in i:
                l.append(type(value))

            if len(set(l)) > 1:
                raise ValueError("All the values in a column should be the same")

            else:
                self.df = df
                self.keys=df.keys()
                l=[]
                for v in df.values():
                    l.append(v)
                self.values=l
    
    def __getitem__(self,colname):
        ''' This function returns the values of the called column'''
        return numpy.array(self.df[colname])
    
    
    def colnames(self):
        ''' This method returns the name of columns'''
        l=[]
        for k in self.keys:
            l.append(str(k)) 
        return l
    
    
    def get_row(self,index_start,index_end):
        ''' This method returns the cited rows'''
        dummy=dict()
        for k in self.keys:
            dummy[k]=(self.df[k])[index_start:index_end]
        
        return dummy
    
    def sum(self):
        ''' This method returns a dictionary including the sum of all columns'''
        d=dict()
        for k in self.keys:
            d[k]=numpy.sum(self.df[k])
        return d
    
    def median(self):
        ''' This method returns a dictionary including the median of all columns'''
        d=dict()
        for k in self.keys:
            d[k]=numpy.median(self.df[k])
        return d
    
    def min(self):
        ''' This method returns a dictionary including the min of all columns'''
        d=dict()
        for k in self.keys:
            d[k]=numpy.min(self.df[k])
        return d
    
    def max(self):
        ''' This method returns a dictionary including the max of all columns'''
        d=dict()
        for k in self.keys:
            d[k]=numpy.max(self.df[k])
        return d
	