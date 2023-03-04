from random import choice, randint
from functools import reduce
import string


# Task 1
# vowels_smb = (''.join(choice(string.ascii_lowercase) for i in range(30)))
# print(vowels_smb)
#
# remove_vowels = lambda find_vowels: find_vowels if find_vowels not in 'aeiouAEIOU' else ''
# print(''.join(map(remove_vowels, vowels_smb)))


# Task 2
# symbols1 = (''.join(choice(string.ascii_lowercase) for _ in range(30)))
# print(symbols1)
#
# symbols2 = (''.join(choice(string.digits) for _ in range(30)))
# print(symbols2)
#
# remove_vowels = lambda s: s.isalpha()
# print('Проверка строки только с буквами:', remove_vowels(symbols1))
# print('Проверка строки с цифрами:', remove_vowels(symbols2))


# Task 3
# nums = [randint(1, 50) for _ in range(int(input('Введите числа: ')))]
# print(nums)
#
# print(reduce(lambda x, y: x * y, nums))


# Task 4
# lst = ["IN GIRUM IMUS NOCTE - ET CONSUMIMUR IGNI", "роза", "казак", "дед", "шалаш", "мед",]
# is_palindrome = lambda x: x == x[::-1]
# palindromes_only = lambda arr: [x for x in arr if is_palindrome(''.join(filter(str.isalnum, x.lower())))]
#
# palindromes = palindromes_only(lst)
# print(palindromes)


# Task 5
# num = int(input('Введите число: '))
# is_prime = lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)) and x > 1
# print(is_prime(num))


# Task 6
# num = int(input('Введите число: '))
#
# factorial = lambda s: 1 if s == 0 else s * factorial(s - 1)
# print(factorial(num))
