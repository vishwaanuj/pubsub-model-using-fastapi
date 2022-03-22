from importlib.resources import path
from fastapi import FastAPI,Depends

from pandas import read_csv
from sqlalchemy.orm import Session
from db import engine,SessionLocal
from behind_the_scene import string_todate,transaction_id_format,get_last_ndays,get_csv_value
import model,schemas
from sqlalchemy import func
from sqlalchemy.sql import label



app = FastAPI()

df=read_csv("../csvFiles/sku.csv")
tr=model.Transaction_model
'''

'''
def get_db():
    db=SessionLocal()
    try:
        yield db
    except:
        db.close()

model.Base.metadata.create_all(engine)





def transaction_history_by(param,db,days,by):
   
    
    '''
    #the following function will retuurn the total_cost in N Days by Name or category
    
    params
    param:transaction_model column
    db:database  (Transaction.db)
    dayns : last N Days
    by: By sku name or sku category
    
    return:json obj
    '''
  
    e=db.query(label('sku_id', 
              param),
               func.count(param)).group_by(param).filter(tr.transaction_datetime > days).all()
    total_cost=[]#dict to store the id and sum of prices
    
    for i in e :#looping the result from above with unique sku_id and frequency dict
       res=db.query(tr).filter(param==i[0]).first()#again querying for the price
       total_cost.append( {by:i[0],'total_amount':res.sku_price*i[1]})
    return total_cost

  

@app.get("/")
async def root():
    return {"message": "hey!,this is submission for my assigment "}

@app.post("/csv_dummy")
async def csv_up(item:schemas.Transactions,db:Session=Depends(get_db)):
   
    #print(string_todate(item.transaction_datetime))
    new_entry=model.Transaction_model(transaction_id=item.transaction_id,
                                      sku_id=item.sku_id,
                                      sku_price=item.sku_price,
                                      transaction_datetime=string_todate(item.transaction_datetime),
                                      sku_name=get_csv_value(df,col='sku_name',query=item.sku_id),
                                      sku_cat=get_csv_value(df,col='sku_category',query=item.sku_id)
                                      )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return 200,new_entry

@app.get("/transaction/{transaction_id}")
async def transaction_id(transaction_id:int,db:Session=Depends(get_db)):
    t=db.query(tr).filter(tr.transaction_id==transaction_id).first()
    
   
    res=transaction_id_format(t)
    return res

@app.get("/transaction-summary-bySKU/{last_n_days}")
async def transaction_sku_summary(last_n_days:int,db:Session=Depends(get_db)):
    #use time delta
    last_entry=db.query(tr).order_by(tr.transaction_datetime)[-1]
    days=get_last_ndays(last_entry,last_n_days)
    res={"summary":transaction_history_by(by="sku_name",param=model.Transaction_model.sku_name,db=db,days=days)}
    return res


@app.get("/transaction-summary-bycategory/{last_n_days}")
async def transaction_cat_summary(last_n_days:int,db:Session=Depends(get_db)):
    #use time delta
    last_entry=db.query(tr).order_by(tr.transaction_datetime)[-1]
    days=get_last_ndays(last_entry,last_n_days)
    res={"summary":transaction_history_by(by='sku_category',param=model.Transaction_model.sku_cat,db=db,days=days)}
    return res



