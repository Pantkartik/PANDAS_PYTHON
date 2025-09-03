'''
Loading the data 


'''

# head()   head(n)   -----> for loading the first lines 
# by defalut 5


# tail()    tail(n)    ------> for loading the last lines
# default as 5 



import pandas as pd 

df=pd.read_csv(r"C:\Users\naman\OneDrive\Documents\GitHub\PANDAS_PYTHON\BASICS\LOADING_ANALYSING\data.csv")


# print(df)



# for showing first 5 lines from starting 

print(df.head(5))


# for showing last 5 lines from ending 

print(df.tail(5))