# cache = {}
#
#
# def fibonacci(n):
#     sequence = []
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#
#     if n in cache:
#         return cache[n]
#
#     cache[n] = (fibonacci(n - 1) + fibonacci(n - 2))
#
#     for i in range(0, n + 1):
#         sequence.append(fibonacci(i))
#     return sequence
#
#
# print(fibonacci(10))


def find_anagrams(lst):
    anagrams = []
    word_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word))
        if sorted_word in word_dict:
            word_dict[sorted_word].append(word)
        else:
            word_dict[sorted_word] = [word]

    for key, value in word_dict.items():
        if len(value) > 1:
            anagrams.append(tuple(value))
    return anagrams


print(find_anagrams(['cat', 'dog', 'tac', 'god', 'act', 'good']))


# def compress_file(filename):
#     with open(filename, 'r', encoding='utf-8') as f:
#         line = f.read()
#
#     dict_syblom = {}
#     for i in line:
#         if i in dict_syblom:
#             dict_syblom[i] += 1
#         else:
#             dict_syblom[i] = 1
#
#     new_file = filename[:-4] + '_compress.txt'
#     with open(new_file, 'w', encoding='utf-8') as f:
#         new_file = ''
#         for k, v in dict_syblom.items():
#             new_file = new_file + k + str(v)
#         f.write(new_file)


def file_read_write(file_read=None, file_write=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if file_read is not None:
                open_file = open(file_read, 'r', encoding='utf-8')

            if file_write is not None:
                open_file_white = open(file_read, 'w', encoding='utf-8')

            result = func(open_file, open_file_white, *args, **kwargs)
            if open_file is not None:
                open_file.close()

            if open_file_white is not None:
                open_file_white.close()

            return result
        return wrapper
    return decorator



