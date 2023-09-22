import os
import time
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('token')
secret = os.getenv('secret')
invalid_token = os.getenv('invalid_token')
invalid_secret = os.getenv('invalid_secret')
user_balance = float(os.getenv('user_balance'))


def duration_time_of_test(func):
    """Функция-декоратор для определения длительности авто-теста с момента запуска\до момента его окончания."""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"\nНачало выполнения теста: {round(start_time,3)}")

        func(*args, **kwargs)

        end_time = time.time()
        print(f"\nОкончание выполнения теста: {round(end_time,3)}")
        result = time.time() - start_time
        print(f"\nОбщая продолжительность выполнения теста: {round(result,3)})")

    return wrapper
