"""
Второй тип континуального параметра - KeyWords args - аргументы с ключевыми словами
"""
def ccccombo(**kwargs):
    """
    **kwargs принимает на вход аргументы вида a = 2, b= 9, petya = 12
    И конвертирует переданные аргументы в словарь kwargs = {'a' : 2, 'b' :9, 'petya' : 12}
    """
    print("Что такое kwargs:", kwargs)
    print("Тип:", type(kwargs))


ccccombo(a=2, b=9, petya=12)