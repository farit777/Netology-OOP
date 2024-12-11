import xml.etree.ElementTree as ET
from collections import Counter
import re

# Функция для извлечения текста из XML
def extract_text_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    texts = []
    
    # Предполагаем, что текст новостей находится в тегах <description> или <title>
    for item in root.findall('.//item'):
        title = item.find('title')
        description = item.find('description')
        if title is not None:
            texts.append(title.text)
        if description is not None:
            texts.append(description.text)
    
    return ' '.join(texts)

# Функция для подсчета слов
def count_words(text):
    # Используем регулярное выражение для разделения текста на слова
    words = re.findall(r'\b\w{7,}\b', text.lower())  # Слова длиной 7 и более символов
    return Counter(words)

# Основная функция
def main():
    file_path = 'Lesson8-formats/newsafr.xml'  # Относительный путь к файлу
    text = extract_text_from_xml(file_path)
    word_count = count_words(text)
    
    # Получаем 10 самых распространенных слов
    top_10_words = word_count.most_common(10)
    
    print("Топ 10 самых часто встречающихся слов (длиннее 6 символов):")
    for word, count in top_10_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()