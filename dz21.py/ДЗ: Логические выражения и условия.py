try:
    age = int(input("Укажите ваш возраст: "))
    citizenship = input("Вы гражданин РФ? если да то 'y': ")
    disqualified = str(input("Есть ли у вас судимость? если нет то 'n': "))
    
    if age >=18 and citizenship.lower() == 'y'  and disqualified.lower() == 'n':
      print("Указанные данные прошли базовую проверку, Вам можно голосовать")
    else:
      print("Вы не прошли проверку, советуем обратится в пункт голосования!")
        
except ValueError:
       print("Ошибка: В пункте возраст введено не число!")
