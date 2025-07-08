#Einfügen von Sachen, Entfernen, Anzeigen der kompletten Liste (Anzahl Artikel immer anzeigen)
Einkaufsliste = []

#Einfügen der Artikel
while True:
    Eingabe = input("Gib ein Artikel ein und drücke Enter (leerlassen zum Bestätigen der Liste): ")
    Einkaufsliste.append(Eingabe)
    if Eingabe == "":
        break
print("Deine Aktuelle Einkaufsliste enthält: ")

for i in range(len(Einkaufsliste)-1):
    print(f"{i+1}. {Einkaufsliste[i]}")

while True:
    Option = input("Drücke [s] zum Speichern, [r] zum entfernen von Artikeln oder [a] zum anzeigen: ")

    if Option == "s":
        with open("Liste.txt", "a") as Datei:
            for i in range(len(Einkaufsliste)-1):
                Datei.write(f"{i+1}. {Einkaufsliste[i]}\n")
    elif Option == "r":

        for i in range(len(Einkaufsliste)-1):
            print(f"{i+1}. {Einkaufsliste[i]}")

        while True:
            Eingabe_Entfernen = input("Gib die Nummer des Artikel ein, leerlassen zum Beenden: ")
            if Eingabe_Entfernen != "":
                Einkaufsliste.pop(int(Eingabe_Entfernen)-1)
                print(Einkaufsliste)
            else:
                break
    elif Option == "a":
        for i in range(len(Einkaufsliste) - 1):
            print(f"{i + 1}. {Einkaufsliste[i]}")