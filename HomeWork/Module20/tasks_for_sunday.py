# Task 1
# from abc import ABC, abstractmethod
#
#
# class SocialMediaAccount(ABC):
#     @abstractmethod
#     def post(self, content):
#         pass
#
#
# class FacebookAccount(SocialMediaAccount):
#     def post(self, content):
#         print(f'Публикация в Facebook: {content}')
#
#
# class InstagramAccount(SocialMediaAccount):
#     def post(self, content):
#         print(f'Публикация в Instagram: {content}')
#
#
# class TwitterAccount(SocialMediaAccount):
#     def post(self, content):
#         print(f'Публикация в Twitter: {content}')
#
#
# class SocialMediaAccountFactory(ABC):
#     @abstractmethod
#     def create_account(self):
#         pass
#
#
# class FacebookAccountFactory(SocialMediaAccountFactory):
#     def create_account(self):
#         return FacebookAccount()
#
#
# class InstagramAccountFactory(SocialMediaAccountFactory):
#     def create_account(self):
#         return InstagramAccount()
#
#
# class TwitterAccountFactory(SocialMediaAccountFactory):
#     def create_account(self):
#         return TwitterAccount()
#
#
# factory = FacebookAccountFactory()
# account = factory.create_account()
# account.post("Привет, Facebook!")
#
# factory = InstagramAccountFactory()
# account = factory.create_account()
# account.post("Привет, Instagram!")
#
# factory = TwitterAccountFactory()
# account = factory.create_account()
# account.post("Привет, Twitter!\n")
#
#
# class ProxySocialMediaAccount(SocialMediaAccount):
#     def __init__(self, verified_account):
#         self.verified_account = verified_account
#
#     def post(self, content):
#         if self.content_verification(content):
#             self.verified_account.post(content)
#         else:
#             print('Публикация отклонена! -> Запрещенный контент')
#
#     @staticmethod
#     def content_verification(content):
#         forbidden_words = ['спам', 'война', 'расизм', 'вирус', 'насилие']
#         for word in forbidden_words:
#             if word in content.lower():
#                 return f'#модерация {content}'
#             else:
#                 return 'Отказ. Запрещенный контент!'
#
#
# instagram_account = InstagramAccount()
# proxy_account = ProxySocialMediaAccount(instagram_account)
# proxy_account.post("Это публикация содержит спам")


# Task 2
# class File:
#     def __init__(self, filename):
#         self.filename = filename
#
#     def read(self):
#         with open(self.filename, 'r', encoding='utf-8') as f:
#             return f.read()
#
#     def write(self, text):
#         with open(self.filename, 'w', encoding='utf-8') as f:
#             return f.write(text)
#
#     def append(self, text):
#         with open(self.filename, 'a', encoding='utf-8') as f:
#             return f.write(text)
#
#
# class FileProxy(File):
#     def __init__(self, filename, role=None):
#         super().__init__(filename)
#         self.read_attempt = 0
#         self.cache = []
#         self.access_log = []
#         self.role = role
#
#     def register_access(self, read):
#         self.access_log.append(read)
#
#     def checking_access(self, read):
#         if self.role is None:
#             print(f'Доступ запрещен. Роль не найдена')
#         elif self.role == 'admin':
#             print('Доступ разрешен')
#         else:
#             print('Доступ запрещен. У вас нет разрешения на выполнение операций')
#
#     def read(self):
#         self.read_attempt += 1
#         self.register_access("read")
#
#         if self.checking_access("read"):
#             if self.cache:
#                 print(f"Извлечение содержимого из кеша...\n {self.cache}")
#                 return self.cache
#             data = super().read()
#             self.cache.append(data)
#             return data
#
#     def write(self, text):
#         self.register_access("write")
#         if self.checking_access("write"):
#             data = File(self.filename)
#             super().write(data)
#
#     def append(self, text):
#         self.register_access("append")
#         if self.checking_access("append"):
#             data = File(self.filename)
#             super().append(data)
#
#     def count_read_attempt(self):
#         return self.read_attempt
#
#
# proxy_file1 = FileProxy('fileproxy.txt', 'admin')
#
# content = proxy_file1.read()
# print(content)
#
# proxy_file1.write('Проверка записи в файл')
#
#
# proxy_file2 = FileProxy('fileproxy.txt', 'user')
#
# content = proxy_file2.read()
# print(content)
#
# proxy_file2.write('Проверка записи в файл')
#
# read_attempt = proxy_file2.count_read_attempt()
# print(read_attempt)


class Command:
    def execute(self):
        pass

    def cancel(self):
        pass


class PowerOnCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.power_on()

    def cancel(self):
        self.device.power_off()


class PowerOffCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.power_off()

    def cancel(self):
        self.device.power_on()


class VolumeUpCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.volume_up()

    def cancel(self):
        self.device.volume_down()


class VolumeDownCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.volume_down()

    def cancel(self):
        self.device.volume_up()


class RemoteControl:
    def __init__(self):
        self.commands = {}

    def set_command(self, button, command):
        self.commands[button] = command

    def press_button(self, button):
        if button in self.commands:
            command = self.commands[button]
            command.execute()


class Television:
    def __init__(self):
        self.power = False
        self.volume = 0

    def power_on(self):
        self.power = True
        print("Телевизор включен")

    def power_off(self):
        self.power = False
        print("Телевизор выключен")

    def volume_up(self):
        if self.power:
            self.volume += 1
            print(f"Уровень громкости: {self.volume}")

    def volume_down(self):
        if self.power and self.volume > 0:
            self.volume -= 1
            print(f"Уровень громкости: {self.volume}")


tv = Television()

remote_control = RemoteControl()

power_on_command = PowerOnCommand(tv)
volume_up_command = VolumeUpCommand(tv)

remote_control.set_command(0, power_on_command)
remote_control.set_command(1, volume_up_command)

remote_control.press_button(0)
remote_control.press_button(1)
remote_control.press_button(1)
