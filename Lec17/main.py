"""
Считать из input.txt и вывести на консоль
"""

fhand = open("input.txt", "r") # Path_to_file , режим_работы
# fhand - FileDescriptor
print(fhand)
content = fhand.read()
print(content)
fhand.close() # Операция закрытия дескриптора/файла