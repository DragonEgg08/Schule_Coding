Zahlen = input("Bitte gib Zwei Zahlen ein, getrennt mit einem Komma [x,y]:  ").split(",")
Operator = input("Bitte gib einen Operator ein, unterstützt werden: Plus[+], Minus[-], Mal[*], Geteilt[/], Modulu[%]: ")
Ergebnis = 0
match Operator:
    case "+":
        Ergebnis = int(Zahlen[0]) + int(Zahlen[1])
    case "-":
        Ergebnis = int(Zahlen[0]) - int(Zahlen[1])
    case "*":
        Ergebnis = int(Zahlen[0]) * int(Zahlen[1])
    case "/":
        Ergebnis = int(Zahlen[0]) / int(Zahlen[1])
    case "%":
        Ergebnis = int(Zahlen[0]) % int(Zahlen[1])


print(f"{Zahlen[0]} {Operator} {Zahlen[1]} = {Ergebnis}")