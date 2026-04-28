HASLO = "kraboburger"
LOGIN = "szlafrok"

login = ""
haslo = ""
licznik = 0

while login != LOGIN or haslo != HASLO:
    login = input("Podaj login: ")
    haslo = input("Podaj hasło: ")
    licznik += 1
    print(f"Koniec pętli - {licznik} próba logowania.")

print(f"OK. Próby: {licznik}")