class Held:
    def __init__(self, stärke:int, angriffswert:int, lebenspunkte:int ,name:str="Held"):
        self.name = name
        self.stärke = stärke
        self.angriffswert = angriffswert
        self.lebenspunkte = lebenspunkte


class Zauberer(Held):
    def __init__(self, stärke:int, angriffswert:int, lebenspunkte:int, name: str = "Merlin", heilfaktor:int = 0.1):
        super().__init__(stärke, angriffswert, lebenspunkte, name)
        self.lebenspunkte_aktuell = lebenspunkte
        self.heilfaktor = heilfaktor

    def heilen(self):
        if self.lebenspunkte * 0.1 + self.lebenspunkte_aktuell > self.lebenspunkte:
            self.lebenspunkte_aktuell = self.lebenspunkte
        else:
            self.lebenspunkte_aktuell += int(self.lebenspunkte * 0.1)
        print(f"{self.name} hat sich geheilt, seine Lebenspunkte betragen {str(self.lebenspunkte_aktuell)}")


class Krieger(Held):
    def __init__(self, stärke:int, angriffswert:int, lebenspunkte:int, name: str = "Link"):
        super().__init__(stärke, angriffswert, lebenspunkte, name)