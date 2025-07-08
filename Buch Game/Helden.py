class Held():
    def __init__(self, name: str = "Held"):
        self.name = name

class Zauberer(Held):
    def __init__(self, name: str = "Merlin"):
        super().__init__(name)

    def heilen(self):



class Krieger(Held):
    def __init__(self, name: str = "Link"):
        super().__init__(name)