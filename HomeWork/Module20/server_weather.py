import socket
import threading
import json

with open('weather.json', 'r', encoding='utf-8') as f:
    text = f.readlines()

database = {}

for string in text:
    data = json.loads(string)
    database[f"{data['city']['country']}, {data['city']['name']}"] = data

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 4321

server_socket.bind((host, port))
print(f'Сервер запущен по адресу {host}, порту {port}')

server_socket.listen(5)

welcome_message = 'Добро пожаловать! Вы подключены к серверу о погоде. \n' \
                  'Введите сообщение в виде "Страна, Город": '


def handle_client(client_socket, client_address):
    print(f'Подключился клиент: {client_address}')
    client_socket.send(welcome_message.encode())

    while True:
        client_message = client_socket.recv(1024).decode()

        if not client_message:
            print('Клиент отключился: ', client_address)
            break

        words = client_message.split(',')
        words = list(map(str.strip, words))
        words[0], words[1] = words[0].upper(), words[1][0].upper() + words[1][1:]
        query = ', '.join(words)
        answer = database.get(query, 'Такой город не найден')

        client_socket.send(answer.encode())

    client_socket.close()


while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
