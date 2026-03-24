import random
import string
import time


ilosc_znakow = int(input("ile chcesz, aby twoje haslo mialo znakow?: "))

start = time.time()
haslo = ""
znaki = string.ascii_lowercase + string.ascii_uppercase + string.punctuation

for _ in range(ilosc_znakow):
    haslo += random.choice(znaki)

print(f"Twoje haslo to: {haslo}")
end = time.time()
print(f"wygenerowanie zajelo {end - start:.10f} sekund/y")