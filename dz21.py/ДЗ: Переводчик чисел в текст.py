try:
    number = int(input("Введите число в диапазоне от 1 до 5: "))
except ValueError:
    print("Ошибка: введено не число!")

number_dict = {
    "1": " One",
    "2": " Two",
    "3": " Three",
    "4": " Four",
    "5": " Five"
}

if number == 1:
    print(f"Соответствующее слово:{number_dict["1"]}")
elif number == 2:
    print(f"Соответствующее слово:{number_dict["2"]}")
elif number == 3:
    print(f"Соответствующее слово:{number_dict["3"]}")
elif number == 4:
    print(f"Соответствующее слово:{number_dict["4"]}")
elif number == 5:
    print(f"Соответствующее слово:{number_dict["5"]}")
else:
    print("Вы не попали в диапазон от 1 до 5, попробуйте позже")
