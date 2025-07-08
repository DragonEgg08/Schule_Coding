import random

class Würfel:
    def __init__(self, anzahlSeiten:int=20):
            self.anzahlSeiten = anzahlSeiten
    def würfeln(self) -> int:
        return random.randint(1, self.anzahlSeiten)

class Kampfregeln:
    def kampf(self, k1, k2):
        pass

