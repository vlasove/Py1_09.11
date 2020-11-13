"""
D5:A solution
"""
from_home_to_park = set()
from_park_to_home = set()

# Заполняем первое множество
while True:
    message = input()
    if message == "": #len(message) == 0
        break
    else:
        bus_num = int(message)
        from_home_to_park.add(bus_num)

# Заполняем второе множество
while True:
    message = input()
    if message == "": #len(message) == 0
        break
    else:
        bus_num = int(message)
        from_park_to_home.add(bus_num)

total = from_home_to_park.intersection(from_park_to_home)
print(len(total))