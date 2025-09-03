'''
info()  


1. finds the data type
2. finds the rows and columns
3. finds the null non count
4. memory usage of the data

'''

import pandas as pd 

df=pd.read_csv(r"C:\Users\naman\OneDrive\Documents\GitHub\PANDAS_PYTHON\BASICS\LOADING_ANALYSING\data.csv")


# print(df)

print(df.info())