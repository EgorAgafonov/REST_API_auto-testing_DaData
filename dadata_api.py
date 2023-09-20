import json
import requests
import os


class DadataAddress:
    """Класс AddressDadata с методами для отправки REST API-запросов к сервисному модулю "API: стандартизация адресов"
    на сайте https://dadata.ru/api/clean/address/. Класс использует стандартную библиотеку Python - requests."""

    def __init__(self, token: str, secret: str = None):
        self.base_url = 'https://cleaner.dadata.ru/api/v1/clean/address'
        self.token = token
        self.secret = secret

    def get_address_standartization(self, address: str) -> json:
        headers = {
            "Content-type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Token {self.token}",
            "X-Secret": f"{self.secret}"
             }
        data = [address]
        response = requests.post(self.base_url, headers=headers, data=data)
        status = response.status_code
        result = response.json()
        return status, result

