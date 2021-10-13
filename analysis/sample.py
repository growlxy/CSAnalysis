import os

import pandas as pd

fl = os.listdir(os.getcwd())
flag = True
for i in fl:
    if '.csv' in i:
        df = pd.read_csv(i, index_col=0, encoding='utf-8')
        if flag == True:
            temp = df
            flag = False
        else:
            temp = pd.concat([temp, df],  ignore_index=True)
print(temp)
df = temp.drop_duplicates(subset=['positionId'], keep='first').reset_index(drop=True)
print(df)

df.to_csv('sample.csv', encoding='utf-8')
