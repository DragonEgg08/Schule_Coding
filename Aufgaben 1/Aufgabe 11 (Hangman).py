Wort = input("Gib bitte ein Wort an, welches erraten werden muss: ")
for i in range(100):
    print()
Erratene_Buchstaben = []
Leben = -1
Männchen_Grafisch = ["\n\n\n\n/ \\", "\n |\n |\n |\n/ \\", " ______\n |\n |\n |\n/ \\", " ______\n |/\n |\n |\n/ \\",
                     " ______\n |/   |\n |\n |\n/ \\", " ______\n |/   |\n |    O\n |\n/ \\",
                     " ______\n |/   |\n |    O\n |    |\n/ \\", " ______\n |/   |\n |    O\n |   \\|/\n/ \\",
                     " ______\n |/   |\n |    O\n |   \\|/\n/ \\  / \\"]
while True:
    Wort_Unzensiert = ""
    Buchstabe = input("Gib bitte ein Buchstabe ein: ")
    if Buchstabe.lower() in Wort.lower():
        Erratene_Buchstaben.append(Buchstabe.lower())
    else:
        Leben += 1
        print(f"Dein Männchen hängt gleich:")
        print(Männchen_Grafisch[Leben])
        if Leben == 8:
            print(f"Dein Männchen ist gestorben, das Wort war: {Wort}")
            break

    for i in Wort.lower():
        if i in Erratene_Buchstaben:
            Wort_Unzensiert += i
        else:
            Wort_Unzensiert += "_"
    print(f"Das bisher erratene Wort lautet: {Wort_Unzensiert}")