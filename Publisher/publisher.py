'''
The publisher will be used to read the data from csv files and publish to the broker
'''

from csv_generator import csv_dummy_generator
import csv
import json
import requests
path_to_csv="./csvFiles/"
Host=" http://127.0.0.1:8000"
#csv_dummy_generator(path=path_to_csv,dummy_range=20)

      

def make_normal_json(csvFilePath):
    # create a dictionary
    data = []
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:   
            data.append(rows)
    return(json.dumps(data))

def send_to_broker():
         
    transactions=make_normal_json(csvFilePath=path_to_csv+'transactions.csv')
    
    url = Host+"/csv_dummy"
    requests.post(url,data={
    "transaction_id": "dsdsdsdsd",
    "sku_id": "string",
    "sku_price": "string",
    "transaction_datetime": "string"
    })
    #print(x)
send_to_broker()








    
        