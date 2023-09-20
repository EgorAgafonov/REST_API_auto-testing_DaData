"""Коллекция авто-тестов для проверки отправки запросов на REST API сервис https://dadata.ru/. Для формирования тестовых
запросов импортирована библиотека от разработчика сервиса - Dadata."""
import requests
from dadata import Dadata
import pytest
from requests import *
import json
import http_api_exception
from settings.settings import *

Dd = Dadata(token, secret)


# def test_get_address_info_valid_data():
#     """Позитивный тест с валидными данными на проверку post-запроса к услуге "Разбор адреса из строки («стандартизация»)
#     api-сервиса https://dadata.ru/. Тестируется корректная обработка и разбор введенного пользователем адреса,
#     намеренно содержащего ошибки и сокращения."""
#
#     response = Dd.clean('address', source='мск, металургов, дом 58,')
#     assert response['region_with_type'] == 'г Москва'
#     assert response['street'] == 'Металлургов'
#     assert response['house'] == '58'
#     assert response['house_type'] == 'д'
#     assert response['postal_code'] == '111399'

def test_get_address_info_invalid_data():
    """Негативный тест с не валидными данными на проверку post-запроса к услуге "Разбор адреса из строки
    («стандартизация») api-сервиса https://dadata.ru/. Тестируется отправка и обработка post-запроса с некорретными
    ключами token и secret. """

    Dd = Dadata(invalid_token, invalid_secret)

    try:
        response = Dd.clean('address', source='мск, перовская, дом 13, корпус 1')
    except http_api_exception.HTTPStatus:
        print('Ошибка! Проверьте корректность ключей пользователя для отправки запроса!')








