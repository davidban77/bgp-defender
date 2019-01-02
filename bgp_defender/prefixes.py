class Prefixes:
    def __init__(self, prefixes=[]):
        """
        It constructs Prefix objects based on the arg `prefix` passed,
        Arguments:
            prefixes: Could be list of strings or dictionary, that holds the information necessary for creating a prefix. Examples:

            - List of strings
            prefixes = ['1.1.1.1/24', '2.2.2.2']

            - List of dictionaries
            prefixes = [
                {
                    'prefix': '1.1.1.1/24',
                    'asn': 1111
                },
                {
                    'prefix': '1.1.1.1/24',
                    'asn': None
                },
            ]

        Returns:
            :obj:`Prefix`: List of objects placeholder
        """
        self.prefixes = []
        if not isinstance(prefixes, list):
            prefixes = [prefixes]

        for prefix in prefixes:
            self.prefixes.append(Prefix(prefix))


class Prefix:
    pass
