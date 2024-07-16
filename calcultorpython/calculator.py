def log_to(enter):
    file = open("History.txt","a")
    file.write(enter + "\n")
def read():
    file = open("History.txt","r")
    history =file.readlines()
    try:
        if history:
            print("Showing History:")
            for line in history:
                print(line.strip())
            else:
                print("No History Found")
    except Exception as e:
        print(f"an error occured while reading the history:{e}")





Shrey = True
print("1-Addition \n2-Substraction\n3-Multiplication\n4-Division\n5-power to\n6-Rounding\n7-Remaining\n8-Show History\noo-Exit")

while Shrey is True:
    opp = int(input("Enter the Operator:"))
    if opp==8:
        read()




    First = int(input("Enter the first digit:"))
    if First == 00:
        print("Closing the app")
        exit()
    Sec = int(input("Enter the sec digit:"))
    if Sec==00:
        print("Closing the app")
        exit()

    if opp == 1:
        Sum = First + Sec
        Sum2 = (f"{First}+{Sec}={Sum}")
        log_to(Sum2)
        print(Sum)
    elif opp == 2:
        Sum = First - Sec
        Sum2 = (f"{First}-{Sec}={Sum}")
        log_to(Sum2)
        print(Sum)
    elif opp == 3:
        Sum = First * Sec
        Sum2 = (f"{First}-{Sec}={Sum}")
        log_to(Sum2)
        print(Sum)
    elif opp == 4:
        Sum = First / Sec
        Sum2 = (f"{First}/{Sec}={Sum}")
        log_to(Sum2)
        print(Sum)
    elif opp == 5:
        Sum = First ** Sec
        Sum2 = (f"{First}^{Sec}={Sum}")
        log_to(Sum2)
        print(Sum)
    elif opp == 6:
        Sum = First // Sec
        Sum2 = (f"{First}//{Sec}={Sum}")
        log_to(Sum2)
        print(Sum)
    elif opp == 7:
        Sum = First % Sec
        Sum2 = (f"{First}%{Sec}={Sum}")
        log_to(Sum2)
        print(Sum)
    elif opp == 00:
        Shrey = False
        print("Closing the app")
    else:
        print("Wrong input")


