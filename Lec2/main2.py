"""
Вывод нескольких значений
"""

# Подряд через пробел
word1 = "First"
word2 = "Second"
word3 = "Third"

print(word1, word2, word3, "Fourth!")
# Но что если хочется не через пробел? А хочется слитно
# Пример: конкатенация
total_word = word1 + word2
print(total_word)
# Конкатенация на месте
print(word1 + word2)
# Конкатенация и дополнительные перечисления
print(word1 + word2, word3)