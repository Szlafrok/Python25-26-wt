# zad 1
wiek = 632
zgodarodzica = False

if wiek < 18 and zgodarodzica == False:
    print("nie, nie możesz wejść")
else:
    print("dobra, możesz wejść")

if wiek < 18:
    if zgodarodzica == True:
        print("dobra, możesz wejść")
    else:
        print("nie, nie możesz wejść")
else:
    print("dobra, możesz wejść")


# zad 2

plusy = int(input("ile masz plusów?: "))

if plusy >= 10:
    print("masz 2 gwiazdki :D")
elif plusy >= 5:
    print("masz gwiazdkę :)")
else:
    print("nie masz gwiazdki :(")




if plusy >= 10:
    print("masz 2 gwiazdki :D")
else:
    if plusy == 9:
        print("masz gwiazdkę :)")
    elif plusy == 8:
        print("masz gwiazdkę :)")
    elif plusy == 7:
        print("masz gwiazdkę :)")
    elif plusy == 6:
        print("masz gwiazdkę :)")
    elif plusy == 5:
        print("masz gwiazdkę :)")
    elif plusy < 5:
        print("nie masz gwiazdki :(")