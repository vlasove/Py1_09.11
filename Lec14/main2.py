# 4. Явные функции(с параметрами, возвращающие значение)
def strange_add(a,b): #  Параметрическая сигнатура (сигнатура)
    ans = a**2 + b**3
    return ans #  Вычисляется до возврата


result = strange_add(10, 20) # Вызов функции с передачей конкретных значений параметров
print("Result strange_add(10,20):", result)
print("Result strange_add(20, 10):", strange_add(20, 10))