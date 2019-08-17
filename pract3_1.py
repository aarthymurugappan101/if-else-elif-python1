usrInput = input("Enter ph value: ")
usrInput = int(usrInput)

if usrInput > 7:
    print("Alkaline")
if usrInput == 7:
    print("Netural")
if usrInput < 7:
    print("Acidic")