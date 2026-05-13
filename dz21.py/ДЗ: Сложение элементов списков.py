import random

def get_the_final_list (list_one, list_two):
    final_list = max(len(first_list), len(second_list))
    result = []

    for i in range(final_list):
        element1 = list_one[i] if i < len(list_one) else 0
        element2 = list_two[i] if i < len(list_two) else 0

        sum_element = element1 + element2
        result.append(sum_element)

    return result


try:
    length_of_the_first_list = int(input("Введите длину первого списка: "))
    length_of_the_second_list = int(input("Введите длину второго списка: "))

    first_list = [random.randint(1, 100) for i in range(length_of_the_first_list)]
    second_list = [random.randint(1, 100) for i in range(length_of_the_second_list)]

    final_list = get_the_final_list(first_list, second_list)

except ValueError:
    print("Ошибка: Введите корректное число!")

else:
    print(first_list)
    print(second_list)
    print(final_list)

finally:
    print("Программа завершена.")
