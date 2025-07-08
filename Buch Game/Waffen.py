def Material_Datenbank(Material) -> int:
    match Material:
        case "Holz":
            return 0


class Waffe:
    def __init__(self, bonus:int, material:str, magie:int):
        self.bonus = bonus
        self.material = material
        self.magie = magie

    def bonusBerechnen(self):
        Materialbonus = Material_Datenbank(self.material)
        return self.bonus + Materialbonus + self.magie