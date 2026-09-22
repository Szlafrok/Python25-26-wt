liczba = 10
liczba_2 = 15

tekst = "10"
tekst_2 = "15"

print(liczba + liczba_2) # 25
print(tekst + tekst_2) # 1015
# print(liczba + tekst) # BŁĄD

int() 
float() 
str() 

print( type("123") ) # <class 'str'>
print( type(123) ) # <class 'int'>
print( type(5.0) ) # <class 'float'>

wartosc = int(12.4)
print(wartosc)

wartosc = float(2)
print(wartosc)

wartosc = str(12.5)
print(wartosc)

# -----------
wartosc = int("20") # OK
print(wartosc)

wartosc = int("-5") # OK
#wartosc = int("1.0") # BŁĄD
#wartosc = int("1.2") # BŁĄD
#wartosc = int("kosiarka") # Czemu w ogóle o tym rozmawiamy?

wartosc = float("-5") # OK
wartosc = float("1.0") # OK
wartosc = float("1.2") # OK
# wartosc = float("kosiarka") # Czemu w ogóle o tym rozmawiamy?