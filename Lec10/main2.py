"""
Сравнение строк. В Python все строки - Unicode.
"""
print("A > a:", "A" > "a")
print("A is:", ord("A"))
print("a is:", ord("a"))
print("66 is:", chr(66))
print("98 is:", chr(98))


print("ABCD" < "ABCE")

"""
'ABCD' VS 'a'
Лексико-графический порядок сравнения (как в словарь)
"""

print("ABCD" < "a")