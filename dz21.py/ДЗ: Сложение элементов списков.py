import random

try:
    row_size = int(input("Введи размер строк: "))
    first_list = [random.randint(1, 100) for i in range(row_size)]
    second_list = [random.randint(1, 100) for i in range(row_size)]
    final_list = [first_list[i] + second_list[i] for i in range(row_size)]

except ValueError:
    print("Ошибка: Введите корректное число!")
    
else:
    print(first_list)
    print(second_list)
    print(final_list)
    
finally:
    print("Программа завершена.")
