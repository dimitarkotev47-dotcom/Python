n = int(input("Брой числа: "))
max_chislo = int(input("Въведете число: "))
for i in range(n - 1):
    A = int(input("Въведете число: ")) 
    if A > max_chislo:
        max_chislo = A
print("Най-голямото число е:", max_chislo)