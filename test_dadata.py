from dadata_api import DadataAddress
from settings.settings import token, secret
import requests
import pytest
import os

dadata = DadataAddress(token=token, secret=secret)

def test_get_address_info_successfull(address='мск сухонская 11 89'):

    status, result = dadata.get_address_standartization(address=address)
    print(status)
    print(result)
