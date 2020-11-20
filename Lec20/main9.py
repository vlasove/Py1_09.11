"""
Лямбда-выражения (анонимные фукнции - у них нет имени)
"""
def add(a:int, b:int):
    """
    a + b
    """
    return a + b

# Не надо писать название, не надо аннотировать типы параметров
# Не надо писать слово return
anon_add = lambda a,b: a + b
print("Func add:", add, "Res:", add(2,3))
print("Anon add:", anon_add, "Res:", anon_add(2,3))
