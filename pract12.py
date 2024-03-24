def sum_numbers(n):
    """
    Приймає одне додатне ціле число та повертає суму цілих чисел від нуля до вхідного параметра, інакше нуль.

    Параметри:
    n (int): Вхідне ціле число.

    Повертає:
    int: Сума цілих чисел від нуля до n або нуль, якщо n від'ємне.

    Приклади:
    >>> sum_numbers(5)
    15
    >>> sum_numbers(0)
    0
    >>> sum_numbers(-3)
    0
    """
    try:
        if n < 0:
            return 0

        return sum(range(n + 1))
    except TypeError:
        return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
