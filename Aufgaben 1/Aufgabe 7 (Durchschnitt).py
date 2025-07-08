Zahlen = input("Drücke Enter um den Durchschnitt von 7, 15, 25, 64 und 98 zu berechnen, oder Zahlen getrennt mit einem Komma um variable Zahlen zu berechnen [x,y,z...]: ")
Summe = 0
if Zahlen == "":
   Zahlen = "7,15,25,64,98"

Zahlen = Zahlen.split(",")

for i in Zahlen:
    Summe += int(i)

print(f"Dein Durchschnitt beträgt: {Summe / len(Zahlen)}")