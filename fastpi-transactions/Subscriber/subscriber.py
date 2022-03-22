'''
The subscriber will be used to subscribe for the message

urls:
http://127.0.0.1:8000/transaction-summary-bycategory/{last-n-days}

http://127.0.0.1:8000/transaction-summary-bySKU/{last-n-days}

http://127.0.0.1:8000/transaction/{transaction_id}

'''

import csv
import json
import requests

Host=" http://127.0.0.1:8000"



res=requests.get('http://127.0.0.1:8000/transaction/1')
print(res.json())










    
        