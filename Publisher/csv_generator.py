import csv
import os
from random import uniform


class csv_dummy_generator:
    '''
    this class is used to populate the csv files with random data
    params
    path:where to store the files
    dummy_range:range of dummy data to be written default 20 
    
    '''
    def __init__(self,path:str,dummy_range=20):
  
         self.range=dummy_range
         self.path=path
         #self.name=csvname #name of csv file
         
         self.fields={"transactions":['transaction_id', 'sku_id', 'sku_price','transaction_datetime'],
                      "sku":["sku_id","sku_name", "sku_category"]
                      }
         self.write_to_csv()
         
    
             
    def write_to_csv(self):
         
          for field in self.fields:
               lst=[]
               
               if field=="transactions":#for transaction csv 
               
                    for i in range (1,self.range):
                         #transaction_id, sku_id, sku_price and transaction_datetime
                         lst.append([i,'Id'+str(i),uniform(10.5, 75.5),str(0+i)+"/1/2018"])
                       
                    
                    
               else:# for static sku
                    for i in range (1,self.range):
                         lst.append(['Id'+str(i),'S'+str(i),'C'+str(i)])
               
               with open(self.path+field+'.csv', 'w') as csvfile: 
                       
                         writer = csv.writer(csvfile) 
                       
                         writer.writerow(self.fields[field]) 
               
                         writer.writerows(lst)

               