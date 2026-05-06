import string

#колличество слов в тексте
def get_number_of_words_in_the_text(text):
    words = [word for word in text.split() if word]
    return len(words)


#Самое длинное слово в тексте
def get_the_longest_word_in_the_text(text):
    words = text.split()

    if not words:
        return ""

    return max(words, key=len)


#Количество гласных в тексте
def get_the_number_of_vowels_in_the_text(text):
    vowels = set('аеёиоуыэюя')
    count = 0
    for symbol in text.lower():
        if symbol in vowels:
            count +=1
    return count


#Слова и их повторение
def get_the_words_and_their_repetition(text):
    words = text.lower().split()
    word_count = {}


    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count



user_text = input("Введите текст для анализа: ")
processed_text = user_text.translate(str.maketrans('', '', string.punctuation))

print(f"Количество слов в тексте {get_number_of_words_in_the_text(processed_text)}")
print(f"Самое длинное слово в тексте {get_the_longest_word_in_the_text(processed_text)}")
print(f"Количество гласных в тексте {get_the_number_of_vowels_in_the_text(processed_text)}")
print(f"Слова и их повторение {get_the_words_and_their_repetition(processed_text)}")
