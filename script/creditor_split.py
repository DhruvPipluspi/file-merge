import pandas as pd




def split_rec(x):
    ls = x['creditor'].split("\n\n")  
    return ls


file = pd.read_csv("test.csv")
temp_df = pd.DataFrame()


temp_df['creditor'] = file['Name  And  Address of  Judgment  Creditor ( Plaintiff)']


temp_df['list_rec'] = temp_df.apply(lambda x: split_rec(x), axis=1)

temp_df.to_csv("tesst.csv",index=False)