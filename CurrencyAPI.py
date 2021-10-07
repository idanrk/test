from URL import *
import requests


@singleton
class CurrencyAPI:
    def __init__(self, url: URL):
        self.response = requests.get(url.form_url()).json()
        self.url = url

    def get_exchange_rate(self):
        return float(self.response["conversion_rates"][self.url.target])
