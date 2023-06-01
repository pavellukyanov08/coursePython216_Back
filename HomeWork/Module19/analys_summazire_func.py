from collections import Counter


def analysis_and_summarize_file(filename):
    with open(filename, 'r') as file:
        content = file.read().lower()
    total_length, word_count, counter = 0, 0, 0
    word_counts = Counter()
    word_freq = {}

    lines = content.split('\n')
    # Вычисляем количество строк
    num_lines = len(lines)

    # Разделяем текст на слова
    words = content.split()
    # Вычисляем количество слов
    num_words = len(words)

    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    total_word_length = sum(len(word) for word in content)
    avg_word_length = total_word_length / num_words

    report = f'Анализ файла: {filename}\n'
    report += f'Кол-во строк в файле: {num_lines}\n'
    report += f'Кол-во слов в файле: {num_words}\n'
    report += f'Количество строк: {num_lines}\n'
    report += f'Количество слов: {num_words}\n'
    report += f'Средняя длина слова: {avg_word_length:.3f}\n\n'
    report += 'Частота слов:\n'

    for word, freq in word_freq.items():
        report += f'{word}: {freq}\n'

    with open('report.txt', 'w', encoding='utf-8') as report_file:
        report_file.write(report)


analysis_and_summarize_file('textdata.txt')
