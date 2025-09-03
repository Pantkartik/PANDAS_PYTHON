import pandas as pd

# Read data form csv file

# df = pd.read_csv("C:/Users/naman/OneDrive/Documents/GitHub/PANDAS_PYTHON/BASICS/LOADING_ANALYSING/data.csv")
 
data=pd.read_csv(r'C:\Users\naman\OneDrive\Documents\GitHub\PANDAS_PYTHON\BASICS\LOADING_ANALYSING\data.csv',encoding="latin1")

# both methods
# data=pd.read_csv(r'C:\Users\naman\OneDrive\Documents\GitHub\PANDAS_PYTHON\BASICS\LOADING_ANALYSING\data.csv')
print(data)