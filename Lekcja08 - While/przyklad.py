x = 5

while x < 10:
    x += 1
    print(x * 2)
    print("---")

print("############################")


print("Terminal - wpisz 'exit' aby zakończyć.")

komenda = ""
while komenda != "exit":
    komenda = input("Komenda: ")

    if komenda == "info":
        print("Wersja 1.0")
    elif komenda == "exit":
        print("Do zobaczenia")
    
print("Koniec programu")