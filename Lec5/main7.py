"""
Определение количества введенных чётных чисел
"""

evens = 0

while True:
    num = int(input())
    if num < 0:
        break 
    else:
        if num % 2 ==0:
            evens+=1

print("Total amount of even vals:", evens)