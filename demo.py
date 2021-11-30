from datetime import datetime
my_date = datetime.now()
print(my_date.strftime('%Y-%m-%dT%H:%M:%S.%f%z'))
print(my_date.isoformat())