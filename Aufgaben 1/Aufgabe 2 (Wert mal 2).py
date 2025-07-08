#   Pseudocode
# input % 2 = 0: *2
# input % 2 != 0: +1
while True:
    try:
        input = int(input("Bitte gib eine Zahl ein: "))
        break
    except:
        print("Nur Zahlen sind erlaubt!")
if input % 2 == 0:
    print(input * 2)
else:
    print(input + 1)