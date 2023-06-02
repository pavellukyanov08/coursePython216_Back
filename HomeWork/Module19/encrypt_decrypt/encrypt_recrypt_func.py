import datetime
from cryptography.fernet import Fernet


def encryption_logging(filename, key):
    def decorator(func):
        def wrapper(*args, **kwargs):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"Operation: {func.__name__}, File: {filename}, Key: {key}, Timestamp: {timestamp}"
            return log_message
        return wrapper(filename, key)
    return decorator


# Создание ключа шифрования
def write_key():
    encrypt_key = Fernet.generate_key()
    with open('crypto.key', 'wb') as key_file:
        key_file.write(encrypt_key)


# Загружаем ключ шифрования
def load_key():
    return open('crypto.key', 'rb').read()


# Шифрование файла и его запись
def encrypt(readfile, writefile, key):
    f = Fernet(key)

    with open(readfile, 'rb') as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)

    with open(writefile, 'wb') as file:
        file.write(encrypted_data)


# Расшифровка файла и его запись
def decrypt(readfile, writefile, key):
    f = Fernet(key)

    with open(readfile, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)
    with open(writefile, 'wb') as file:
        file.write(decrypted_data)


# если ключ шифрования не создан, раскомментировать 'write_key' строку
# write_key()

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
