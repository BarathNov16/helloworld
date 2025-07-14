# import csv
# import json
# with open('data.csv', 'r') as csvfile:
#     writer = csv.DictReader(csvfile)
#     data = list(writer)
# json_list = []
# for row in data:
#     json_list.append(
#         {row.get("num"): row.get("alpha")}
#     )

# json_str = json.dumps(json_list)
# file = open("test.json", 'w')
# json.dump(json_list, file)

# with open('transfer.json', 'w') as jsonfile:
#     json.dump(data, jsonfile)


from datetime import datetime
print(datetime.now())
