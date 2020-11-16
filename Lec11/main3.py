"""
Общее для коллекций в языке
"""
nums = [10, 20, 30, -4, -3, -10]

# Проверка вхождения
if 10 in nums:
    print("10 in nums!")

# Переборы циклами
for i in range(0, len(nums), 1):
    print("Id:", i, "Elem[id]:", nums[i])

for val in nums:
    print("Elem:", val)

# Взятие среза
reversed_nums = nums[::-1]
print('Reverse slice:', reversed_nums)


# sum(), min(), max()
print("Sum():", sum(nums))
words = ["a", "ab", "ba"]
print("Min()/max():", min(nums), "/", max(nums))
print("words: min():", min(words), "max():", max(words))