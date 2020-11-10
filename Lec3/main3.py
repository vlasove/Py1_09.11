"""
Строка - последовательность символов заключенная в кавычки
"""
# В Python нет такого типа как char()

message = "Hello Brain O'Connor!"
letter = "q"
empty = ""

# В Питоне можно использовать два типа кавычек "", ''
equal_message = 'Hell"o" Bob!'

"""
Правило - той кавычкой, какой открывали строку, такой же и закрываем
"""

# 1. Конкатенация
total = message + " " + equal_message
print(total)
# 2. Конкатенация через умножение НА НАТУРАЛЬНОЕ ЧИСЛО
word = 'Dog'
zero_dog = word * 10
print(type(zero_dog)) 
print(zero_dog)

# 3. Узнать длину
length = len(word)
print("Word length:", length)


# 4. Приведение к строке
a_int = 10
b_int = 20

total = str(a_int) + str(b_int)
print("Total:", total)



