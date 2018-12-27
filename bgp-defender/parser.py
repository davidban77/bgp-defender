"""
Module to parse router BGP database and sent it to an ordered structure
{
    ('1.1.1.0/24', 7777): [
        {
            'preferred': False,
            'as_path': [111, 123],
            'local_pref': 100,
            'med: 10
        },
        {
            'preferred': True,
            'as_path': [444],
            'local_pref': 150
        }
    ]
}
"""
import re

patterns = [
    re.compile(r'(?P<as_path>AS path:.{1,10})'),
    re.compile(r'(?P<med>MED.{1,2})'),
    re.compile(r'(?P<prefix>\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b\/.[0-9])\s+'),
    re.compile(r'to\s+(?P<next_hop_ip>\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'),
]
