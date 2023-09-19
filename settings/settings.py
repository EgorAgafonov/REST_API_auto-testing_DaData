import os
from dotenv import load_dotenv

load_dotenv()
valid_key = os.getenv('valid_key')
secret_key = os.getenv('secret_key')
