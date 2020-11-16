new_message = "hEllo WoRlD22!"
message = new_message[:-3]

# Перевод строки в верхний регистр
upper_word = message.upper()
print("UPPER:", upper_word)

# Перевод строки в нижний регистр
lower_word = message.lower()
print('lower:', lower_word)

# Перевод строки : Первый символ - прописаной, все остальные - строчные
Capitalize_word = message.capitalize()
print("Capitalize:", Capitalize_word)


"""
Полный список  методов
"""
#print(dir(message))
"""
Как узнать, сколько символов `l` содержится в строке?
"""

counter = message.count("l")
print("l in message:", counter)

"""
Как узнать индекс первого вхождения элемента `l`?
"""
id_ = message.index('l')
print("Message:", message, "Id of `l`:", id_)
