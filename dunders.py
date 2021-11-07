class ASAPMob:
    def __init__(self):
        self._members = [
            'A$AP Ant',
            'A$AP Bari',
            'A$AP Ferg',
            'A$AP Illz',
            'A$AP Lotto',
            'A$AP Nast',
            'A$AP Relli',
            'A$AP Rocky',
            'A$AP Snacks',
            'A$AP TyY',

        ]

    def __len__(self):
        return len(self._members)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._members.pop(key)  # remove 1st member
        raise TypeError('Cannot get key')

    def __contains__(self, member):
        return member in self._members

    def __iter__(self):
        while self._members:
            yield self._members.pop() # gets each member and removes from list


asap_mob = ASAPMob()
for member in asap_mob:
    print(member)

print(len(asap_mob))
