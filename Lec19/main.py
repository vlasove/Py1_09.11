"""
Модуль для работы с регулярными выражениями
"""
import re 

"""
Регулярное выражение - это последовательность символов, которая используется для 
замен и поиска текста в входных строках, файлах, базах данных и т.д.


Чаще всего используются для:
* Замены подстроки или ее части
* Разделение целостных строк на подстроки
* Задачи поиска на строках
"""

"""
Начинка модуля re состоит из:

* re.match() - поиск по шаблону В НАЧАЛЕ СТРОКИ
* re.search() - поиск по шаблону ВО ВСЕЙ СТРОКЕ
* re.findall() - поиск совпадений
* re.split() - разделение строки по шаблону
* re.sub() - замена шаблона в подстроке
* re.compile() - компиляция шаблона в виде отдельного объекта
"""


# re.match()
result = re.match(r'Python', "Python is a programming language for pro!")
print(result)
if result is not None:
    print("Что нашли:", result.group(0))
    print("Start:", result.start())
    print("Finish:", result.end())


print("==========================================================")
result = re.search(r'Java', "This is Java Programming Language")
print(result)
if result is not None:
    print("Что нашли:", result.group(0))
    print("Start:", result.start())
    print("Finish:", result.end())

print("=========================================================")
result = re.findall(r'Go', "This is Go . Go? Go!")
print(result)

print("=========================================================")
result = re.split(r'[;,\s]', "It's, all ; All,p it's")
print(result)


print("=========================================================")
result = re.sub(r'Python', "C++", "Python is the best programming Python Language!")
print(result)


print("========================================================")
template = re.compile(r'Python')
print(template.findall("Python Python cool!"))

"""
Рассмотрели первый вид шаблонов - литеральные
Есть еще шаблоны на основе спец символов - на основе специального синтаксиса -
синтаксис регулярных выражений
"""

"""
Operator                    Description
.                           Абсолютно любой символ (кроме new line \n)
+                           1 и более вхождений шаблона слева
*                           0 и более вхождений слева
\w                          Любая цифра или буква
\W                          ВСЕ ЧТО УГОДНО, КРОМЕ БУКВЫ И ЦИФРЫ
"""

message = "It is Bob#from !NY?"
result = re.findall(r'\w*', message)
print(result)












