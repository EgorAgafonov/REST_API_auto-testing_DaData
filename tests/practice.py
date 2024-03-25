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

        data = MultipartEncoder(fields={"query": query}, encoding="UTF-8")

        headers = {
            "Content-type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Token {token}",
        }

        response = requests.post(self.base_url, headers=headers, data=data)
        status = response.status_code
        result = ""
        try:
            result = response.json()
        except json.JSONDecodeError:
            result = response.text

        return status, result


dd = DadataAPI()
status, result = dd.email_id_company(query="info@dadata.ru")

print(status)
print(result)

