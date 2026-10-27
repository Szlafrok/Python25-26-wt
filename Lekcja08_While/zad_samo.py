LOGIN_POPR = "admin"
HASLO_POPR = "qwerty123456" # bezpieczeństwo to moja pasja!
LIMIT = 3

# Proszę napisać program, który do zmiennej 'login' zapisuje
# podany przez użytkownika login, a następnie do zmiennej 'haslo'
# zapisuje podane przez użytkownika hasło. Proszę za pomocą instrukcji
# if/else, operatora 'and' oraz znaku porównania == napisać program,
# który poinformuje nas, czy podane dane logowania są poprawne, czy nie.

bledy = 0

while bledy < LIMIT:
    login = input("Podaj login: ")
    haslo = input("Podaj hasło: ")

    if login == LOGIN_POPR and haslo == HASLO_POPR:
        print("Zalogowano poprawnie!")
        break
    else:
        print("No i gagatku dałeś złe dane :P")
        bledy += 1


while True:
    break