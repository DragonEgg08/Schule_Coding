import random

class Würfel:
    def würfeln(anzahlSeiten:int=10) -> int:
        return random.randint(1, anzahlSeiten)

class Kampfregeln:
    def kampf(k1, k2):
        Runden = 0
        while True:
            Runden += 1
            print("Runde " + str(Runden))
            print("Spieler würfelt...")
            Zahl = Würfel.würfeln()
            print(Zahl)