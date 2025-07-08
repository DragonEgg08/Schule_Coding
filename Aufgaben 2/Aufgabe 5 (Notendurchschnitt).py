Punkte_Klausuren = input("Bitte gib deine Klausurenpunkte (0-15) getrennt von einem Komma ein [x,y,z,...]: ").split(",")
Punkte_Restlich = input("Bitte gib deine restlichen Punkte (0-15) getrennt von einem Komma ein [x,y,z,...]: ").split(",")

Punkte_Klausuren_Zusammen = 0
Punkte_Restlich_Zusammen = 0

Durchschnitt_Klausuren = 0
Durchschnitt_Restlich = 0

for i in Punkte_Klausuren:
    Punkte_Klausuren_Zusammen += int(i)
for i in Punkte_Restlich:
    Punkte_Restlich_Zusammen += int(i)

Durchschnitt_Klausuren = Punkte_Klausuren_Zusammen / len(Punkte_Klausuren)
Durchschnitt_Restlich = Punkte_Restlich_Zusammen / len(Punkte_Restlich)

print(f"Dein Durschnitt ist: {(Durchschnitt_Restlich + 2 * Durchschnitt_Klausuren)/3}")