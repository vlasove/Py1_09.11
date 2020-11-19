"""
Запись в файл
"w" - ПЕРЕзапись
"""
nums = [10,20,30]
with open("output.txt", "w") as fhand:
    fhand.write("[" + ", ".join([str(x) for x in nums]) + "]\n") # write(str), где str - одна неделимая строка