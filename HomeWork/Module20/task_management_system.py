class User:
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

    @staticmethod
    def create_account(name, email, role):
        new_user = User(name, email, role)
        return new_user

    def update_userdata(self, name, email, role):
        if name:
            self.name = name
        elif email:
            self.email = email
        elif role:
            self.role = role

    def view_assigned_tasks(self, task_manager):
        # for task in task_manager.tasks:
        #     if task.is_assignee == self:
        #         print(f'Задача: {task.task_name}\n Назначена: {task.is_assignee.name}')
        #         print()
        assigned_tasks = [task for task in task_manager.tasks if task.is_assignee == self]
        if assigned_tasks:
            for task in assigned_tasks:
                print(f'Задача: {task.task_name}\n Назначена: {task.is_assignee.name}')
            print()


class TaskManager:
    def __init__(self, task_name):
        self.task_name = task_name
        self.tasks = []
        self.is_completed = False
        self.is_assignee = None

    def adding_tasks(self, task):
        self.tasks.append(task)

    def assigning_tasks(self, user, task):
        if task in self.tasks:
            self.is_assignee = user

    def mark_task_completed(self, task):
        if task in self.tasks:
            self.is_completed = True

    def display_tasks(self):
        for task in self.tasks:
            print(f"Задача: {task.task_name}")
            if task.is_completed:
                print("Статус: выполнена")
            else:
                print("Статус: ожидает выполнения")
            # if task.is_assignee:
            #     print(f"Назначена пользователю: {task.is_assignee.name}")
            print()


# Создание задач
task1 = TaskManager('Сходить на прогулку')
task2 = TaskManager('Сделать уборку')

admin = User("Sam", "admin@gmail.com", "Администратор")
user1 = User("Alex", "john@gmail.com", "Пользователь")

# Добавление задач в TaskManager
task1.adding_tasks(task1)
task2.adding_tasks(task2)

# Назначение задач пользователям
task1.assigning_tasks(user1, task1)
task2.assigning_tasks(admin, task2)

# Пометка задачи как выполненной
task1.mark_task_completed(task1)

# Отображение информации о задачах
task1.display_tasks()
task2.display_tasks()

# Просмотр назначенных задач для пользователя
user1.view_assigned_tasks(task1)
admin.view_assigned_tasks(task2)
