# Task1
from abc import ABC, abstractmethod


class SocialMediaAccount(ABC):
    @abstractmethod
    def post(self, content):
        pass


class ProxySocialMediaAccount(SocialMediaAccount):
    def __init__(self, verified_account):
        self.verified_account = verified_account

    def post(self, content):
        moderated_content = self.moderate_post(content)
        self.verified_account.post(moderated_content)

    @staticmethod
    def moderate_post(content):
        return f'#модерация {content}'


class FacebookAccount(SocialMediaAccount):
    def post(self, content):
        print(f'Публикация в Facebook: "{content}"')


class InstagramAccount(SocialMediaAccount):
    def post(self, content):
        print(f'Публикация в Instagram: "{content}"')


class TwitterAccount(SocialMediaAccount):
    def post(self, content):
        print(f'Публикация в Twitter: "{content}"\n')


class SocialMediaAccountFactory:
    def __init__(self):
        self.social_medias = SocialMediaAccount.__subclasses__()

    def create_account(self, media):
        for social_media in self.social_medias:
            if media.lower() in social_media.__name__.lower():
                return social_media()
    # @abstractmethod
    # def create_account(self):
    #     pass


class FacebookAccountFactory(SocialMediaAccountFactory):
    def create_account(self):
        return FacebookAccount()


class InstagramAccountFactory(SocialMediaAccountFactory):
    def create_account(self):
        return InstagramAccount()


class TwitterAccountFactory(SocialMediaAccountFactory):
    def create_account(self):
        return TwitterAccount()


factory = FacebookAccountFactory()
account = factory.create_account()
account.post("Привет, Facebook!")

factory = InstagramAccountFactory()
account = factory.create_account()
account.post("Привет, Instagram!")

factory = TwitterAccountFactory()
account = factory.create_account()
account.post("Привет, Twitter!")


facebook_account = FacebookAccount()
proxy_account = ProxySocialMediaAccount(facebook_account)
proxy_account.post("Привет, Facebook!")

instagram_account = InstagramAccount()
proxy_account = ProxySocialMediaAccount(instagram_account)
proxy_account.post("Привет, Instagram!")

twitter_account = TwitterAccount()
proxy_account = ProxySocialMediaAccount(twitter_account)
proxy_account.post("Привет, Twitter!")
