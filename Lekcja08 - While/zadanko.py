HASLO = "kraboburger"
LOGIN = "szlafrok"

# Prosze napisać program, który wczytuje od użytkownika login i hasło
# a następnie wypisuje OK, jesli dane logowania (hasło i login) są poprawne
# lub "BŁĄD", jeśli nie są poprawne.

# Należy zapisać wartości funkcją input() do zmiennych i wykorzystać 
# słowo IF wraz z operatorami logicznymi.

login = input("Login: ")
haslo = input("Hasło: ")

if login == LOGIN and haslo == HASLO:
    print("OK")
else:
    print("BŁĄD")