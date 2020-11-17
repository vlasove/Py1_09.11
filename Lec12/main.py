"""
Связующие методы у строк и списков
"""
message = "#################Hello Bob it's me Mario##############"
message = message.strip("#") # Отрубает все пустотые слева и справа от строки
print(message)


words = message.split() # .split() это строковый метод
print("Words:", words)

"""
Как из списка слов сделать предлолжение?
"""
new_words = ["Alice", "Bob", "John"] # список из строковых элементов
ans = ", ".join(new_words) # .join() - строковый метод
# for i in range(len(new_words)):
#     if i >= len(new_words) - 1:
#         ans += new_words[i]
#     else:
#         ans += new_words[i] + ", "

print(ans)