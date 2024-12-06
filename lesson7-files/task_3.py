import os

def merge_files(file1, file2, output_file):
    # Список для хранения информации о файлах
    files_info = []

    # Чтение первого файла
    with open(file1, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        files_info.append((file1, len(lines), lines))

    # Чтение второго файла
    with open(file2, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        files_info.append((file2, len(lines), lines))

    # Сортировка файлов по количеству строк
    files_info.sort(key=lambda x: x[1])

    # Запись в результирующий файл
    with open(output_file, 'w', encoding='utf-8') as out_f:
        for file_name, line_count, lines in files_info:
            out_f.write(f"{file_name}\n")          # Имя файла
            out_f.write(f"{line_count}\n")         # Количество строк
            out_f.writelines(lines)                # Содержимое файла
            out_f.write("\n\n")                      # Между данными файлов

# Пример использования
merge_files("lesson7-files\\f1.txt", "lesson7-files\\f2.txt", "output.txt")