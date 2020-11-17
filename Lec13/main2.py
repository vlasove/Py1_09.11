"""
Специфичные операции
"""
nums = (10, 20, 30)
a, _, c  = nums # Раскрытие кортежа `Tuple unpack`

print("a:", a, "b: empty _ ", "c:",c)

#one, two = input(), input()

"""
Кортежи можно сравнивать
Точно также как и строки
"""
one = (10, 20, 30)
two = (100, 200)

print("one < two:", one < two)