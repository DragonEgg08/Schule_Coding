def Rekursion(Eingabe):
    Ergebnis = 0
    n = 3
    def Dreifaches(Ergebnis, n):
        if n == 0:
            return Ergebnis
        else:
            Ergebnis = Ergebnis + Eingabe * (n-1)
            return Dreifaches(Ergebnis, n-1)
    return Dreifaches(Ergebnis,n)

def Iteration(Eingabe):
    Ergebnis = 0
    for i in range(3):
        Ergebnis = Ergebnis + Eingabe
    return Ergebnis


while True:
    Func = input("Rekursion oder Iteration: ")
    if Func == "Rekursion":
        Eingabe = int(input("Gib ne Zahl ein: "))
        print(Rekursion(Eingabe))
        break
    elif Func == "Iteration":
        Eingabe = int(input("Gib ne Zahl ein: "))
        print(Iteration(Eingabe))
        break
    else:
        print("Gib richtig ein!")