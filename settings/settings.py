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
        print(f"\n\nНачало выполнения теста: {time.asctime()}")

        func(*args, **kwargs)

        end_time = time.time()
        print(f"Окончание выполнения теста: {time.asctime()}")
        result = end_time - start_time
        print(f"Общая продолжительность выполнения теста: {round(result,3)} сек.")

    return wrapper


x = {"a": 1, "b": 2}
y = {"b": 3, "c": 4}
z = {**x, **y}
print(z)
