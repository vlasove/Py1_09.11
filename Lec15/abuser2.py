"""
Подгрузка модуля funcs.py с совмещенной областью именования
"""

from funcs import add, sub, mult


def add2(a,b):
    print("MY ADD HERE!")
    return a**2 + b**3

print("Add:", add(2, 10))
print("Sub:", sub(2, 10))
print("Mult:", mult(3, 4))