"""
Module docstring
"""


def add(a_arg: int, b_arg: int):
    """
    a_arg + b_arg
    """
    return a_arg + b_arg


def sub(a_arg: int, b_arg: int):
    """
    a_arg - b_arg
    """
    return a_arg - b_arg


def mult(a_arg: int, b_arg: int):
    """
    a_arg * b_arg
    """
    return a_arg * b_arg


def div(a_arg: int, b_arg: int):
    """
    a_arg / b+arg
    """
    return a_arg / b_arg


TEMPERATURE = -21

# print(__name__)


if __name__ == "__main__":
    RESULT = add(10, 20) + sub(20, 30) / mult(200, 50000) ** div(10, 3)
    print("RESULT OF:", RESULT)
