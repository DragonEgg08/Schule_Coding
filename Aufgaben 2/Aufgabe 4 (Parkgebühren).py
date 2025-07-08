import math

Minuten_Parken = int(input("Wieviele Minuten möchten sie parken?: "))
Gebühren = 0

if Minuten_Parken > 60:
    Gebühren = int(math.floor(Minuten_Parken / 60) * 2)

if Gebühren == 0:
    print("Sie könnten kostenfrei parken")
elif Gebühren < 12:
    print(f"Sie müssen {Gebühren}€ Gebühren zahlen")
else:
    print(f"Sie müssen 12€ Gebühren zahlen")