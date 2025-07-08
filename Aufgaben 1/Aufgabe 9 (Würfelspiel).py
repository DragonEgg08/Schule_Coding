import random

print("Der Würfel fällt...")
Würfelgröße = int(input("Wieviele Zahlen soll der Würfel haben?: "))

Wurfliste = []

for i in range(999999999999999999999999999999999999999999999999999999999999999999):
    Würfel = random.randint(1, Würfelgröße)
    Wurfliste.append(Würfel)

    if Würfel == int(Würfelgröße / 2):
        break
print(f"Die vollstände Liste der Würfe: \n {Wurfliste}")
print(f"Die {Würfelgröße} ist nach {i+1} Würfen gefallen")
