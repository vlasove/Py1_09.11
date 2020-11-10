"""
D1:S solution
"""

# Организовали ввод
num = float(input())

# Блок анализа
if abs(num) < 0.0001: #num >= -0.0001 and num <= 0.0001:
    # Блок вывода
    print("ОЧЕНЬ МНОГО")
else:
    # Блок вывода
    print(num ** -1)