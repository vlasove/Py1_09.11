"""
Построчное считывание из файла
"""

with open("input.txt", "r") as fhand:
    current_line = fhand.readline()
    while  current_line != "": # EOF
        print(current_line.strip())
        current_line = fhand.readline()