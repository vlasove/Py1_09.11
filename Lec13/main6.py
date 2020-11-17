"""
Стандартные операции над коллекциями
"""
famous = {1995:"Python 1.0 release", 1997:"Java release", 2010:"GoLang Releas", 2020:"COVID release"}

# По умолчанию - проверка идет только по ключам
if 1997 in famous:
    print("1997 in famous!")

# Явная проверка по ключам
if 1997 in famous.keys():
    print("1997 in famous!")

# Явная проверка по значениям
if "Python 1.0 release" in famous.values():
    print("Python release!")


# Итерирование (по умолчанию только по ключам)
for elem in famous:
    print(elem)


# Итерирование явно по ключам
for key in famous.keys():
    print("Key:", key, "Val:", famous[key])

# Итерирование явно по значениям
for val in famous.values():
    print("Val:", val)

# Итерирование явное ПАРАМИ
for key , val in famous.items(): #[(1995, "Python"), (1997, "Java") ...]
    print("Key:", key, "Val:", val)