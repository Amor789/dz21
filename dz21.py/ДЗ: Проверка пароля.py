password = "ama_1234_10"

while True:
    user_input = (input("Введите пароль: "))

    if user_input == password:
        print("Верный пароль!")
        break

    print("Не верный пароль, попробуйте ещё раз")
