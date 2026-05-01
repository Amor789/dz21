password = "ama_1234_10"

while 1 == 1:
    password_2 = str(input("Введите пароль: "))

    if password_2 == password:
        print("Верный пароль!")
        break

    print("Не верный пароль, попробуйте ещё раз")
