import string

#колличество слов в тексте
def number_of_words_in_the_text(text):
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    words = [word for word in cleaned_text.split() if word]
    return len(words)


#Самое длинное слово в тексте
def the_longest_word_in_the_text(text):
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    words = cleaned_text.split()

    if not words:
        return ""

    return max(words, key=len)


#Количество гласных в тексте
def number_of_vowels_in_the_text(text):
    slov = set('аеёиоуыэюя')
    count = 0
    for i in text.lower():
        if i in slov:
            count +=1
    return count


#Слова и их повторение
def words_and_their_repetition(text):
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    words = cleaned_text.lower().split()
    word_count = {}


    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


user_text = input("Введите текст для анализа: ")

print(f"Количество слов в тексте {number_of_words_in_the_text(user_text)}")
print(f"Самое длинное слово в тексте {the_longest_word_in_the_text(user_text)}")
print(f"Количество гласных в тексте {number_of_vowels_in_the_text(user_text)}")
print(f"Слова и их повторение {words_and_their_repetition(user_text)}")(poem)}")
print(f"Слова и их повторение {double_t(poem)}")
