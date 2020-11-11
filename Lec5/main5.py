"""
Подсчет суммы всех введенных значений
"""

summ = 0
while True:
    num = int(input())
    if num < 0:
        break 
    else:
        summ += num 

print("Total sum:", summ)