import datetime
import os
from cryptography.fernet import Fernet


def encryption_logging(func):
    def decorator(readfile, writefile, key):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"Operation: {func.__name__},\n" \
                        f"Read file: {readfile} -> write file: {writefile}, \n" \
                        f"Key: {key}, \n" \
                        f"Timestamp: {timestamp}\n"
        print(log_message)
        return func(readfile, writefile, key)
    return decorator


# Создание ключа шифрования
def write_key():
    if not os.path.exists('crypto.key'):
        encrypt_key = Fernet.generate_key()
        with open('crypto.key', 'wb') as key_file:
            key_file.write(encrypt_key)


# Загружаем ключ шифрования
def load_key():
    try:
        return open('crypto.key', 'rb').read()

    except FileNotFoundError:
        print("Файл ключа не найден.")

    except IOError:
        print("Ошибка при чтении файла ключа.")


@encryption_logging
# Шифрование файла и его запись
def encrypt(readfile, writefile, key):
    try:
        f = Fernet(key)

        with open(readfile, 'rb') as file:
            file_data = file.read()
            encrypted_data = f.encrypt(file_data)

        with open(writefile, 'wb') as file:
            file.write(encrypted_data)

    except FileNotFoundError:
        print("Файл для шифрования не найден.")

    except IOError:
        print("Ошибка при чтении/записи файлов.")


@encryption_logging
# Расшифровка файла и его запись
def decrypt(readfile, writefile, key):
    try:
        f = Fernet(key)

        with open(readfile, 'rb') as file:
            encrypted_data = file.read()

        decrypted_data = f.decrypt(encrypted_data)
        with open(writefile, 'wb') as file:
            file.write(decrypted_data)

    except FileNotFoundError:
        print("Файл для расшифровки не найден.")

    except IOError:
        print("Ошибка при чтении/записи файлов.")


# если ключ шифрования не создан, раскомментировать 'write_key' строку
write_key()

# загрузка ключа
encrypted_key = load_key()

# Чтение файла и запись данных в зашифрованный файл
read_file = '../analysis_summarize/textdata.txt'
write_encrypt_file = 'encrypt.txt'

read_encrytped_file = 'encrypt.txt'
decrypted_file = 'decrypt.txt'

# зашифровать файл
encrypt(read_file, write_encrypt_file, encrypted_key)
# расшифровать файл
decrypt(read_encrytped_file, decrypted_file, encrypted_key)
