PIN = 1234
Kontostand = 0


PIN_Nutzereingabe = int(input("Geben sie ihre PIN ein: "))

if PIN_Nutzereingabe == PIN:
    while True:
        for i in range(10):
            print()
        print(f"Sie haben noch {Kontostand}€ auf dem Konto")
        Was_tun = input("Möchten sie Geld abheben [1] oder Geld einbezahlen [2] (geben sie die Zahl ihrer Möglichkeit ein, Enter um abzubrechen): ")
        if Was_tun == "":
            exit()
        elif Was_tun == "1":
            Wieviel_Abheben = int(input("Wieviel Geld möchten sie abheben?: "))
            if Kontostand >= Wieviel_Abheben:
                print("Sie haben ihr Geld erfolgreich abgehoben")
                Kontostand -= Wieviel_Abheben
            else:
                print("Sie haben nicht mehr genug Geld auf dem Konto")
        elif Was_tun == "2":
            Kontostand += int(input("Wieviel Geld möchten sie einzahlen?: "))
