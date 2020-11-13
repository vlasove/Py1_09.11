"""
Как опустошать множества
"""

a_set = set(["Bob", "Alice", 10, 20])
# .pop() - удаляет СЛУЧАЙНЫЙ ЭЛЕМЕНТ, и возвращает его
deleted_elem = a_set.pop()
print("First deleted elem:", deleted_elem)
if len(a_set) > 0:
    second_elem = a_set.pop()
    print("Second deleted elem:", second_elem)
print("A_set after .pop():", a_set)

b_set = set([10, 20, 30, "Hello", "Bob"])

# .remove() - удаляет конкретный элемент. Ничего не возвращает
if "Bob" in b_set:
    b_set.remove("Bob")
print("B_set after .remove():", b_set)


# .clear()
a_set.clear()
print(a_set)


