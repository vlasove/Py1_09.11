message = "Hello Bob!"
print("First:", message[0])
"""
Массив - это мат.модель.
Реализация массив - то, что есть языке (что-то массиво-подобное).
Строка - реализация "массива" из символов.
Строка - упорядоченная (индексируемая) коллекция, способная хранить элементы одного типа.
"""
print("Last:", message[-1])
#print("Error:", message[100])

for i in range(0, len(message), 1):
    print("Id:", i, "Elem[id]:", message[i])

print("for .... collection")
for letter in message:
    print("Elem:", letter)

