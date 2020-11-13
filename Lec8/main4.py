"""
D5:E solution
"""

total = set() # Множество студентов, которые были во все дни в семестре
n_days = int(input())

for i in range(n_days):
    n_students = int(input())
    stds = set()
    for _ in range(n_students):
        student = input()
        stds.add(student)
    
    if i == 0: # Это значит , что сейчас самый первый день семестра
        total = total.union(stds)
    else:
        total = total.intersection(stds)

print(len(total))