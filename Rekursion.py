def Karl(Auswahl):
    def Rekursion():
        eingabe = int(input("Fakultät eingeben"))
        counter = eingabe
        Ausgabe = 1
        Schon_Null = False
        def Fakultät(counter, Ausgabe, Schon_Null):
            if counter == 0:
                Schon_Null = True
            elif not Schon_Null:
                counter -= 1
                Fakultät(counter, Ausgabe, Schon_Null)
            if Schon_Null:
                counter += 1
                Ausgabe = counter*Ausgabe
                print(Ausgabe)
                if counter != eingabe:
                    Fakultät(counter, Ausgabe, Schon_Null)
                else:
                    print(Ausgabe)
        Fakultät(counter, Ausgabe, Schon_Null)

    def Iteration():
        eingabe = int(input("Fakultät eingeben: "))
        Ausgabe = 1
        for i in range(1, eingabe):
            print(i/eingabe*100)
            Ausgabe *= i
        print(Ausgabe)


    if Auswahl == "Rekursion":
        Rekursion()
    elif Auswahl == "Iteration":
        Iteration()

Karl("Iteration")