def book_list_view(library):
    for key, value in library.items():
        if value["Availability"]:
            print(f"{key}: есть на полках")
        else:
            print(f"{key}: нет в наличии")


def add_book(title, author, year):
    if title in library:
        print(f"Книга \"{title}\" уже существует в библиотеке.")
        update = input("Хотите обновить информацию о ней? (да/нет): ").lower()
        if update in ('да', 'yes', 'y'):
            library[title]["author"] = author
            library[title]["year"] = year
            print(f"Информация о книге \"{title}\" успешно обновлена!")
        else:
            print("Обновление отменено.")
    else:
        library_n = {
            title: {"author":author,"year": year,"edition":None, "Availability": None}
        }
        library.update(library_n)

    return (library), print(f"Книга \"{title}\" успешно добавлена!")


def remove_book(title):
    if title in library:
        del library[title]
        print(f"Книга \"{title}\" удалена")
    else:
        print("Книга не найдена! ")


library = {
    "Эгоистичный ген": {"author":"Ричард Докинз", "year": 2023, "edition": "CORPUS", "Availability": True },
    "Кровь, пот и пиксели": {"author":"Джейсон Шрейнер", "year": 2012, "edition": "CORPUS", "Availability": False },
    "Иди туда где трудно": {"author":"Таэ Юн Ким", "year": 2023, "edition": "БОМБОРА", "Availability": True },
    "Искусство войны": {"author":"Сунь-цзы", "year": 2000, "edition": "Издательство Стрельбицского", "Availability": True },
    "Homo Sapiens": {"author":"Эдвард Норберд", "year": 2022, "edition": "АСТ", "Availability": True },
    "Автостопом по галактики": {"author":"Дуглас Адамс", "year": 2022, "edition": "NEOCLASSIC", "Availability": True },
    "Парфюмер": {"author":"Патрик Зюскинд", "year": 2012, "edition": "Азбука", "Availability": True }
}

del_name = input("Введите книгу для удаления: ")
remove_book(del_name)
