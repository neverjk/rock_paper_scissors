def sum_of_natural_numbers(n):
    try:
        return sum(range(1, n + 1))
    except TypeError:
        print("Будь ласка, введіть ціле число.")
        return None


try:
    number = int(input("Введіть ціле число: "))
    result = sum_of_natural_numbers(number)
    if result is not None:
        print("Сума натуральних чисел до", number, "дорівнює", result)
except ValueError:
    print("Неправильний формат числа. Будь ласка, введіть ціле число.")
