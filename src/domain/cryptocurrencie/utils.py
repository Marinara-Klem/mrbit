import decimal

import requests
from django.conf import settings


def get_price_cryptocurrency(cryptocurrency_abbreviation: str, currency: str):
    url = f'{settings.URL_BASE_CRYPTOCOMPARE}?api_key={settings.API_KEY_CRYPTOCOMPARE}&fsym={cryptocurrency_abbreviation}&tsyms={currency}'
    response = requests.request('GET', url)

    if response.status_code == 200:
        data = response.json()

        if data.get('Response') != 'Error':
            return decimal.Decimal(data.get(currency))


def cryptocurrencies_for_dollars(cryptocurrency_abbreviation: str):
    return get_price_cryptocurrency(cryptocurrency_abbreviation=cryptocurrency_abbreviation, currency='USD')


def valid_cryptocurrency_abbreviation(abbreviation: str):
    return True if cryptocurrencies_for_dollars(cryptocurrency_abbreviation=abbreviation) else False
