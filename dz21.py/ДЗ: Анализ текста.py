def words(text):
    words = [word for word in text.split() if word]
    return len(words)


def max_len(text):
    words = text.split()
    return max(words, key=len)


def glass_t(text):
    slov = set('аеёиоуыэюя')
    count = 0
    for i in text.lower():
        if i in slov:
            count +=1
    return count


def double_t(text):
    words = text.lower().split()
    word_count = {}

    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

poem = input("Введите текс для анализа: ")

print(f"Количество слов в тексте {words(poem)}")
print(f"Самое длинное слово в тексте {max_len(poem)}")
print(f"Количество гласных в тексте {glass_t(poem)}")
print(f"Слова и их повторение {double_t(poem)}")
