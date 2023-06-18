import socket
import threading
import requests

api_key = 'da31b15b6201146d9653f4d84c096e82'
url_base = 'https://api.openweathermap.org/data/2.5/'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 1010

server_socket.bind((host, port))
print(f'Сервер запущен по адресу {host}, порту {port}')

server_socket.listen(5)

welcome_message = 'Добро пожаловать! Вы подключены к серверу о погоде.\n'


def handle_client(client_socket, client_address):
    print(f'Подключился клиент: {client_address}')
    client_socket.send(welcome_message.encode())

    while True:
        client_message = client_socket.recv(1024).decode()

        if not client_message:
            print('Клиент отключился: ', client_address)
            break

        def weather_forecast(q: str = 'Barnaul, RU', appid: str = api_key, units: str = 'metric'):
            response = requests.get(url_base + 'forecast', params={'q': q, 'appid': appid, 'units': units}).json()

            week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            if response["cod"] == '404':
                print("Город не найден.")
            else:
                weather_info = ''
                for i in range(7):
                    day = response['list'][i]
                    date = day['dt_txt']
                    weather = day['weather'][0]['description']
                    avg_temp = round((day['main']['temp_max'] + day['main']['temp_min']) / 2)
                    temp = day['main']['temp']
                    max_temp = day['main']['temp_max']
                    min_temp = day['main']['temp_min']
                    humidity = day["main"]["humidity"]
                    wind_speed = day["wind"]["speed"]
                    weather_info += f'Date: {date}\n' \
                                    f'\nWay of the week: {week_days[i]}\n' \
                                    f'Description: {weather}\n' \
                                    f'Max temp: {max_temp}\n' \
                                    f'Min temp: {min_temp}\n' \
                                    f'Average temperature: {avg_temp}\n' \
                                    f'Humidity %: {humidity}\n' \
                                    f'Speed of wind (m/s): {wind_speed}\n' \
                                    f'==========================================\n'
                client_socket.send(weather_info.encode())

        weather_forecast(client_message.strip())
    client_socket.close()


while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
