def divide_by_zero(numerator, denominator):
    """
    A function which divides numerator by denominator.

    :exception:
        TypeError: if numerator and denominator are not integers , ZeroDivisionError: if denominator is zero
    :param numerator:
    :param denominator:
    :return: a number divided by denominator or 0 if denominator is zero or -1 if the numerator or demoninator is a non-integer.

    examples:
    >>> ans = divide_by_zero(5, 2)
    """
    if not isinstance(numerator, (float, int)) or not isinstance(denominator, (float, int)):
        return -1
    try:
        answer = numerator / denominator
    except ZeroDivisionError:
        return 0
    else:
        return answer