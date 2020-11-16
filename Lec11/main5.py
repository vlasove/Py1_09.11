"""
Сортировка списка
"""
nums = ["alice", "word", "bob", "alex", "aaaaaa", "aa", "AAAAAAA", "water", "vodka"]
nums_copy = nums.copy()

# Способ, изменяющий состояние списка .sort(reverse=True) - в обратном порядке
nums.sort(reverse=True)
print("After .sort():", nums)


# Способ, НЕ изменяющий состояние списка
sorted_copy = sorted(nums_copy, reverse=True)
print("After sorted():", sorted_copy)
print("Original:", nums_copy)