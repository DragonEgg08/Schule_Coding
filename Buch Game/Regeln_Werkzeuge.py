import random

class Würfel():
    def __init__(self, anzahlSeiten:int=20):
            self.anzahlSeiten = anzahlSeiten
    def würfeln(self) -> int:
        return random.randint(1, self.anzahlSeiten)

class Kampfregeln():
    def __init__(self):
        pass
    def kampf(self, Held, Gegner):
        pass

