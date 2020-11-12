"""
Вложенные циклы.
"""
stopFlag = False
q = 10
for i in range(1, q):
    for j in range(1, 5):
        print(i, "*", j, "=", i *j)  
        if j == 3:
            stopFlag = True
            break
    if stopFlag:
        break
