import os

#API_KEY = os.getenv("API_KEY")  # 588826d0ba6c3d4baa39a7dd
API_KEY = "588826d0ba6c3d4baa39a7dd"
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
