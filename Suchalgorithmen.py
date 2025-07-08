def Lineare_Suche():
    Suchfeld = [1,5,7,9,3]
    Suchanfrage = input("Bitte einen Suchbefehl eingeben: ")
    for i in Suchfeld:
        if str(i) == Suchanfrage:
            print("Gefunden")
            break

def Binäre_Suche():
    Suchfeld = [1,2,3,4,5,6,7,8,9]
    Suchanfrage = int(input("Bitte einen Suchbefehl eingeben: "))
    Index_Rechts = len(Suchfeld)
    Index_Links = 0
    Index_Mitte_Temp = 1
    Index_Mitte = 0

    while True:
        if Index_Mitte_Temp == Index_Mitte:
            print("Nicht gefunden")
            exit()
        else:
            Index_Mitte_Temp = Index_Mitte
        Index_Mitte = int((Index_Links+Index_Rechts)/2)
        if Suchfeld[Index_Mitte] == Suchanfrage:
            print("gefunden")
            exit()
        elif Suchfeld[Index_Mitte] > Suchanfrage:
            Index_Rechts = Index_Mitte
        else:
            Index_Links = Index_Mitte


Lineare_Suche()


