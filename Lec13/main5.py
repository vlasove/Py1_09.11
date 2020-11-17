"""
Изменяемый ли словарь или нет? Да!
"""
famous = {1995:"Python 1.0 release", 1997:"Java release", 2010:"GoLang Releas", 2020:"COVID release"}
print("Origin:", famous)
# Если ключ существовал раннее - то перезапишем значение
# Если такого ключа еще не было, то добавим новую пару
famous[2020] = "Python 3.9.0 release"
print("After :", famous)