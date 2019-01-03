"""
Prefix Main module
"""
from netaddr import IPNetwork


class Prefix:
    """
    IP Network construct that consolidates all the data associated to a network prefix.
    """
    def __init__(self, network, asn=None, company=None):
        """
        It construct the Prefix object based on `network`, `asn` and `company`. The `network`
        attribute has a property attached to validate IP address/network
        Returns:
            :obj: `Prefix` object placeholder
        """
        self.network = network
        self.asn = asn
        self.company = company

    def _gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('{}={}'.format(key, getattr(self, key)))
        return ', '.join(attrs)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, self._gatherAttrs())

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self._gatherAttrs())

    @property
    def network(self):
        return self._network

    @network.setter
    def network(self, value):
        valid, res = self.is_ip(value)
        if not valid:
            self._network = None
            raise ValueError('Incorrect IP address/network: {}'.format(value))
        self._network = res
        # Resurfacing the private part
        self.private_network = self._network.is_private()

    @property
    def asn(self):
        return self._asn

    @asn.setter
    def asn(self, value):
        try:
            self._asn = int(value)

            # Setting range based on 32-bit ASN numbering
            if not 1 < self._asn <= 4294967295:
                raise ValueError

            # Determining if private ASN based on RFC 6996
            if 64512 < self._asn <= 65534 or 4200000000 < self._asn <= 4294967294:
                self.private_asn = True
            else:
                self.private_asn = False

        except ValueError:
            self._asn = None
            raise ValueError('Incorrect value for ASN: {}'.format(value))
        except TypeError:
            self._asn = None

    @staticmethod
    def is_ip(ip):
        """
        Validation of IP address/network
        Argument:
            ip(str): IP address/network string
        Returns:
            :tuple: `(bool, value)` -> (True, IPNetwork(ip)) when evaluated to True
                                    -> (False, error) when evaluated to False
        """
        try:
            ip_obj = IPNetwork(ip)
        except Exception as err:
            return False, str(err)
        return True, ip_obj


def prefix_helper(prefix):
    """
    It constructs Prefix objects based on the arg `prefix` passed,
    Arguments:
        prefix: Could be a string or dictionary, that holds the information necessary for creating a
        Prefix object. Examples:

        - String
        prefix = '1.1.1.1/24',

        - Dictionary
        prefixes = {
            'network': '1.1.1.1/24',
            'asn': 1111
        }

    Returns:
        :obj:`Prefix`: List of objects placeholder
    """
    if isinstance(prefix, str):
        return Prefix(prefix)
    elif isinstance(prefix, dict):
        if 'network' in prefix:
            return Prefix(**prefix)
