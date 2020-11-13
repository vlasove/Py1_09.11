"""
Строка - упорядоченная (индексируемая) коллекция, которая хранит элементы ОДНОГО типа.
"""

message = "Hello world!"  # Каждый элемент - односимвольная строка

# Обращение к элементу строки по индексу
print("First letter:", message[0])
print("Second letter:", message[1])
print("Last letter:", message[len(message) - 1])
print("Last letter:", message[-1])
print("Prelast letter:", message[-2])


# Элемент строки - это строка
total = "Bob is "

ans = total + message[0] + message[1]
print(ans)

# Длина строки
print("Len:", len(ans))

# Проверка вхождения
print("Bo" in ans)
a = b = c = d = 20
