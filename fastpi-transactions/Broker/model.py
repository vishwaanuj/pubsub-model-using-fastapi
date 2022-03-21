'''
Creating schemas for the databases
'''

from sqlalchemy import Column,Integer,String,Float,DateTime

from db import Base
from sqlalchemy.orm import relationship


class sku_model(Base):
    __tablename__='sku'
    transaction_id=Column(Integer,primary_key=True,index=True)
    sku_id=Column(String)
    sku_price=Column(Float)
    transaction_datetime=Column(DateTime)
    
class Transaction_model(Base):
    __tablename__='Transactions'
    transaction_id=Column(Integer,primary_key=True)
    sku_id=Column(String)
    sku_price=Column(Float)
    transaction_datetime=Column(DateTime)
    
    #sku_data = relationship("sku_model", back_populates="items")
    
    
    