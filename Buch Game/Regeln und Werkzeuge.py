import random
from Buch_Game import Spieler

def Kampfregeln():
    class Würfel():
        def __init__(self, anzahlSeiten:int=20):
            self.anzahlSeiten = anzahlSeiten
        def würfeln(self) -> int:
            return random.randint(1, self.anzahlSeiten)

    def kampf(Held, Monster):
