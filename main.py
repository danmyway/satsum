#!/usr/bin/env python3
import os

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import argparse
import configparser

configfile = "conf.yaml"
cwd = os.getcwd()


def xconf():
    with open(configfile, "x") as conf:
        conf.write("[DEFAULT]\napiKey =")
    print(f"Created an empty configuration file in {cwd}/{configfile}.")

def readconfig():
    config = configparser.ConfigParser()
    config.read(configfile)

    apiKey = config.get("DEFAULT", "apiKey")

    return apiKey

apiKey = readconfig()

url = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion'
params = {
    'amount': '1',
    'id': '1',
    'convert': 'CZK'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': f'{apiKey}',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=params)
    data = json.loads(response.text)
    print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
