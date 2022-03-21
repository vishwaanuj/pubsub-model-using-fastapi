import csv
import os
from random import uniform,choice


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
                         }
         self.write_to_csv()
         
    
             
    def write_to_csv(self):
         
          my_dict={'ID1':20.3, 'ID2':30.4,"ID3":40.5}
          keys = list(my_dict)
         
      
          for field in self.fields:
               lst=[]
               
              #for transaction csv 
               
               for i in range (1,self.range):
                         ID= choice(keys)
                         #transaction_id, sku_id, sku_price and transaction_datetime
                         lst.append([i,ID,my_dict[ID],str(0+i)+"/1/2022"])
                       
                    
                    

               
               with open(self.path+field+'.csv', 'w') as csvfile: 
                       
                         writer = csv.writer(csvfile) 
                       
                         writer.writerow(self.fields[field]) 
               
                         writer.writerows(lst)

               