"""
Создадим хранилище дней рождений
Допустим у вас 10 друзей
Информацию про каждого вы будете заносить в виде: Витя 12 дек, Катя 13 май,....
"""
# Выбираем схему хранилища как Ключ: месяц, Значение: [список людей, родившихся в этот месяц]
birth = {}
for _ in range(5):
    message = input() # "Витя 12 дек"
    sample = message.split()
    name, month = sample[0], sample[-1]
    if month in birth.keys():
        birth[month].append(name)
    else:
        birth[month] = [name]
    
print(birth)

