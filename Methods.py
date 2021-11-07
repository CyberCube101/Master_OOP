import random

TRAP_ARTISTS = [
    'Rick Ross', 'Future', 'Designer', 'Jeezy'

]




class TrapArtist:
    _hits = ['Dead Presidents',
             'Panda',
             'Money']
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name not in TRAP_ARTISTS:
            raise ValueError('%s is Not a trap artist' % name)
        self._name = name

    @staticmethod  # good for creating instances
    def random_artist():
        return TrapArtist(random.choice(TRAP_ARTISTS))

    @classmethod  # allows us to access class properties
    def hits(cls):
        return cls._hits


ta = TrapArtist.random_artist()
print(ta.name)
print(TrapArtist.hits())
