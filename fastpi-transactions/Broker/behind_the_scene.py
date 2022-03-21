from datetime import datetime
def string_todate(obj):
     date_time_obj = datetime.strptime(obj.strip(), '%d/%m/%Y').date()
     print(date_time_obj)
     return date_time_obj
