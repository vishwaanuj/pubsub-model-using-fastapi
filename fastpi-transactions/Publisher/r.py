
# importing pandas as pd
import pandas as pd
lst=[]
# reading csv file
df = pd.read_csv("../csvFiles/sku.csv")
  
# filtering the rows where Credit-Rating is Fair
df = df[df['sku_id'].str.contains('ID3')]

print(df["sku_category"].values[0])