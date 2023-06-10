class TaskManager:
    def __init__(self):
        self.__tasks = ['Добавить пользователя', 'Прогуляться', 'Сходить в магазин']
        # self.__users = {'1': {'name': 'Sam', 'email': 'sam@gmail.com', 'role': 'Админ',
        #                       'Tasks': ['Добавить пользователя']},
        #                 '2': {'name': 'John', 'email': 'john@gmail.com', 'role': 'Пользователь',
        #                       'Tasks': ['Прогуляться']},
        #                 '3': {'name': 'Michael', 'email': 'michael@gmail.com', 'role': 'Пользователь',
        #                       'Tasks': []}}
        self.__users = {'John': {'email': 'john@gmail.com', 'role': 'Админ', 'Tasks': ['Добавить пользователя']},
                        'Sam': {'email': 'john@gmail.com', 'role': 'Пользователь', 'Tasks': ['Прогуляться']},
                        'Michael': {'email': 'michael@gmail.com', 'role': 'Пользователь', 'Tasks': []}
                        }
        self.is_completed = False

    def show_users(self):
        return self.__users

    def show_tasks(self):
        return self.__tasks

    def getting_user_id(self, user_id):
        return self.__users.get(user_id)

    def adding_tasks(self, task):
        self.__tasks.append(task)
        print(f'Задача успешно добавлена!\nТекущие задачи: {self.__tasks}')
        print()

    def assigning_tasks(self, user, task):
        user = self.getting_user_id(user)
        if user is not None:
            if 'task' in user:
                user['Tasks'].append(task)
            else:
                user['Tasks'] = task

            print(f'Задача "{task}" присвоена пользователю: {user}')
        else:
            print('Пользователь не найден')
        print()

    def mark_task_completed(self, task):
        if task in self.__tasks:
            self.is_completed = True

    def print_tasks(self):
        if self.__tasks:
            for task in enumerate(self.__tasks, 1):
                print(f"Задача: {task}")
                if self.is_completed:
                    print(f"Статус: выполнена")
                else:
                    print("Статус: ожидает выполнения")
                print()
        else:
            print('Список задач пуст!')
            print()


class User:
    def __init__(self):
        self.__name = ''
        self.__email = ''
        self.__role = ''
        self.task_mng = TaskManager()

    def create_account(self, new_id, new_name, new_email, new_role):
        # if self.task_mng.getting_user_id(new_id) is None:
        #     new_user = User(new_name, new_email, new_role)
        if self.task_mng.getting_user_id(new_id) is None:
            new_user = {'name': new_name, 'email': new_email, 'role': new_role, 'tasks': []}
            self.task_mng.show_users()[new_id] = new_user
            print('Пользователь добавлен!')
        else:
            print('Пользователь уже существует')

    def update_userdata(self, name, email, role):
        if name:
            self.__name = name
        elif email:
            self.__email = email
        elif role:
            self.__role = role

    def print_assigned_tasks(self, user_id):
        user = self.task_mng.getting_user_id(user_id)
        if user is not None:
            assigned_tasks = user.get('Tasks')
            if assigned_tasks:
                print('Назначенные задачи: ')
                for i, task in enumerate(assigned_tasks, 1):
                    print(f'{i}. {user_id} -> {task}')
            else:
                print('Для пользователя нет задач.')
        else:
            print('Пользователь не найден.')


# Создание задач
tm = TaskManager()

user1 = User()
user2 = User()

# Добавление задач в TaskManager
tm.adding_tasks('Написать программу')

# Назначение задач пользователям
tm.assigning_tasks('Michael', 'Сходить в магазин')
# tm.assigning_tasks(user1, tm)

# Пометка задачи как выполненной
tm.mark_task_completed('Добавить пользователя')

# Отображение информации о задачах
tm.print_tasks()

# Просмотр назначенных задач для пользователя
user1.print_assigned_tasks('Sam')
user2.print_assigned_tasks('John')
