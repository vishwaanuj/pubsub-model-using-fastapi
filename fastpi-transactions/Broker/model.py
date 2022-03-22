'''
Creating schemas for the databases
'''

from sqlalchemy import Column,Integer,String,Float,DateTime,ForeignKey

from db import Base
from sqlalchemy.orm import relationship,backref

class Transaction_model(Base):
    __tablename__='Transactions'
    transaction_id=Column(Integer,primary_key=True)
    sku_id=Column(String)
    sku_price=Column(Float)
    transaction_datetime=Column(DateTime)
    sku_name=Column(String)
    sku_cat=Column(String)
   
    #sku_data=relationship('sku_model',back_populates='sku_d')
    

 
  
    

    #sku_data = relationship("sku_model", back_populates="items")
    
    
    