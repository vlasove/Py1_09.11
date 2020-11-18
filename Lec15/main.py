"""
Правило смешивания параметров - сначала все позициональные, затем все дефолтные
"""
def combo_adder(a:int, b:int, c:int=0) -> int:
    """
    Супер описание
    """
    return a + b + c 


print(combo_adder(2,3,4))
print(combo_adder(1,2))