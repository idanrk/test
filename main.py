import os
import requests

API_KEY = os.getenv("API_KEY")


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class URL:
    def __init__(self, source, target):
        self.source = source
        self.target = target

    def form_url(self):
        return f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{self.source}"


@singleton
class CurrencyAPI:
    def __init__(self, url: URL):
        self.response = requests.get(url.form_url()).json()
        self.url = url

    def get_exchange_rate(self):
        return float(self.response["conversion_rates"][self.url.target])


@singleton
class File:
    def __init__(self, filename="file.txt"):
        with open(filename) as f:  # sys.argv[1]
            self.content = f.read()

    def get_content(self):
        return self.content


class Model:
    def __init__(self, filename, source, target):
        self.file = File(filename)
        self.url = URL(source, target)
        self.api_handler = CurrencyAPI(self.url)


class Controller:
    def __init__(self, model: Model):
        self.model = model

    def get_exchange(self):
        file_contents = self.model.file.get_content().split()
        rate = self.model.api_handler.get_exchange_rate()
        file_contents = map(lambda x: float(x) * rate, file_contents[2:])
        return print_currency(file_contents)

    def start(self):
        self.get_exchange()


def print_currency(values):
    for value in values:
        print(value)


if __name__ == '__main__':
    model = Model("file.txt", "USD", "ILS")
    c = Controller(model)
    c.start()
