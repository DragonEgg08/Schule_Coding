Umsatz = int(input("Bitte gib deinen Umsatz ein: "))
Rabatt = 0

if Umsatz > 500:
    Rabatt = 0.1
elif Umsatz > 100:
    Rabatt = 0.05

if Rabatt > 0:
    print(f"Dein Rabatt beträgt {int(Rabatt * 100)}%, du musst also nur {Umsatz - Umsatz * Rabatt}€ bezahlen")
else:
    print(f"Du bekommst keinen Rabatt und musst die vollen {Umsatz}€ zahlen")