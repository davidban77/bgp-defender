"""
Holds the Query app module code
"""
from parser.bgp_parser import BgpParser
from parser.ripe_parser import RipeParser
from parser.db_parser import DbParser
from prefixes import Prefix, prefix_helper


class Query:
    pass


class QueryPrefix(Query):
    pass


if __name__ == "__main__":
    # Note! remeber to run it like python -m app.query

    prefixes = [Prefix('1.1.1.1/24')]  # => [Prefix(prefix='1.1.1.1/24', asn=None)]
    # OR
    raw_prefixes = ['1.1.1.1/24', '2.2.2.0/22', {'network': '3.3.3.3/23', 'asn': 3333}]
    prefixes = [prefix_helper(x) for x in raw_prefixes]

    devices = [('router01', 'junos'), ('router02', 'ios')]
    db_info = [('db01', 'elasticsearch'), ('db02', 'mongodb')]

    for prefix in prefixes:
        query = QueryPrefix(prefix, devices=devices, ripe=True, db=db_info)

        # Execute Device related query and parse it
        prefix._result_devices = BgpParser().prefix_parser(query.devices())

        # Execute RIPE query and parse it
        prefix._result_ripe = RipeParser().message_parser(query.ripe())

        # Execute all needed queries (Devices, RIPE and DB)
        prefix._result_db = DbParser().record_parser(query.db())

        # Now normalize attributes. => Add ASN, GeoIP info etc... as standard attributes
        prefix.normalize()

    # Now present it the way you want
    print('######### PREFIX INFO #########')
    for prefix in prefixes:
        print(prefix)  # [Prefix(prefix='1.1.1.1/24', asn='1111', company='XYZ'...)]
    print('###############################')
