"""
Считать из input.txt и вывести на консоль
"""

# fhand = open("input.txt", "r") # Path_to_file , режим_работы
# # fhand - FileDescriptor
# print(fhand)
# content = fhand.read()
# print(content)
# fhand.close() # Операция закрытия дескриптора/файла

with open("input.txt", "r") as fhand:
    content = fhand.read() # Считывает ВЕСЬ ФАЙЛ ЦЕЛИКОМ В ВИДЕ ОДНОЙ БОЛЬШОЙ СТРОКИ
    print(content)
    new_content = fhand.read()
    print(new_content, fhand.read(), fhand.read())


with open("nums.txt", "r") as fhand:
    nums = [int(x) for x in fhand.read().split()] # [2, 4, 5]
    print("Sum from file:", sum(nums))