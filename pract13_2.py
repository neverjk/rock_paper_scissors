def sum_of_natural_numbers(n):
    return sum(range(1, n + 1))


# Приклад використання функції:
number = int(input("Введіть ціле число: "))
result = sum_of_natural_numbers(number)
print("Сума натуральних чисел до", number, "дорівнює", result)
