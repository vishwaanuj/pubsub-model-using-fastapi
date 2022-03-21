from pydantic import BaseModel

'''

Creating serializer models

'''
class Transactions(BaseModel):
    transaction_id:int
    sku_id:str
    sku_price:float
    transaction_datetime:str
    
    
class SKU(BaseModel):
    sku_name:str
    sku_category:str
    sku_id:str
    
