from datetime import datetime
from pydantic import BaseModel

'''

Creating schemas for the API 

'''
class Transactions(BaseModel):
    transaction_id:int
    sku_id:str
    sku_price:float
    transaction_datetime:str
    
