from settings.settings import *
import pytest
import requests
from requests_toolbelt import MultipartEncoder
import httpx
import json


class DadataAPI:

    def __init__(self):
        self.base_url = "http://suggestions.dadata.ru/suggestions/api/4_1/rs/findByEmail/company"

    def email_id_company(self, query: str):

        data = MultipartEncoder(fields={"query": query})
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json',
                   'Authorization': token,
                   'X-Secret': secret}

        response = requests.post(self.base_url, headers=headers, data=data)
        status = response.status_code
        result