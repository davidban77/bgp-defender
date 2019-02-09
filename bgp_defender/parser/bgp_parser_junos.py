from pprint import pprint
import re
"""
Holds the BGP Parser object
"""


class BgpParser:
    pass


def main():
    with open('../../data/juniper-table.txt', 'r') as f:
        table = f.readlines()

    patterns = [
        re.compile(
            r'(?P<prefix>\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b\/.[0-9])\s+'),
        re.compile(r'(?P<as_path>AS path:.{1,10})'),
        re.compile(
            r'(?P<next_hop_ip>\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'),
        re.compile(r'(?P<med>MED.{1,2})')
    ]

    result_list = []
    # list of dictionaries ( dict per BGP route entry)
    regex_dict = {}

    for line in table:
        for regexp in patterns:
            match = re.search(regexp, line)
            if match:
                if ('prefix') in match.groupdict():
                    regex_dict = {'prefix': match.group('prefix')}
                    result_list.append(regex_dict)
                else:
                    regex_dict.update(match.groupdict())
    #                                revised="#".join(result_list)
    #                               print(revised)

    #                                t = regex_dict.items(1)
    #                                print(t)
    pprint(result_list)


if __name__ == "__main__":
    main()
