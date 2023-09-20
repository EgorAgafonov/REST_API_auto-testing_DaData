"""Коллекция авто-тестов для проверки отправки запросов на REST API сервис https://dadata.ru/. Для формирования тестовых
запросов импортирована библиотека от разработчика сервиса - Dadata."""

from dadata import Dadata
import pytest
import requests
import json
from settings.settings import token, secret

Dd = Dadata(token, secret)


def get_address_info_valid_data():
    response = Dd.clean('address', source='МО, г. Видное, Проспект Ленинского Комсомола, д. 2')
    print(type(response))


