"""
Перебор элементов строк
"""

message = "Hello world!"
for i in range(0, len(message), 2):
    print("Letter:", message[i])

for letter in message:
    print("Elem:", letter)
