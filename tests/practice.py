from settings.settings import *
import pytest
import requests
from requests_toolbelt import MultipartEncoder
import httpx
import json


class DadataAPI:

    def __init__(self):
        self.base_url = "http://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party"

    def find_company(self, query: str):

        data = MultipartEncoder(fields={"query": query}, encoding="utf-8")

        headers = {
            "Content-type": data.content_type,
            "Accept": "application/json",
            "Authorization": f"Token {token}"}

        response = requests.post(self.base_url, headers=headers, data=data)
        stat = response.status_code
        res = ''
        try:
            res = response.json()
        except json.JSONDecodeError:
            res = response.text

        return stat, res


dd = DadataAPI()
status, result = dd.find_company(query="7707083893")

print(status)
print(result)

