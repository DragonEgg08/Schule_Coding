class Katze:
    def __init__(self, spielen:bool):
        self._spielen = spielen

    @property
    def spielen(self):
        if self._spielen:
            return "Katze möchte spielen"
        else:
            return "Katze möchte nicht spielen"
    @spielen.setter
    def spielen(self, spielen):
        if spielen:
            self._spielen = True
        else:
            self._spielen = False

class Siamkatze(Katze):
    def __init__(self, _spielen):
        super().__init__(_spielen)

    @property
    def spielen(self):
        print(self._spielen)

spielen = Siamkatze(True)
f = spielen.spielen
print(f)

