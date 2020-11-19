"""
Считывание из файла input.txt  в виде набора строк
"""

with open("input.txt", "r") as fhand:
    lines = [x.strip() for x in fhand.readlines()]
    print(lines)