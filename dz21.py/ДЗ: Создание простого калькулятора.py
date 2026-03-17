print("Добро пожаловать в кальекулятор!")

while True:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    message = '''
        Выберете математическую операцию:

        + : Сложение
        - : Вычитание
        / : Деление
        * : Умножение

        Ваш выбор:
        '''
    operation = input(message)

    try:
        if operation == '+':
            print('Сложение')
            result = a + b
        elif operation == '-':
            print('Вычитание')
            result = a - b
        elif operation == '/':
            print('Деление')
            try:
                result = a / b
            except ZeroDivisionError:
                print("Камон, на ноль делить нельзя!")

        elif operation == '*':
            print('Умножение')
            result = a * b
        else:
            print('Неизвестная операция')

        print("Результат:", result)


    except ValueError:
        print("Ошибка: введено не число!")
    else:
        print("Операция выполнена успешно.")
    b = input("Продолжим?\n" "'Y' это да, 'N' это нет\n")
    if b == "Y" or b == "y":
        True
    elif b == "n" or b == "N":
        print("Программа завершина) Чао")
        break




