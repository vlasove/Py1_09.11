def dangerous(n:int):
    """
    Очень опасная функция
    """
    return 1 / n


try:
    """
    Тут размещаем потенциально-опасный блок кода
    """
    n = int(input())
    print(dangerous(n))
except:
    """
    Что делать, если в try возникло исключение
    """
    print("Don't use Zero value!")

print("Done!")