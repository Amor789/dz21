try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    result = a // b
    print(f"Результат целочисленного деления: {result}")

except ValueError:
    print("Ошибка: введено не число!")
except ZeroDivisionError:
    print("Камон, на ноль делить нельзя!")
else:
    print("Операция выполнена успешно.")
finally:
    print("Программа завершена. Чао!")