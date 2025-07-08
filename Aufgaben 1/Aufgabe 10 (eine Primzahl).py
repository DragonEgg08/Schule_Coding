Zahl = int(input("Bitte gib eine Zahl ein, um zu prüfen, ob sie eine Primzahl ist: "))
Teilbare_Zahlen = []

for i in range(2, Zahl):
    x1 = i/Zahl
    print(f"Fortschritt: {int(x1*100)}%")
    if Zahl % i == 0:
        Teilbare_Zahlen.append(i)

if len(Teilbare_Zahlen) > 0:
    print(f"Die {Zahl} ist keine Primzahl, da sie durch \n{Teilbare_Zahlen}\nteilbar ist")
else:
    print(f"Die {Zahl} ist eine Primzahl")