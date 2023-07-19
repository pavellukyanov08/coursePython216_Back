def save_to_file(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result:
            with open('log_data.txt', 'w', encoding='utf-8') as res:
                for row in result:
                    print(row, file=res)
            print('Данные сохранены!')
            return result
        else:
            print('Ошибка! Данные не сохранены.')
    return wrapper