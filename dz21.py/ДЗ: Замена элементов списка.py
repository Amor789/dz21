main_list = []
temporary_list = [None,None]
number = 0

print("Необходимо ввести 5 слов ниже, далее я махну местами первое и последнее")

for i in range(5):
    number += 1
    word = str(input(f"Введите {number} слово: "))
    main_list.append(word)
print(main_list)

temporary_list [0] = main_list [0]
temporary_list [1] = main_list [4]

main_list.pop(0)
main_list.pop(3)

main_list.insert(0, temporary_list[1])
main_list.append( temporary_list[0])
print(main_list)
