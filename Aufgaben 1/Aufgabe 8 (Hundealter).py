Alter = int(input("Bitte gib das Alter deines Hundes ein (in Jahren), um es in Menschenjahren umzurechnen: "))
Alter_Hund = 0

if Alter == 1:
    Alter_Hund = 14
elif Alter == 2:
    Alter_Hund = 22
elif Alter > 2:
    Alter_Hund = 22 + ((Alter-2)*5)

print(f"Dein Hund ist in Menschenjahren {Alter_Hund} Jahre alt")