"""Коллекция авто-тестов для проверки отправки запросов на REST API сервис https://dadata.ru/. Для отправки тестовых
запросов импортирована готовая API библиотека Dadata от разработчика сервиса."""

from dadata import Dadata
from settings.settings import *
import pytest
import httpx
import json

Dd = Dadata(token, secret)


@duration_time_of_test
def test_get_address_info_valid_data():
    """Позитивный тест с валидными данными на проверку post-запроса к услуге "Разбор адреса из строки («стандартизация»)
    api-сервиса https://dadata.ru/. Тестируется корректная обработка и разбор введенного пользователем адреса,
    намеренно содержащего ошибки и сокращения."""

    response = Dd.clean('address', source='Спб, Олеко Дундича, дом 2,')

    assert response['region_with_type'] == 'г Санкт-Петербург'
    assert response['street'] == 'Олеко Дундича'
    assert response['house'] == '2'
    assert response['house_type'] == 'д'


@duration_time_of_test
def test_get_address_info_invalid_data():
    """Негативный тест проверки post-запроса к услуге "Разбор адреса из строки («стандартизация») api-сервиса
    https://dadata.ru/. Тестируется отправка и обработка post-запроса с некорректными ключами token и secret.
    Валидация негативного теста считается успешной, если ответ сервера вызывает тип исключения
    HTTPStatusError (сервер понял запрос, но отказывается его авторизовать)."""

    Dd = Dadata(invalid_token, invalid_secret)

    try:
        response = Dd.clean('address', source='мск, перовская, дом 13, корпус 1')
    except httpx.HTTPStatusError:
        print('\n\nЗапрос с некорректными ключами отклонен сервером, валидация негативного теста прошла успешно!')
    else:
        assert response != {}
        print(f"\nОшибка! Сервер принял запрос с некорректными ключами и сформировал ответ. Создать баг-репорт и "
              f"отразить ошибку в системе отслеживания.")


@duration_time_of_test
def test_geo_loc_by_address_valid():
    """Позитивный тест с валидными данными на проверку корректного определения географических координат здания на
    основании указанного пользователем адреса. Валидация теста считается успешной, если полученные от сервиса значения
    координат соответствует ожидаемым(фактическим)."""

    response = Dd.clean('address', 'Москва, ул. Тюрина, д. 1, строение 3')

    # получим координаты из ответа и округлим до 4 знаков после запятой:
    response_lat = round(float(response['geo_lat']), 4)
    response_lon = round(float(response['geo_lon']), 4)

    assert response_lat == 55.6195
    assert response_lon == 37.6735


@duration_time_of_test
def test_find_by_id_company_valid():
    """Позитивный тест с валидными данными на проверку корректного определения наименования и реквизитов юридического
    лица на основании указанного пользователем ИНН. Валидация теста считается успешной, если полученные от сервиса
    полное наименование организации её и КПП соответствуют фактическим."""

    response = Dd.find_by_id('party', '7721581040')  # получаем список с одним элементом - словарем, включающим в себя
    # другие словари.

    block_of_data = response[0].get('data')  # для получения данных о коде причине постановки (КПП) организации в
    # полученном массиве данных сначала обращаемся к элементу списка(словарь), а затем обращаемся к значению ключа
    # 'data', также являющееся словарем и содержащее, помимо прочего, сведения о КПП.

    block_of_name = block_of_data['name']  # для получения данных о полном наименовании организации(ПНО) с
    # организационно-правовой формой (ОПФ), в словаре block_of_data обращаемся к значению ключа 'name'(тоже словарь),
    # также являющееся словарем и содержащее, помимо прочего, сведения о ПНО с ОПФ.

    assert block_of_data['kpp'] == '770401001'  # получаем значение ключа 'kpp' и сравниваем его с ожидаемым(верным)
    assert block_of_name['full_with_opf'] == '''ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "ДЕЙТА КЬЮ"'''


@duration_time_of_test
def test_find_by_id_company_invalid():
    """Негативный тест с валидными данными ключа, но некорректным ИНН юридического лица в заголовке. Валидация
    негативного теста считается успешной, если ответ сервера содержит информацию об отсутствии организации с
    указанным ИНН в БД и/или список ответа пустой"""

    inn_org = '12345678'
    response = Dd.find_by_id('party', inn_org)

    assert response == []


@duration_time_of_test
def test_get_user_balance_valid():
    """Позитивный тест проверки запроса получения баланса пользователя api-сервиса https://dadata.ru/. Валидация
    теста считается успешной, если ответ сервера содержит корректные данные о фактическом балансе пользователя на
    момент тестирования."""

    response = Dd.get_balance()

    assert response == user_balance  # полученное от сервера значение баланса пользователя сравнивается с
    # фактическим значением в переменной user_balance.


@pytest.mark.skip(reason='Тест генерирует 30 платных запросов, запускать в комплекте по необходимости.')
@duration_time_of_test
def test_requests_stress_testing(requests_quantity=30):
    """Тест работы api-сервиса DaData под нагрузкой. С помощью декоратора @duration_time_of_test проверятся скорость
    обработки запросов сервером по пяти различным эндпоинтам и методам."""

    for i in range(requests_quantity):
        response_address = Dd.clean('address', source='мск, Петровско-Разумовская аллея, д. 6')
        response_balance = Dd.get_balance()
        response_fms_unit = Dd.suggest("fms_unit", "500-064")
        response_ip_address = Dd.iplocate('5.199.192.0')
        response_geolocate = Dd.geolocate(name='address', lat=56.8376, lon=60.5989)

        assert response_address['result'] == 'г Москва, аллея Петровско-Разумовская, д 6'
        assert response_balance == user_balance
        assert response_fms_unit[1].get('value') == ('ТП В Г. МОСКОВСКИЙ ОУФМС РОССИИ ПО МОСКОВСКОЙ ОБЛ. В ЛЕНИНСКОМ '
                                                     'РАЙОНЕ')
        assert response_ip_address['value'] == 'Свердловская обл, г Кировград'
        assert response_geolocate[0].get('unrestricted_value') == ("620014, Свердловская обл, г Екатеринбург, пр-кт "
                                                                   "Ленина, д 26")
