"""
Кортеж - упорядоченная(индексируемая) коллекция, способная хранить элементы ЛЮБОГО типа,
при этом - не изменяемая.
"""

# Инициализация пустого кортежа
a_tuple = tuple()
b_tuple = ()

print("Tuple:", b_tuple, "Type:", type(b_tuple), "Len:", len(b_tuple))

# Кортеж с элементами
c_tuple = (1,2,3,4,5)
one_tuple = (10,)
print("Tuple:", one_tuple, "Type:", type(one_tuple), "Len:", len(one_tuple))

# Какие методы есть у кортежа?
#print(dir(c_tuple))

# Конкатенация кортежей
new_tuple = (1,2,3,4) + (2,3,4,7)
print(new_tuple)