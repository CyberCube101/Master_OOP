class Portishead:
    def __init__(self):
        print('Portishead')


class KayneWest(Portishead):
    def __init__(self):
        print('Kaybe West')
        Portishead.__init__(self)
        # super().__init__()


class ASAPRocky(Portishead):
    def __init__(self):
        print('A$AP Rocky')
        Portishead.__init__(self)


class ASAPSebbie(ASAPRocky, KayneWest):
    def __init__(self):
        print('A$AP Sebbie')
        ASAPRocky.__init__(self)
        KayneWest.__init__(self)


asap_sebbie = ASAPSebbie()  # Portishead called twice which is undesirable
