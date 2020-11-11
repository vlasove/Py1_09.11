"""
Подсчет произведения всех введенных значений
"""

mult_result = 1
while True:
    num = int(input())
    if num < 0:
        break 
    else:
        mult_result *= num 

print("Total mult_result:", mult_result)