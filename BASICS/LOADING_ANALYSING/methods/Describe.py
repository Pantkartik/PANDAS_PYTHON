'''

step 1 : sample data frame

'''

import pandas as pd

# creating a data frame

data={
    "Name":["kartik","Naman","sidhu","karan"],
    "Class":["Btech Cse","Btech Cse","Btech Cse","Btech Cse"],
    "Blood":["A+",'B','A-','AB+'],
    "Height":["6 feet","5 feet","5.6 feet","6 feet",]
}

df=pd.DataFrame(data)

print(df)


# DESCRIPTIVE STAT

print(df.describe())