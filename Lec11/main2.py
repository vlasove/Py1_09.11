"""
Список - это РЕАЛИЗАЦИЯ динамического массива в питоне
"""
nums = [10, 30, 40, -2, -4, -3]

# Удаляем по индексу и возвращаем удаленный элемент
elem = nums.pop(0) # .pop(0) - удалить элемент с индексом 0 из списка
print("Deleted elem:", elem, "List:", nums)
nums.pop(2)
print("List after .pop(2):", nums)

# Всегда проверяйте, что в списке есть то, что удаляем
if len(nums) > 0:
    nums.pop()

# Удаляем по значению .remove() - удаляет первое вхождение
nums = ["Alice", "Bob", "Alice"]
print("Origin:", nums)
nums.remove("Alice") # .remove("Alice") - удалить `"Alice"` из списка
print("After deleting:", nums)

if "GALAKTUS!" in nums:
    nums.remove("GALAKTUS!")