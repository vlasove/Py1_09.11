"""
Блоки- else и finally
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
else:
    """
    Выполняется только тогда, когда не было выброшено исключение в блоке try
    """
    print("Else block working!")
finally:
    """
    Выполняется всегда
    """
    print("Finally block working!")


print("Done!")