from fastapi import FastAPI,Depends
from datetime import datetime
from schemas import Transactions
from sqlalchemy.orm import Session
from db import engine,SessionLocal
from behind_the_scene import string_todate
import model
app = FastAPI()
'''

'''
def get_db():
    db=SessionLocal()
    try:
        yield db
    except:
        db.close()

model.Base.metadata.create_all(engine)



@app.get("/")
async def root():
    return {"message": "hello this is my submission for my assigment"}

@app.post("/csv_dummy")
async def csv_up(item:Transactions,db:Session=Depends(get_db)):
    
    #print(string_todate(item.transaction_datetime))
    new_entry=model.Transaction_model(transaction_id=item.transaction_id,
                                      sku_id=item.sku_id,
                                      sku_price=item.sku_price,
                                      transaction_datetime=string_todate(item.transaction_datetime)
                                      )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return 200,new_entry

@app.get("/transaction/{transaction_id}")
async def transaction_id(transaction_id:int,db:Session=Depends(get_db)):
    t=db.query(model.Transaction_model).filter(model.Transaction_model.transaction_id==transaction_id).first()
    return t

@app.get("/transaction-summary-bySKU/{last_n_days}")
async def transaction_sku_summary(id:int):
    return



