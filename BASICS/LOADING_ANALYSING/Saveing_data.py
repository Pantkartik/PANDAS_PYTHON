'''
savinig the data

'''


import pandas as pd

data={
    "Name":['RAM','SHYADM','HERO'],
    "City":['delhi','mumbai','gurugram'],
    "Age":[23,51,67]
    

}

df=pd.DataFrame(data)
print(df)



# saving the data(csv)


df.to_csv("data_maked_kartik.csv",index=False)


# saving the data(xlsx)

df.to_csv("data_maked_kartik.xlsx",index=False)

# saving the data(json)

df.to_csv("data_maked_kartik.json",index=False)