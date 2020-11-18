#Required positional args
def add_new(a:int, b:int):
    """
    Супер-пупер документация
    для супер-пупер функции
    Принимает на вход 2 параметра (желательно целочисленных)
    Возвращает результат сложения (арифметического)
    """
    return a**2 + b**3 

# Default value args
def default_func(a:int=1, b:int=1) -> int:
    """
    Функция со значениями по умолчанию
    для параметров входных
    """
    return a**2 + b**3

print(default_func(10, 20))
print(default_func(10))
print(default_func())
print(default_func(b = 20))

