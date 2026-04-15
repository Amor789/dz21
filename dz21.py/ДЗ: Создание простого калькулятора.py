print("Добро пожаловать в кальекулятор!")

while True:
   try:
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
       if operation == '+':
           print('Сложение')
           result = a + b
       elif operation == '-':
            print('Вычитание')
            result = a - b
       elif operation == '/':
            print('Деление')
            result = a / b
       elif operation == '*':
            print('Умножение')
            result = a * b
       else:
            print('Неизвестная операция')

       print("Результат:", result)
       
   except ZeroDivisionError:
       print("Камон, на ноль делить нельзя!")
   except ValueError:
       print("Ошибка: введено не число!")
       
   сhoice = input("Продолжим?\n" "'Y' это значит да ")
   if сhoice.lower() == "y":
       True
   else:
       print("Программа завершина) Чао")
       break



