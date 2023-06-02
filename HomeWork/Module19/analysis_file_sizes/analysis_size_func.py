import os
from pathlib import Path


def analysis_file_sizes(directory):
    total_size = 0  # Общий размер файлов
    path = Path(directory)
    if path.is_dir():
        for dirpath, dirname, filenames in os.walk(directory):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                if os.path.isfile(filepath):
                    total_size += os.path.getsize(filepath)

    units = ['Byte', 'Kb', 'Mb', 'Gb']
    unit_index = 0  # Индекс текущей единицы измерения
    while total_size >= 1024 and unit_index < len(units) - 1:  # Преобразуем размер в удобный формат
        total_size /= 1024
        unit_index += 1

    total_size = round(total_size, 3)

    return f'Общий объем всех файлов: {total_size} {units[unit_index]}'


print(analysis_file_sizes('C:/Users/lukja/PycharmProjects/coursePython216_Back/HomeWork/Module19'))
