## Publisher

The following folder is used to create the API.

To run the API service run from this folder




```bash
uvicorn main:app -reload
```

##### The swagger documentation can be found on *http://127.0.0.1:8000/docs*

## Usage


```
Delete the transactions.db if you want to upload new data

Run publisher.py script from PUBLISHER folder in home after running the API service using above run command
```



## Methods
##### The Api Uses Following URLs And Methods
```
GET API   /transaction/{transaction_id}
```
#### params:
transaction_id : int

#### Description
 To be used by the subscriber to get transaction data of the product
```
example: GET http://127.0.0.1:8000//transaction/1
output:  {
    "transaction_id": "1",
    "sku_name": "S1",
    "sku_price": 20.3,
    "transaction_datetime": "01/01/2022"
}
```
---


```
GET API /transaction-summary-bySKU/{last_n_days}
```
#### params:
last_n_days : int

#### Description
 To be used by the subscriber to get transaction data of the product in the last N days

The query will return Name Of The Product and The Total Cost Summary with respect to Products Name parameter in the last N days 
```
example: GET http://127.0.0.1:8000/transaction-summary-bySKU/2
output: {
    "summary": [
        {
            "sku_name": "S1",
            "total_amount": 20.3
        },
        {
            "sku_name": "S2",
            "total_amount": 30.4
        }
    ]
}
```
---

```
GET API /transaction-summary-bycategory/{last_n_days}
```
#### params:
last_n_days : int

#### Description
 To be used by the subscriber to get transaction data of the product in the last N days

The query will return Name Of The Product and The Total Cost Summary with respect to Products 'Category' parameter in the last N days 
```
example: GET http://127.0.0.1:8000/transaction-summary-bycategory/2
output: {
    "summary": [
        {
            "sku_category": "C1",
            "total_amount": 20.3
        },
        {
            "sku_category": "C2",
            "total_amount": 30.4
        }
    ]
}
```
---
```
POST API /csv_dummy
```

#### Description
 To be used by the publisher to post the Transaction data of the product 

#### Params
```
example {'transaction_id': 20,'transaction_datetime': '1/1/2022', 'sku_id': 'ID1',  'sku_price': 20.3}
```





## License
[MIT](https://choosealicense.com/licenses/mit/)
