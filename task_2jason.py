import json
import csv
import time
from datetime import datetime
e_time = int(time.time())
e_timekey = {"epochtime": e_time}
json_list = []


with open("data.csv") as file:
    reader = csv.DictReader(file)
    data = list(reader)
    for _data in data:
        date = datetime.now().date()
        time = datetime.now().time()
        epooch_timestamp = datetime.now().timestamp()
        _data.update(
            {
                "date": date,
                "time": time,
                "eppoch": epooch_timestamp
            }
        )
        json_list.append(_data)


with open('data.json', 'w') as f:
    json.dump(json_list, f)

