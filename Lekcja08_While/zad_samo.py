LOGIN_POPR = "admin"
HASLO_POPR = "qwerty123456" # bezpieczeństwo to moja pasja!

# Proszę napisać program, który do zmiennej 'login' zapisuje
# podany przez użytkownika login, a następnie do zmiennej 'haslo'
# zapisuje podane przez użytkownika hasło. Proszę za pomocą instrukcji
# if/else, operatora 'and' oraz znaku porównania == napisać program,
# który poinformuje nas, czy podane dane logowania są poprawne, czy nie.

login = input("Podaj login: ")
haslo = input("Podaj hasło: ")

if login == LOGIN_POPR and haslo == HASLO_POPR:
    print("Zalogowano poprawnie!")
else:
    print("No i gagatku dałeś złe dane :P")

