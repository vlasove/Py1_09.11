"""
Файл содержащий набор функций и переменных, которым будут все пользоваться
Модуль - это любой файл с расширением .py
"""

def add(a:int, b:int):
    """
    a + b 
    """
    return a + b 

def sub(a:int, b:int):
    """
    a - b
    """
    return a - b 

def mult(a:int, b:int):
    """
    a * b 
    """
    return a * b 

def div(a:int, b:int):
    """
    a / b
    """
    return a / b

TEMPERATURE = -21
"""
Секретный секрет №2. - переменная __name___
"""
#print(__name__)


if __name__ == "__main__":
    result = add(10, 20) + sub(20, 30) / mult(200,50000) ** div(10,3)
    print("RESULT OF:", result)
