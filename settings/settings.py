import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('token')
secret = os.getenv('secret')
invalid_token = os.getenv('invalid_token')
invalid_secret = os.getenv('invalid_secret')
