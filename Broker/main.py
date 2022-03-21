from fastapi import FastAPI
from model import Transactions
app = FastAPI()
'''

'''




@app.get("/")
async def root():
    return {"message": "hello this is my submission for my assigment"}

@app.post("/csv_dummy")
async def csv_up(item:Transactions):
    print(item)
    return 200,item

@app.get("/transaction/{transaction_id}")
async def transaction_id(transaction_id:int):
    
    return transaction_id

@app.get("/transaction-summary-bySKU/{last_n_days}")
async def transaction_sku_summary(id:int):
    
    return



