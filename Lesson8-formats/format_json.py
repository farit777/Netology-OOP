import os
import json
from collections import Counter

print(os.getcwd())

def load_json_file(file_path):
    """Загружает JSON файл и возвращает его содержимое."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def extract_words(data):
    """Извлекает слова из описаний и заголовков новостей."""
    words = []
    for item in data['rss']['channel']['items']:
        # Извлекаем заголовок и описание
        title = item['title']
        description = item['description']
        
        # Добавляем слова в список
        words.extend(title.split())
        words.extend(description.split())
    
    return words

def filter_long_words(words, min_length=6):
    """Фильтрует слова по минимальной длине."""
    return [word for word in words if len(word) > min_length]

def count_word_frequencies(words):
    """Подсчитывает частоту слов и возвращает 10 самых распространенных."""
    word_counts = Counter(words)
    return word_counts.most_common(10)

def main():
    # Загружаем данные из JSON
    file_path = 'Lesson8-formats/newsafr.json'
    data = load_json_file(file_path)
    
    # Извлекаем слова
    words = extract_words(data)
    
    # Фильтруем длинные слова
    long_words = filter_long_words(words)
    
    # Подсчитываем частоту и получаем топ-10
    top_words = count_word_frequencies(long_words)
    
    # Выводим результат
    print("Топ 10 самых часто встречающихся слов длиннее 6 символов:")
    for word, count in top_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()