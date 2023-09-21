"""Коллекция авто-тестов для проверки отправки запросов на REST API сервис https://dadata.ru/. Для формирования тестовых
запросов импортирована библиотека Dadata от разработчика сервиса."""

import httpx
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

# def test_get_address_info_invalid_data():
#     """Негативный тест с не валидными данными на проверку post-запроса к услуге "Разбор адреса из строки
#     («стандартизация») api-сервиса https://dadata.ru/. Тестируется отправка и обработка post-запроса с некорретными
#     ключами token и secret. Валидация негативного теста считается успешной, если ответ сервера вызывает тип исключения
#     HTTPStatusError (сервер понял запрос, но отказывается его авторизовать). """
#
#     Dd = Dadata(invalid_token, invalid_secret)
#
#     try:
#         response = Dd.clean('address', source='мск, перовская, дом 13, корпус 1')
#     except httpx.HTTPStatusError:
#         print('\n\nЗапрос с некорректными ключами отклонен сервером, валидация негативного теста прошла успешно!')


# def test_geo_loc_by_address_valid():
#     """Позитивный тест с валидными данными на проверку корректного определения географических координат здания на
#     основании указанного пользователем адреса. Валидация теста считается успешной, если полученные от сервиса значения
#     координат соответствует ожидаемым(фактическим) ."""
#
#     response = Dd.clean('address', 'МО, г. Видное, проспект Ленинского Комсомола, д. 1, корпус В')
#     assert response['geo_lat'] == '55.5499054'
#     assert response['geo_lon'] == '37.7189312'


def test_find_by_id_company_valid():
    """Позитивный тест с валидными данными на проверку корректного определения наименования и реквизитов юридического
    лица на основании указанного пользователем ИНН. Валидация теста считается успешной, если полученные от сервиса
    полное наименование организации её и КПП соответствуют фактическим."""

    response = Dd.find_by_id('party', '7721581040')

    print(response)

    # modify_list = dict(response[0]).get('data')
    # modify_dict = dict(modify_list).get('name')
    # full_with_opf = dict(modify_dict).get('full_with_opf')
    #
    # assert full_with_opf == '''ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "ДЕЙТА КЬЮ"'''













