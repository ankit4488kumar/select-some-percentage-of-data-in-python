import pandas as pd
df=pd.read_csv("/mnt/c/Users/ankit/Documents/CSVFile_2021-03-25T10_15_55.csv",low_memory=False)
print("ok")
print(df.shape)
print(df.columns)
df2=df.sort_values('visit_mf_id',ascending=True).head(int(df.shape[0]*.5))
#df2=df.head(int(df.shape[0]*.5))
print(df2.shape)
