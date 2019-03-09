"""
Holds REST API type of objects
"""
import time
import requests

from urllib.parse import urlencode
from requests import ConnectionError, ConnectTimeout, HTTPError
from pprint import pprint


class RipeConnector:
    "Class that uses the RIPE restful API"

    def __init__(self, base_url=None, user=None, cred=None):
        requests.packages.urllib3.disable_warnings()
        self.base_url = base_url
        self.user = user
        self.headers = {'Content-Type': 'application/json'}
        self.verify = False
        self.api_calls = 0

        self.session = requests.Session()
        self.session.headers['Accept'] = 'application/json'
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

    @staticmethod
    def error_checker(response_obj):

        if response_obj.status_code == 400:
            print('[ERROR][{}] Illegal input - incorrect value in one or more parameters: {}'.format(
                response_obj.status_code, response_obj.text))
            return True
        elif response_obj.status_code == 404:
            print('[WARNING][{}] No object(s) found: {}'.format(
                response_obj.status_code, response_obj.text))
            return True

        # if not response_obj:
        #     if hasattr(response_obj, 'text'):
        #         print('[ERROR] Could not perform GET operation\n{}'.format(
        #             response_obj.text))
        #     else:
        #         print('[ERROR] Could not perform GET operation')
        #     return True

        return False

    def get_prefix(self, prefix, asn):
        """
        Gets prefix information by passing prefix and asn:
        prefix: 193.0.0.0/21
        ASN: 3333
        """
        _url = '{}/ripe/route/{}AS{}.json'.format(self.base_url, prefix, asn)
        _response = self.http_call('get', _url)

        if RipeConnector.error_checker(_response):
            return False

        print('[INFO] Prefix found: {} - ASN {}'.format(prefix, asn))

        return _response.json()

    def search_prefix(self, prefix):
        """
        Search based on a query-string for IP/Network address
        query-string: `prefix`
        flags: resource       --> To look on other databases

        It expects the `inetnum` and `route` object of the prefix sent

        NOTE: The prefix has to be either an IP address (1.1.1.1) or a network (1.1.1.0/24) for the query to work
        """
        _url = '{}/search?flags=no-filtering&query-string={}&flags=resource'.format(
            self.base_url, prefix)
        _response = self.http_call('get', _url)

        if RipeConnector.error_checker(_response):
            return False

        print('[INFO] Prefix found - Prefix {}'.format(prefix))

        return _response.json()

    def search_asn(self, asn):
        """
        Search based on a query-string for ASN
        query-string: `asn`
        inverse-attribute: `origin`  --> which refers to ASN

        It expects the `route` object of the `asn` sent
        """
        _url = '{}/search?flags=no-filtering&query-string=AS{}&inverse-attribute=origin'.format(
            self.base_url, asn)
        _response = self.http_call('get', _url)

        if RipeConnector.error_checker(_response):
            return False

        print('[INFO] Records of ASN {} found'.format(asn))

        return _response.json()

    def search_mantainer(self, mnt_by):
        """
        Search based on a query-string for mantainer
        query-string: `mantainer`    --> Mantainer Code in RIPE
        inverse-attribute: `mnt-by`  --> which refers to ASN

        It expects ...
        """
        _url = '{}/search?flags=no-filtering&query-string={}&inverse-attribute=mnt-by'.format(
            self.base_url, mnt_by)
        _response = self.http_call('get', _url)

        if RipeConnector.error_checker(_response):
            return False

        print('[INFO] Records for {} found'.format(mnt_by))

        return _response.json()


if __name__ == "__main__":
    # test Call
    test_session = RipeConnector('http://rest.db.ripe.net')
    # prefix = test_session.get_prefix('193.0.0.0/21', 3333)
    prefix = test_session.search_prefix('193.138.100.0/24')
    # prefix = test_session.get_prefix('185.10.116.0/22', 199559)
    if prefix:
        pprint(prefix)
        print('[INFO] Pues si lo encontro!')
    else:
        print('[ERROR] Bad! no lo encontro...')
    # to keep progressing in the content  of the reply for error from the API itself
    # extract Values from the response itself for what is needed
