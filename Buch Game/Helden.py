class Held():
    def __init__(self, stärke:int, angriffswert:int, lebenspunkte:int ,name:int="Held"):
        self.name = name
        self.stärke = stärke

class Zauberer(Held):
    def __init__(self, name: str = "Merlin"):
        super().__init__(name, )

    def heilen(self):



class Krieger(Held):
    def __init__(self, name: str = "Link"):
        super().__init__(name, )