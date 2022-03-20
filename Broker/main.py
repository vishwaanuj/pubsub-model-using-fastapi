from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
'''

'''

class Item(BaseModel):
    transaction_id:str
    sku_id:str
    sku_price:str
    transaction_datetime:str


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/csv_dummy")
async def root(item:Item):
    print(item.sku_id)
    return 200

