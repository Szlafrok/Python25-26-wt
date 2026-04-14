hp = float(input("Podaj HP: "))

if hp > 0:
    print("ŻYJEMY :D")
else: # w przeciwnym razie
    print("WE DED :<")



for i in range(0, 31): # 0, 1, 2, ..., 30
    if i % 2 == 0:
        print(f"{i} jest parzysta")
    else:
        print(f"{i} jest nieparzysta")

# i = 0
# while True:
#   ...
#   i += 1

"""
    1 ELSE - MA SENS

jeżeli masz min. 10 lat:
    podskocz
w przeciwnym razie:
    siedź dalej

    
    ELSE BEZ IFA - NIE MA SENSU

w przeciwnym razie:
    wypij kawę

    
    WIĘCEJ NIŻ 1 ELSE - NIE MA SENSU

jeżeli masz ochotę:
    wypij herbatę
w przeciwnym razie:
    wypij wodę
w przeciwnym razie:
    wypij kawę

"""