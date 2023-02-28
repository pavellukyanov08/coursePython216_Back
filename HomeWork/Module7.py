from random import choice
import string

letters = string.ascii_lowercase
rand_string = ''.join(choice(letters) for i in range(30))

remove_vowels = lambda find_vowels: "".join([s for s in find_vowels if 'aeiouAEIOU' not in rand_string])

print(f'Random string of length {len(rand_string)} is: {rand_string}; \nString without vowel letter:'
      f' {remove_vowels(rand_string)}')

# letters = string.ascii_lowercase
# vowels = "aeiouAEIOU"
# remove_vowels = lambda s: "".join([c for c in s if c not in vowels])
# print(''.join(choice(letters) for i in range(30)))
# print(remove_vowels(''.join(choice(letters) for _ in range(30))))
