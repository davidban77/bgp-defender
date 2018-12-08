# RIPE queries to RIPE for Prefixes through HTTP requests
# By Krlosromero 08-12-2018
# according to https: // github.com/RIPE-NCC/whois/wiki/WHOIS-REST-API

import requests

from requests import HTTPError
import json
from pprint import pprint


def ripe_query(prefix, asnumber):

    source = 'ripe'
    objecttype = 'route'
    # prefix = '193.0.0.0/21'
    # asnumber= '3333'
    key = f'{prefix}AS{asnumber}'
    # building the URL for request
    url = f'http://rest.db.ripe.net/{source}/{objecttype}/{key}.json'

    try:

        r = requests.get(url)
        print(f'Request Status {r.status_code}')
        r.raise_for_status()
    except HTTPError as err:
        print('ERROR!!'.format(r.status_code))
        print(str(err))
# pending more Errors to Catch
    return r.json()


# test Call
print(ripe_query('193.0.0.0/21', '3333'))
# to keep progressing in the content  of the reply for error from the API itself
# extract Values from the response itself for what is needed
