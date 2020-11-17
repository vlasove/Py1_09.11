# famous =[None] * 2021
# famous[1995] = "Python 1.0 release"
# famous[1997] = "Java release"
# famous[2010] = "GoLang release"
# famous[2020] = "COVID release"

# print(famous)
"""
Словарь - множество пар вида ключ:значение
"""
# Инициализация пустого словаря
empty = {}
# Инициализация словаря
famous = {1995:"Python 1.0 release", 1997:"Java release", 2010:"GoLang Releas", 2020:"COVID release"}
print("Len:", len(famous))
print("1995:", famous[1995])
print("2010:", famous[2010])

# Как добавить новую пару? Одновременно требуется указать как ключ, так и значение
famous[1960] = "First OOP Language Release"
print(famous)