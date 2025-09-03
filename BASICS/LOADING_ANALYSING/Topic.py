# Before manipulation of the data we must know the following things 


# 1. how big is the dataset 
# 2. what are the names of columns


# shape and columns
# ''''    to find the size of the data set ''''
# ''''    to find tcolumn name ''''


import pandas as pd

df=pd.read_csv(r"C:\Users\naman\OneDrive\Documents\GitHub\PANDAS_PYTHON\BASICS\LOADING_ANALYSING\data.csv")

# to find the size of the dataset we use the shape and columns of the dataset

print(df.shape)
print(df.columns)