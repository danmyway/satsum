#!/usr/bin/env python3
import os

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import argparse
import configparser

configfile = "conf.yaml"
cwd = os.getcwd()

#amount 1 returns average market price
#convto == convert to
convto = 'BTC'
#convfrom == convert from
convfrom = 'CZK'

parser = argparse.ArgumentParser()
#parser.add_argument()



args = parser.parse_args()

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

url_conversion = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion'
params_conversion = {
    'amount': '1',
    'symbol': f'{convto}',
    'convert': f'{convfrom}'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': f'{apiKey}',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url_conversion, params=params_conversion)
    data_json = json.loads(response.text)
    data = data_json['data']['quote'][f'{convfrom}']['price']
    print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
