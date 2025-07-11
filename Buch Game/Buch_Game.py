from Charakter import Held, Zauberer, Krieger, Monster
from Waffen import Waffe
from Regeln_Werkzeuge import Kampfregeln

#Materialdatenbank füllen


Spieler = Krieger(10, 10, 100, 10, "Gerald")
Gegner = Monster(10, 100)

Schwert = Waffe(1,"Holz",1)
print(Schwert.bonusBerechnen())