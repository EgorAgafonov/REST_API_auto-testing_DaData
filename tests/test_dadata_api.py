"""Коллекция авто-тестов для проверки отправки запросов на REST API сервис https://dadata.ru/. Для формирования тестовых
запросов импортирована библиотека от разработчика сервиса - Dadata."""

from dadata import Dadata
import pytest
import requests
import json
from settings.settings import *

Dd = Dadata(token, secret)


def test_get_address_info_valid_data():
    """Позитивный тест с валидными данными на проверку post-запроса к услуге "Разбор адреса из строки («стандартизация»)
    api-сервиса https://dadata.ru/. Тестируется корректная обработка введенного пользователем адреса, намеренно
    содержащего ошибки и сокращения """

    response = Dd.clean('address', source='мск, металургов, дом 58,')
    assert response['region_with_type'] == 'г Москва'
    assert response['street'] == 'Металлургов'
    assert response['house'] == '58'
    assert response['house_type'] == 'д'
    assert response['postal_code'] == '111399'


