import random

Random_Zahl = random.randint(1,100)
Versuche = int(input("Wieviele Versuche möchtest du insgesamt nur haben? (gib 0 für unendlich ein): "))
if Versuche == 0:
    Versuche = 9999999999999999999999

for i in range(1,Versuche):
    if i > Random_Zahl:
        print("Deine Zahl ist größer")
    elif i < Random_Zahl:
        print("Deine Zahl ist kleiner")
    elif i == Random_Zahl:
        print("Deine Zahl ist richtig")
        break
    if i > Versuche:
        break

print(f"Du hast {i} Versuche gebraucht")