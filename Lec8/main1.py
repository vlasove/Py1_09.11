"""
Ссылочность
"""

a_set = set([10, 20, 30])
b_set = a_set.copy() # .copy() создает копию множества и помещает ее в новую облатсь памяти

b_set.add(10000)
print("a_set:", a_set)
print("b_set:", b_set)
