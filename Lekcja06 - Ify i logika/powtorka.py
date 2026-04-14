for i in range(10):
    print(i)

print("----")
for j in range(5): # 1 argument range(n) - liczby od 0 do n-1
    print(j+2)

n = 10
range(20) # od 0 do 19  | 19 = 20 - 1
range(50) # od 0 do 49  | 49 = 50 - 1
range(n)  # od 0 do n-1 | n-1 = n - 1

print("-----")

for i in range(5, 10): # 5, 6, 7, 8, 9 (bez 10)
    print(i)

print("-----")
for i in range(2, 6): # 2, 3, 4, 5
    print(i)

print("-----")
for i in range(-3, 2): # -3, -2, -1, 0, 1
    print(i)