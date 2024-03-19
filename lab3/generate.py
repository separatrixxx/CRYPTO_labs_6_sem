import random


def generate_letters(length):
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    return ''.join(random.choice(letters) for _ in range(length))

def generate_words(word_list, length):
    text = ""
    
    while len(text) < length:
        space_left = length - len(text)  # Считаем, сколько места осталось без учёта пробела

        if space_left <= 8:  # Если остаток символов 8 и меньше - на тестах именно при таком показателе точность составляет около 99%
            # Ищем слова, которые подойдут для оставшегося места
            fitting_words = [w for w in word_list if 1 <= len(w) <= space_left]
            
            if fitting_words:
                # Выбираем самое длинное подходящее слово
                word = max(fitting_words, key=len)

                if len(text) + len(word) <= length:
                    text += word  # Добавляем слово без дополнительного пробела, если оно вмещается
                break  # Выходим из цикла после добавления
        else:
            # Если места больше 8 символов, добавляем любое подходящее слово
            possible_words = [w for w in word_list if len(text) + len(w) + 1 <= length]

            if possible_words:
                word = random.choice(possible_words)
                text += word + " "  # Добавляем слово и пробел
            else:
                break  # Нет подходящих слов, выходим из цикла

    return text.rstrip()

def test_generate_words():
    sample_words = ["дом", "собака", "прогулка", "цветок", "книга", "окно", "музыка", "ночь", "день", "человек",
                    "да", "ням", "лес", "он", "я", "мама", "яблоко", "ложка"]
    n = 100
    m = 100
    k = 100

    sum = 0
    
    for _ in range(k):
        count = 0
    
        for _ in range(m):
            word = generate_words(sample_words, n)

            if len(word) == n:
                count += 1

        sum += count / m

    print(sum / k)