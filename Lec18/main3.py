"""
Использование типизированных исключений
За раз выполняется только один обработчик
"""


def dangerous(n:int):
    """
    Очень опасная функция
    """
    return 1 / n

n = None
try:
    n = int(input())
    print(dangerous(n))
except ZeroDivisionError as z_err:
    print("Don't use Zero value:", z_err)
except ValueError as v_err:
    print("Only integer number:", v_err)  
except KeyboardInterrupt as k_err:
    print("Don't use CTRL+C:", k_err)
except:
    print("SOMETHING WENT WRONG!")

print("Done!")