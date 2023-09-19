import json
import requests
import os


class DadataAddress:
    """Класс AddressDadata с методами для отправки REST API-запросов к сервисному модулю "API: стандартизация адресов"
    на сайте https://dadata.ru/api/clean/address/. Класс использует стандартную библиотеку Python - requests."""

    def __init__(self):
        self.base_url = 'https://cleaner.dadata.ru/api/v1/clean/address'

    def get_address_standardization(self, token: str, secret: str, address: str = '') -> json:
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'token': token, 'secret': secret}
        response = requests.post(self.base_url, headers=headers, data=address)
        status = response.status_code
        result = response.json()

