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
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Начало выполнения теста: {start_time}")

        func(*args, **kwargs)

        end_time = time.time()
        print(f"Окончание выполнения теста: {end_time}")
        result = time.time() - start_time
        print(f"Общая продолжительность выполнения теста: {result}")

    return wrapper
