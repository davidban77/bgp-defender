# RIPE queries to RIPE for Prefixes through HTTP requests
# By Krlosromero 08-12-2018
# according to https: // github.com/RIPE-NCC/whois/wiki/WHOIS-REST-API

import requests

# https: // rest.db.ripe.net/{source}/{objecttype}/{key}
source = ripe
objecttype = prefixes
key = route/maskAS
