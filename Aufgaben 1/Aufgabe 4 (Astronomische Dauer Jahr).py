while True:
    try:
        Jahr = int(input("Bitte gib ein Jahr ein: "))
        break
    except:
        print("Nur Ganzzahlen sind erlaubt!")
Schaltjahr = False

if Jahr % 4 == 0:
    if Jahr % 100 == 0 and Jahr % 400 != 0:
        Schaltjahr = False
    else:
        Schaltjahr = True

if Schaltjahr:
    print(f"Das Jahr {Jahr} ist ein Schaltjahr.")
else:
    print(f"Das Jahr {Jahr} ist kein Schaltjahr.")