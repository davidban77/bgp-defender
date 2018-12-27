# RIPE queries to RIPE for Prefixes through HTTP requests
# By Krlosromero 08-12-2018
# according to https: // github.com/RIPE-NCC/whois/wiki/WHOIS-REST-API
import time
import requests

from urllib.parse import urlencode
from requests import ConnectionError, ConnectTimeout, HTTPError
from pprint import pprint


class RipeConnector(object):
    "Class that uses the RIPE restful API"

    def __init__(self, base_url=None, user=None, cred=None):
        requests.packages.urllib3.disable_warnings()
        self.base_url = base_url
        self.user = user
        self.header = {'content-type': 'application/json'}
        self.verify = False
        self.api_calls = 0

        self.session = requests.Session()
        if self.user:
            self.session.auth = (user, cred)

    def http_call(self, method, url, data=None, headers=None, verify=False, params=None):
        "Standard method to perform calls"
        try:
            if data:
                _response = getattr(self.session, method.lower())(
                    url,
                    data=urlencode(data),
                    headers=headers,
                    params=params,
                    verify=verify)

            else:
                _response = getattr(self.session, method.lower())(
                    url,
                    headers=headers,
                    params=params,
                    verify=verify)

            # pprint(_response.json())
            time.sleep(0.5)
            self.api_calls += 1

        except (ConnectTimeout, ConnectionError) as err:
            print(
                '[ERROR] Connection Error, could not perform {} operation: {}'.format(method, err))
            return False
        except HTTPError as err:
            print(
                '[ERROR] An unknown error has been encountered: {} - {}'.format(err, _response.text))
            return False

        return _response

    def get_prefix(self, prefix, asn):
        """
        Gets prefix information by passing prefix and asn:
        prefix: 193.0.0.0/21
        ASN: 3333
        """
        _url = '{}/ripe/route/{}AS{}.json'.format(self.base_url, prefix, asn)
        _response = self.http_call('get', _url)

        if _response.status_code == 404:
            print('[ERROR] The query did not return any valid object: {}'.format(
                _response.text))
            return False
        elif _response.status_code == 400:
            print('[ERROR] Bad request: {}'.format(
                _response.text))
            return False

        if not _response:
            if hasattr(_response, 'text'):
                print('[ERROR] Could not perform GET operation\n{}'.format(
                    _response.text))
            else:
                print('[ERROR] Could not perform GET operation')
            return False

        print('[INFO] Prefix found: {} - ASN {}'.format(prefix, asn))

        return _response.json()


if __name__ == "__main__":
    # test Call
    test_session = RipeConnector('http://rest.db.ripe.net')
    prefix = test_session.get_prefix('193.0.0.0/21', 3333)
    if prefix:
        pprint(prefix)
        print('[INFO] Pues si lo encontro!')
    else:
        print('[ERROR] Bad! no lo encontro...')
    # to keep progressing in the content  of the reply for error from the API itself
    # extract Values from the response itself for what is needed
