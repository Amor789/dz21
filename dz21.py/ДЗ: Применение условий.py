def to_get_the_sum_of_all_numbers(sum_of_even_numbers):
    data = [i for i in range(0, 101) if i % 2 == 0]
    for i in data:
        sum_of_even_numbers += i
    print(f"Сумма всех четных чисел от 1 до 100: {sum_of_even_numbers}")


def get_the_square_of_odd_numbers():
    the_square_of_odd_numbers = [i * i for i in range(1, 10, 2)]
    print(f"Квадраты всех нечетных чисел от 1 до 10: {the_square_of_odd_numbers}")


def get_the_number_of_entered_numbers(entered_numbers):
    number = 0
    while number >= 0:
        try:
            number = int(input("Введите число: "))
            entered_numbers.append(number)
        except ValueError:
            print("Ошибка! Пожалуйста, введите корректное число.")
    print(f"Количество введённых чисел: {entered_numbers}")


sum_of_even_numbers = 0
entered_numbers = []

to_get_the_sum_of_all_numbers(sum_of_even_numbers)
get_the_square_of_odd_numbers()

print("Введите числа. Для завершения введите отрицательное число.")
get_the_number_of_entered_numbers(entered_numbers)
