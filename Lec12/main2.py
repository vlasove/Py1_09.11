# Список из чисел от 1 до 100
nums = [str(i + 2) for i in range(1, 101)] # ListComprehension - списочное выражение

# for i in range(0, 101):
#     nums.append(i)

# print(nums)

"""
Хочу список, в котором четные числа возведены в квадрат, а нечетные - в куб
"""
# qwe = 10 if False else 20
# print(qwe)
strange_nums = [i ** 2 if i % 2 == 0 else i**3 for i in range(1, 101)]

# for i in range(1, 101):
#     if i % 2 ==0:
#         strange_nums.append(i ** 2)
#     else:
#         strange_nums.append(i ** 3)

print(strange_nums)