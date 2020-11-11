"""
Простейший алгоритм поиска мин/макс из входных данных
"""

i = 0 # Который просматривает количество уже ввденных чисел
currentMax = None 
currentMin = None 

while True:
    num = int(input())
    if num < 0:
        break 
    if i == 0:
        currentMax = num 
        currentMin = num 
    else:
        if currentMax < num:
            currentMax = num 

        if currentMin > num:
            currentMin = num
    i += 1

print("Maximum:", currentMax)
print("Minimum:", currentMin)

