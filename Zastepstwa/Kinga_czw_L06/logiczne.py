login = "admin"
haslo = "cyberka"

podany_login = input("Podaj login: ")
podane_haslo = input("Podaj haslo: ")

if podane_haslo == haslo and podany_login == login:
    print("Poprawny login i hasło")
else:
    print("Błędne dane")