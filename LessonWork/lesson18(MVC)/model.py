import json


class Article:
    def __init__(self, title, author, symbols, publisher, annotation):
        self.title = title
        self.author = author
        self.symbols = symbols
        self.publisher = publisher
        self.annotation = annotation

    def __str__(self):
        return f'{self.title} - {self.author}'


class DecodeError(Exception):
    pass


class Model:
    def __init__(self):
        self.filepath = 'db.text'
        self.__articles = {}
        try:
            self.data = json.load(open(self.filepath, 'r', encoding='utf-8'))
            for article in self.data.values():
                self.__articles[f'{article["title"]} {article["author"]}'] = Article(*article.values())
        except json.JSONDecodeError:
            raise DecodeError
        except FileNotFoundError:
            with open(self.filepath, 'w') as f:
                f.write('{}')

    @property
    def articles(self):
        return self.__articles

    def add_new_article(self, article_data):
        new_article = Article(*article_data.values())
        self.__articles[f'{new_article.title} {new_article.author}'] = new_article
        dict_article = {art.title: art.__dict__ for art in self.__articles.values()}
        json.dump(dict_article, open(self.filepath, 'w', encoding='utf-8'))

    def find_articles(self, criteria):
        articles = []
        for article in self.__articles.values():
            for crit in criteria:
                if article in articles:
                    break
                for prop in article.__dict__.values():
                    if crit.lower() in prop.lower():
                        articles.append(article)
                        break
        return articles

    def delete_article(self, articles):
        if len(articles) == 0:
            return 'Такой статьи не было найдено'
        elif len(articles) == 1:
            article = articles[0]
            key = f'{article.title} {article.author}'
            self.__articles.pop(key)
            return 'Статья была удалена'
        else:
            return 'Слишком много статей'
