'''
The publisher will be used to read the data from csv files and publish to the broker
'''

from csv_generator import csv_dummy_generator
import csv
import json
import requests
path_to_csv="../csvFiles/"
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
    for obj in json.loads(transactions):
     print("pew pew--->",end=" ")
     x = requests.post(url,json=obj)
     if x.json()[0] == 200:
        print(f"{x.json()[1]} was posted succesfully " )
     else:
         print(f"failed with {x.json()[0]} response")
         break
     
def send_live_data():
    
    print("to send live data ")
    t_id=input("transaction_id:")
    sku_id=input("sku_id:")
    sku_price=input("sku_price:")
    t=input("sku_id:")
send_to_broker()








    
        