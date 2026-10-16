broi = 0

dolna = int(input("Въведете долна граница: "))
gorna = int(input("Въведете горна граница: "))
for i in range(10):
    chislo = int(input(f"Въведете число {i + 1}: "))
    if chislo < dolna:
        print("Под долната граница")
    elif chislo > gorna:
        print("Над горната граница")
    else: broi += 1
print("Брой числа в интервала:", broi)