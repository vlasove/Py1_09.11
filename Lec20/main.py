"""
Генераторы - это "ленивые" итераторы.
Генераторы не создают диапазон для итерирования в привычном понимании слова "создать", они
генерируют новый (следующий) элемент по мере обращения к ним.
"""
# my_iterator = [0]* 100000000000
# print("Size:", my_iterator.__sizeof__(), "Bytes")
print(range(1000000000000000000000000000000000).__sizeof__(), "Bytes")
for i in range(100000000000):
    print(i)
    break


"""
Создадим свой генератор
"""
print("===========================================")
def my_generator(n:int):
    """
    Создает диапазон итерирования от 0 до n (не включительно)
    """
    i = 0 
    while i < n:
        yield i  # Оператор отложенного возврата. При выполнении инструкции 
                 # yield - тело функции паузится до момента следующего обращения к функции
        i += 1


def strange_gen():
    yield 10
    yield 20
    yield 30

sg = strange_gen()
print(next(sg))
print(next(sg))
print(next(sg))
print(next(sg))

print("Type of my_gen:", type(my_generator))
gen5 = my_generator(5)
print("Type of my_gen5:", type(gen5))
print("Size:", gen5.__sizeof__(), "Bytes")
# print(next(gen5))
# print(next(gen5))
# print(next(gen5))
# print(next(gen5))
# print(next(gen5))
# print(next(gen5))


for elem in gen5:
    #try:
    #    elem = next(gen5)
    # except StopIteration:
    #    break
    print("Current elem:", elem)