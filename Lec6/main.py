"""
Цикл while удобен и полезен тогда, когда заранее неизвестно,
сколько итераций нужно выполнить, но есть представление о стоп-сигнале.


Цикл for - используем тогда, когда ЗАРАНЕЕ ИЗВЕСТНО,
сколько итераций нужно выполнить, ИЛИ известен ДИАПАЗОН перебора элементов.
"""
print("range(1, 5, 1)")
for i in range(1, 5, 1): # range(start, stop, step)
                          # в Python правая граница диапазонов НЕ ВКЛЮЧАЕТСЯ ВСЕГДА!
    print("Elem:", i)

print("range(1, 5)")
for i in range(1, 5): # range(start, stop, step=1)
    print("Elem:",i)

print("range(5)")
for i in range(5):# range(start=0, stop, step=1)
    print("Elem:", i)

"""
start, stop, step - ИСКЛЮЧИТЕЛЬНО ЦЕЛЫЕ ЧИСЛА
"""

