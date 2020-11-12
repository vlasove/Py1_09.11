A = float(input())
B = float(input())
C = float(float())

"""
Ax^2 + Bx + C = 0
"""
if A == 0:
    #Bx + C = 0
    # x = -C/B
    if B == 0:
        print("КОРНЕЙ НЕТ")
    else:
        print("один корень")
else:
    # Ax^2 + ..... = 0
    D = B**2 - 4*A*C 
    if D > 0:
        print("два корня")
    elif D == 0:
        print("один корень")
    else:
        print("корней нет")