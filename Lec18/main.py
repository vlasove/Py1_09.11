"""
Исключение - ситуация, в результате возникновения которой
дальнейшее выполнение программы невозможно.

Обработка исключений - набор действий, который совершается программой,
в результате возникновения исключения. Эти действия направлены на выбор
альтернативного пути развития событий.

Пример: пытаемся получить данные - нет интернета,
пытаемся считать из базы - бд удалили.
Делим 2 числа - знаменатель 0.
"""
lst = [10, 20]
print(lst[100])