from datetime import datetime,timedelta
import csv
import pandas as pd
from db import engine


#for creating string to date in desired format 
def string_todate(obj):
     date_time_obj = datetime.strptime(obj.strip(), '%d/%m/%Y').date()
     print(date_time_obj)
     return date_time_obj
 
 
#for creating date to string in desired format 
def date_tostring(obj):
    return datetime.strftime(obj, '%d/%m/%Y')

#creating the sku.db in sqlite to be used on on mount phase of app
def sku_csv_to_sql(path,engine,table_name="sku"):
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        columns = ['sku_id','sku_name','sku_category']
        df = pd.DataFrame(data=reader, columns=columns)
        try:
            with engine.begin() as connection:
                df.to_sql(table_name, con=connection)
                print('Done, ok!')
        except Exception as e :
            print(f'{e}')
            pass
        
      
def get_last_ndays(obj,days):
    days =obj.transaction_datetime-timedelta(days=days)
    
    return days

def get_csv_value(df,col,query):
   
  
    # filtering the rows where  query is present
    df = df[df['sku_id'].str.contains(query)]
    res=df[col].values[0]
    return res

        
def transaction_id_format(transaction_json):
    res={"transaction_id":str(transaction_json.transaction_id),
     "sku_name":str(transaction_json.sku_name),
     "sku_price":(transaction_json.sku_price),
     "transaction_datetime":date_tostring(transaction_json.transaction_datetime) 
    }
    return res






