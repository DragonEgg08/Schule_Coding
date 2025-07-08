Zahlen = input("Drücke Enter, um die ersten 10 natürlichen Zahlen, eine Zahl, um zu dieser zu summieren oder [x-y] ein, um von x bis y zu summieren: ")
Summe = 0

if Zahlen == "":
    print("Die Summe von 1 bis 10 wird berechnet...")
    for i in range(1, 11):
        Summe += i
elif "-" in Zahlen:
    Zahlen = Zahlen.split("-")
    print(f"Die Summe von {Zahlen[0]} bis {Zahlen[1]} wird berechnet...")
    for i in range(int(Zahlen[0]), int(Zahlen[1])+1):
        Summe += i
else:
    print(f"Die Summe von {Zahlen} wird berechnet...")
    for i in range(1, int(Zahlen)+1):
        Summe += i

print("Die Summe deiner Zahl beträgt: " + str(Summe))