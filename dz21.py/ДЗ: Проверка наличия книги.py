def find_book(title):
    if library[title]["Availability"] == True:
        print("Книга доступна")
    elif library[title]["Availability"] == False:
        print("Книга выдана")
    elif library[title]["Availability"] == None:
        print("Книга в библиотеке, но ее статус не определен")
    else:
        print("Такой книги нету)")


library = {
    "Эгоистичный ген": {"author":"Ричард Докинз", "year": 2023, "edition": "CORPUS", "Availability": True },
    "Кровь, пот и пиксели": {"author":"Джейсон Шрейнер", "year": 2012, "edition": "CORPUS", "Availability": False },
    "Иди туда где трудно": {"author":"Таэ Юн Ким", "year": 2023, "edition": "БОМБОРА", "Availability": True },
    "Искусство войны": {"author":"Сунь-цзы", "year": 2000, "edition": "Издательство Стрельбицского", "Availability": True },
    "Homo Sapiens": {"author":"Эдвард Норберд", "year": 2022, "edition": "АСТ", "Availability": None },
    "Автостопом по галактики": {"author":"Дуглас Адамс", "year": 2022, "edition": "NEOCLASSIC", "Availability": True },
    "Парфюмер": {"author":"Патрик Зюскинд", "year": 2012, "edition": "Азбука", "Availability": True }
}

title_book = str(input("Введите название книги: "))
find_book(title_book)
