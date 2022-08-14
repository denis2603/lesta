
def isEven(value): return value % 2 == 0


# Решение
def is_even_fast(value: int) -> bool:
    """
    Определение четности числа.
    :param value: Целое число.
    :return: True - если число четное, False - если число не четное.
    """
    return not(value & 1)
