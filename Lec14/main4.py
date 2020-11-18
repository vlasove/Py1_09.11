"""
Подсчет факториала
n! = n * (n-1) * (n-2) * (n-3) * .. * 1
1! = 1
0! = 1
"""


def factorial(n:int): # -> int:
    """
    function for factorial of N calculation
    n - integer (>=0)
    should return n! >= 1
    """
    if n <= 1: 
        return 1
    else:
        ans = 1
        for i in range(2, n+1):
            ans *= i 
        return ans 

def factorial_call_and_print(start:int, stop:int):
    """
    Функция для того, чтобы вывести значения
    факториала чисел: от start до stop включительно
    С шагом в единицу
    """
    for j in range(start, stop+1):
        print("Factorial: ", "n=",j, "n!=", factorial(j))

factorial_call_and_print(1, 100)