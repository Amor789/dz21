password = "ama_1234_10"

while True:
    pas2 = str(input("Введите пароль: "))

    if pas2 == password:
        print("Вернвый пароль!")
        break
    else:
        print("Не верный пароль, попробуйте ещё раз")
