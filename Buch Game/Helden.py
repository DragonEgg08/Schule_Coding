class Held():
    def __init__(self, stärke:int, angriffswert:int, lebenspunkte:int ,name:str="Held"):
        self.name = name
        self.stärke = stärke


class Zauberer(Held):
    def __init__(self, stärke:int, angriffswert:int, lebenspunkte:int, name: str = "Merlin"):
        super().__init__(name, stärke, angriffswert, lebenspunkte)

    def heilen(self):
        pass


class Krieger(Held):
    def __init__(self, stärke:int, angriffswert:int, lebenspunkte:int, name: str = "Link"):
        super().__init__(name, stärke, angriffswert, lebenspunkte)