from random import choice
import string
from random import randint


# Task 1
# vowels_smb = (''.join(choice(string.ascii_lowercase) for i in range(30)))
# print(vowels_smb)

# remove_vowels = lambda find_vowels: find_vowels if find_vowels not in 'aeiouAEIOU' else ''
# print(''.join(map(remove_vowels, vowels_smb)))


# Task 2
# symbols = (''.join(choice(string.ascii_lowercase + string.digits + string.punctuation) for i in range(30)))
# print(symbols)
#
# remove_vowels = lambda find_vowels: find_vowels if find_vowels in \
#                                                    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' else ''
# print(''.join(map(remove_vowels, symbols)))


# Task 3
nums = [randint(1, 100) for _ in range(3)]

# multipli = lambda x, y: [x * y, nums]
print(list(map(lambda x, y: x * y, nums)))