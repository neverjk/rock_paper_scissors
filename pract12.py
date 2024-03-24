# app.py


def sum_numbers(n):
    """
    Приймає одне додатне ціле число та повертає суму цілих чисел від нуля до вхідного параметра, інакше нуль.

    Параметри:
    n (int): Вхідне ціле число.

    Повертає:
    int: Сума цілих чисел від нуля до n.
    """
    if n < 0:
        return 0

    result = 0
    for i in range(n + 1):
        result += i

    return result


# Приклад використання:
num = int(input("Введіть ціле додатне число: "))
result = sum_numbers(num)
print(f"Сума цілих чисел від 0 до {num}: {result}")
