"""
Оператор множественного выбора
"""
age = int(input())

if age <= 14:
    print("Do1")
elif age > 14 and age <= 18:
    print("Do2")
elif age > 18 and age <= 25:
    print("Do3")
else:
    print("Do4")

print("Done")