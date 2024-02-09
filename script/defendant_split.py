import pandas as pd
import numpy as np


def split_rec(x):
    ls = x['defendant'].split("\n\n")
    return ls

def split_lists(row):
    return pd.Series(row['list_rec'])

file = pd.read_csv("test.csv")
temp_df = pd.DataFrame()

temp_df['defendant'] = file['Name  And  Address of  Judgment  Debtor(s) ( Defendant(s))']

temp_df['list_rec'] = temp_df.apply(lambda x: split_rec(x), axis=1)
df_exteded = pd.concat([temp_df.apply(split_lists, axis=1), temp_df['list_rec']], axis=1)
# df_exteded.drop(df_exteded['list_rec'])
print(df_exteded)

df_exteded.to_csv('extended.csv',index=False)




