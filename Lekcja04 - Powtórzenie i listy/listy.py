# Lista stringów
zakupy = ["lamborghini", "coś", "coś", "breloczek", "żelki", "PS5", "Komputer"]
#         0               1     2       3            4       5      6
print(zakupy)

print(zakupy[0])
print(zakupy[4])
print(zakupy[5])
#print(zakupy[6])

zakupy[3] = "Bomba wodorowa"
print(zakupy[2])
print(zakupy[3])

print(zakupy)

zakupy.append("kubek")
print(zakupy)

zakupy.remove("coś")
zakupy.remove("coś")
# zakupy.remove("coś") - BŁĄD
print(zakupy)