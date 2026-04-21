studenciak = True
wiek = 21

# if studenciak:
#     if wiek < 26:
#         print("nie płacisz pan podatku")
#     else:
#         print("płacisz podatek")
# else:
#     print("płacisz podatek")


print(studenciak)

print(not studenciak) # False

print(not False) # True


if wiek < 26 and studenciak:
    print("nie płacisz pan podatku")
else:
    print("płacisz podatek :C")

print("--- AND ---")

print(False and False) # False
print(False and True) # False
print(True and False) # False
print(True and True) # True



if not studenciak or wiek >= 26:
    print("płacisz podatek")
else:
    print("nie płacisz podatku :D")

print("--- OR ---")

print(False or False) # False
print(False or True) # True
print(True or False) # True
print(True or True) # True