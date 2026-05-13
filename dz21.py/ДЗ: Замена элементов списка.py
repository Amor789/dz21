main_list = []
number = 0

print("Необходимо ввести 5 слов ниже, далее я махну местами первое и последнее")

for i in range(5):
    number += 1
    word = str(input(f"Введите {number} слово: "))
    main_list.append(word)
print(main_list)

main_list[4], main_list[0] = main_list[0],main_list[4]

print(main_list)
