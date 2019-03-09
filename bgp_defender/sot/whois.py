""" testing using Whois library"""
from ipwhois import IPWhois
from pprint import pprint


class WhoisConnector:

    def __init__(self):
        """to see  what should i initialize the object with"""
        pass

    def Whois_lookup(self, prefix=None, asn=None):
        """create a method to o the lookup by prefix. or ASN, or company
        """
        pass

    def Whois_parser(self):
        """parser into a definitie format"""
    pass


if __name__ == "__main__":
                # test Call
    # inputdata = '193.138.100.0'
    inputdata = 'ASN27648'
    prefix = IPWhois(inputdata)

    result = prefix.lookup_whois()
    pprint(70 * '*')
    pprint(70 * '*')
    pprint("this is the result of the {} whois".format(inputdata))
    pprint(result)
    pprint(70 * '*')

    lookup_result = prefix.lookup_rdap()

    pprint(70 * '*')
    pprint(70 * '*')
    pprint("this is the result of the {} lookup_rdap".format(inputdata))
    pprint(lookup_result)
    pprint(70 * '*')
