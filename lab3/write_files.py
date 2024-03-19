import requests
import json

from generate import generate_words
from generate import generate_letters


def write_file_words(file, n):
    url = "https://raw.githubusercontent.com/LussRus/Rus_words/master/UTF8/json/raw/summary.json"
    response = requests.get(url)
    words_list = json.loads(response.content.decode('utf-8'))

    random_words = generate_words(words_list, n)

    if len(random_words) < n:
        random_words += ' '

    with open(file, 'w', encoding='utf-8') as file:
        file.write(random_words)

def write_file_letters(file, n):
    random_letters = generate_letters(n)

    with open(file, 'w', encoding='utf-8') as file:
        file.write(random_letters)
