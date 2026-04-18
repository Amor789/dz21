count = 0
count2 = []

data = [i for i in range(0, 101) if i % 2 == 0]
for i in data:
    count += i

data2 = [(lambda i: i*i)(i) for i in range(0, 10) if i % 2 != 0]

print("Вводите числа. Для завершения введите отрицательное число.")

while True:
    try:
        number = int(input("Введите число: "))
        if number < 0:
            break
        count2.append(number)
    except ValueError:
        print("Ошибка! Пожалуйста, введите корректное число.")

print(f"Сумма всех четных чисел от 1 до 100: {count}")
print(f"Квадраты всех нечетных чисел от 1 до 10: {data2}")
print(f"Количество введённых неотрицательных чисел: {count2}")
