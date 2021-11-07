class Portishead:
    def __init__(self):
        print('Portishead')


class KayneWest(Portishead):
    def __init__(self):
        print('Kaybe West')
        super().__init__()
        # super().__init__()


class ASAPRocky(Portishead):
    def __init__(self):
        print('A$AP Rocky')
        super().__init__()


class ASAPSebbie(ASAPRocky, KayneWest):
    def __init__(self):
        print('A$AP Sebbie')
        super().__init__()


asap_sebbie = ASAPSebbie()  # Portishead called twice which is undesirable
