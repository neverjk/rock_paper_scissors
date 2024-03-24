def sum_of_natural_numbers(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    return total_sum


number = int(input("Введіть ціле число: "))
result = sum_of_natural_numbers(number)
print("Сума натуральних чисел до", number, "дорівнює", result)
