"""
Внешние способы обработки множества
"""

words = set(["bob", "bob", "alice", "jack"])

# 1. Проверка количества элементов len()
print("Len:", len(words))

# 2. Проверка вхождения `in`
print("`derek` in `words`:", "derek" in words)

# 3. Подсчет суммы элементов sum()
# Только для числовых множеств
nums = set([10, 20, 30, 10, 20, 30, 10, 20, 30, -40.5])
print("sum(nums):", sum(nums))
print("nums size ", nums.__sizeof__(), "bytes")

# 4. Поиск минимального/максимального элементов min() max()
# Все элементы множества должны быть сравнимы между собой!!!
max_words = max(words)
min_words = min(words)

max_nums = max(nums)
min_nums = min(nums)
print("Min/max words:", min_words, "/", max_words)
print("Min/max nums:", min_nums, "/", max_nums)



# 5. Перебор элементов при помощи цикла for
# Перебрать все без учета порядка. Порядок абсолютно случайный
for elem in nums:
    print("Element:", elem)