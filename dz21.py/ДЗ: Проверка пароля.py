password = "ama_1234_10"

while True:
    Variant_parolya = (input("Введите пароль: "))

    if Variant_parolya == password:
        print("Верный пароль!")
        break

    print("Не верный пароль, попробуйте ещё раз")
