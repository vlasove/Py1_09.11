"""
Операции над двумя множествами
"""
a_set = set([1,2,3,4])
b_set = set([3,4,5,6])

intersect = a_set.intersection(b_set)
print("Intersection:", intersect)

uni = a_set.union(b_set)
print("Union:", uni)

diffA = a_set.difference(b_set)
diffB = b_set.difference(a_set)
print("A/B:", diffA)
print("B/A:", diffB)

sym_diff = a_set.symmetric_difference(b_set)
print("A^B:", sym_diff)



