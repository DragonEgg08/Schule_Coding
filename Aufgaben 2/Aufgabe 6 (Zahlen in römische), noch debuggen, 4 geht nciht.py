Zahl_Input = int(input("Bitte gib eine Zahl ein (von 1-3999): "))
Zahl = Zahl_Input
Römische_Zahl = []
Römische_Zahl_Ausgabe = ""

Römische_Zeichen = ["I", "V", "X", "L", "C", "D"]
Römische_Zeichen_Wert = [1,5,10,50,100,500]

Zähler_Zeichen = [0,0,0,0,0,0]

def Letztes_Zeichen(Zeichen, arr: list):
    Zeichen_Liste = []
    for a in range(len(arr)):
        if arr[a] == Zeichen:
            Zeichen_Liste.append(a)
    return Zeichen_Liste[-1]

def Zeichen_entfernen(Zeichen, arr: list) -> int:
    Zeichen_Liste = []
    Wert = 0
    for a in range(len(arr)):
        if arr[a] == Zeichen:
            Zeichen_Liste.append(a)
    for a in range(len(Zeichen_Liste)):
        Wert += Römische_Zeichen_Wert[Römische_Zeichen.index(arr[Zeichen_Liste[0]])]
        arr.pop(Zeichen_Liste[0])
    return Wert


while Zahl != 0:
    match Zahl:
        case _ if Zahl < 5:
            Römische_Zahl.append("I")
            Zahl -= 1
            Zähler_Zeichen[0] += 1
        case _ if Zahl < 10:
            Römische_Zahl.append("V")
            Zahl -= 5
            Zähler_Zeichen[1] += 1
        case _ if Zahl < 50:
            Römische_Zahl.append("X")
            Zahl -= 10
            Zähler_Zeichen[2] += 1
        case _ if Zahl < 100:
            Römische_Zahl.append("L")
            Zahl -= 50
            Zähler_Zeichen[3] += 1
        case _ if Zahl < 500:
            Römische_Zahl.append("C")
            Zahl -= 100
            Zähler_Zeichen[4] += 1
        case _ if Zahl < 1000:
            Römische_Zahl.append("D")
            Zahl -= 500
            Zähler_Zeichen[5] += 1
        case _:
            Römische_Zahl.append("M")
            Zahl -= 1000

    for i in range(len(Zähler_Zeichen)):
        if Zähler_Zeichen[i] > 3 and Zahl_Input != 4:
            print(Zähler_Zeichen)
            Zeichen_Wert = 0
            Zeichen_Wert += Römische_Zeichen_Wert[Römische_Zeichen.index(Römische_Zahl[Letztes_Zeichen(Römische_Zeichen[i + 1], Römische_Zahl)])]
            Zeichen_Wert += Zeichen_entfernen(Römische_Zeichen[i], Römische_Zahl)
            Römische_Zahl.pop(Letztes_Zeichen(Römische_Zeichen[i+1], Römische_Zahl))

            Zahl_Minus = Römische_Zeichen_Wert[i+2]
            while Zahl_Minus > Zeichen_Wert:
                Römische_Zahl.append(Römische_Zeichen[i])
                Zahl_Minus -= Römische_Zeichen_Wert[i]

            Römische_Zahl.append(Römische_Zeichen[i + 2])
            Zähler_Zeichen[i] = 0



for i in Römische_Zahl:
    Römische_Zahl_Ausgabe += i
print(Römische_Zahl_Ausgabe)