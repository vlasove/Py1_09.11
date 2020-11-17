"""
D6:B solution
Как вырезать фамилию из входной строки
"""


message = "Кто последний? Я - Кузнецов." #input()
temp = message.split(" - ") # ["Кто последний? Я", "Кузнецов."]
sample = temp[-1].split(".") # "Кузнецов.".split(".") # ["Кузнецов", ""]
lastname = sample[0]

# Для тру-хацкеров
lastname = message.split(" - ")[-1].split(".")[0]

print("Lastname:", lastname)