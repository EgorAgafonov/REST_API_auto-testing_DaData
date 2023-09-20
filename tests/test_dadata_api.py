"""Коллекция авто-тестов для проверки отправки запросов на REST API сервис https://dadata.ru/. Для формирования тестовых
запросов импортирована библиотека от разработчика сервиса - Dadata."""

from dadata import Dadata
import pytest
import requests
import json
from settings.settings import token, secret

Dd = Dadata(token, secret)


def test_get_address_info_valid_data():
    """Позитивный тест с валидными данными на проверку post-запроса к услуге "Разбор адреса из строки («стандартизация»)
    api-сервиса https://dadata.ru/.  """
    response = Dd.clean('address', source='МО, г. Видное, ул. Проспект Ленинского Комсомола, д. 2, корпус 4, кв. 83')
    print(f" Адрес:{response['result']}\n Широта: {response['geo_lat']}', Долгота:{response['geo_lon']}'")


