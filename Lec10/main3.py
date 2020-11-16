"""
Срезы строк
"""
message = "Hello#Bob!"
my_word = message[0:5:1]#message[0] + message[1] + message[2] + message[3] + message[4]
print("My word:", my_word)

print("======DEFAULT STEP========")
stepper_word = message[0:5]
print("Default step 1:", stepper_word)

print("======Left Board = 0, Step = 1 ======")
zero_start = message[:5]
print("zero start = 0:", zero_start)

print("======Right Board = len(), Step = 2 ========")
zero_finish = message[6::2]
print("zero finish = len():", zero_finish, type(zero_finish))


"""
Операция взятия среза message[a:b] создает:
1) Результатом взятия среза  является коллекция того же типа
2) В результате взятия среза СОЗДАЕТСЯ КОПИЯ элементов
"""

if "a" in message[2:6]:
    print()

for letter in message[0:8:2]:
    print(letter)


reverse = message[::-1]

print("Reverse:", reverse)
print(message[-1:5]) #message[len(message) - 1 : 5 : 1] => message[9:5:1] => ""