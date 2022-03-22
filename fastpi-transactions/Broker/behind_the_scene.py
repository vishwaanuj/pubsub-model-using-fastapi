from datetime import datetime,timedelta
import csv
import pandas as pd
from db import engine


#for creating string to date in desired format 
def string_todate(obj):
     '''
     params
     obj-> type:string 
     '''
     date_time_obj = datetime.strptime(obj.strip(), '%d/%m/%Y').date()
     print(date_time_obj)
     return date_time_obj
 
 
#for creating date to string in desired format 
def date_tostring(obj):
     '''
     params
     obj->type:datetime object from sqlite db
     '''
    return datetime.strftime(obj, '%d/%m/%Y')


        
#for getting the last n day Date       
def get_last_ndays(obj,days):
    '''
    params
    obj->transaction_db model  type: fast-api model class
    days: last number of days type:int
    ''' 
    days =obj.transaction_datetime-timedelta(days=days)
    return days


#for getting value in csv file
def get_csv_value(df,col,query):
    '''
    params
    df: dataframe object after reading csv file type:Dataframe obj
    col:the column data type:str
    query: the string of the particular column type:string
    ''' 
    # filtering the rows where  query is present
    df = df[df['sku_id'].str.contains(query)]
    res=df[col].values[0]
    return res

#to spit out json in desired format        
def transaction_id_format(transaction_json):
     '''
     transaction_json-> type:json object
     '''
    res={"transaction_id":str(transaction_json.transaction_id),
     "sku_name":str(transaction_json.sku_name),
     "sku_price":(transaction_json.sku_price),
     "transaction_datetime":date_tostring(transaction_json.transaction_datetime) 
    }
    return res






