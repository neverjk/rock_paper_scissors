def sum_numbers(n):
    """
    Приймає одне додатне ціле число та повертає суму цілих чисел від нуля до вхідного параметра, інакше нуль.

    Параметри:
    n (int): Вхідне ціле число.

    Повертає:
    int: Сума цілих чисел від нуля до n або нуль, якщо n від'ємне.
    """
    try:
        if n < 0:
            return 0

        return sum(range(n + 1))
    except TypeError:
        return 0


try:
    num = int(input("Введіть ціле додатне число: "))
    result = sum_numbers(num)
    print(f"Сума цілих чисел від 0 до {num}: {result}")
except ValueError:
    print("Введено некоректне значення. Будь ласка, введіть ціле додатне число.")
