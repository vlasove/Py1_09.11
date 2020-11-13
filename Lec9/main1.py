"""
D5:H solution
"""

check = set(["ДА" , "дА", "Да", "да"])
message = input()
straight_message = message[0] + message[-1]
reverse_message = message[-1] + message[0]

if straight_message in check or reverse_message in check:
    print("СОГЛАСЕН")
else:
    print("НЕ СОГЛАСЕН") 


