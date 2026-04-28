while True:
    komenda = input("Komenda: ")

    if komenda == "info":
        print("Wersja 1.2.3")
    elif komenda == "exit":
        print("Do widzenia!")
        break
    elif komenda == "skip":
        print("Pominięto")
        continue

    print("----- Komenda przetworzona! -----")