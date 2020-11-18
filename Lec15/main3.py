"""
Смешение континуальных параметров
"""
def freak(*args:int, **kwargs):
    """
    Считает произведение всех args
    Конкатенирует имена всех ключей kwargs
    Считает сумму всех значений в kwargs
    """
    result_mult = 1
    for elem in args:
        result_mult *= elem 
    
    result_concat = ""
    for key in kwargs.keys():
        result_concat += key
    
    result_sum = 0
    for val in kwargs.values():
        result_sum += val 

    print("Общее произведение args:", result_mult)
    print("Конкатенация ключей:", result_concat)
    print("Сумма значений:", result_sum)

freak(10, 20, 30, 40, a=2, b=4, c=200, d=10000000)
