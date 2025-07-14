import csv
from loguru import logger
# logger.add(sink=lambda msg: print(msg, end=""))
with open("data.csv") as file:  # file variable name
    reader = csv.DictReader(file)
    data = list(reader)
    we = data
    # for row in data:
    #  print(row)
    # if int(row['num']) % 2 == 0:
    # logger.info(row.get("alpha"))
    # print(row.get("alpha"))
    # logger.info(data[::2])
get_odd = data[::2]
# for i in get_odd:
# logger.info(i.get("alpha"))
get_even = data[1::2]
for k in get_even:
    logger.info(k.get("alpha"))

# get_even2 = filter(lambda x: x % 2 == 0, data)
# print(list(get_even2))


# print(file)
# reader = csv.DictReader(file)
#pack(*we)
