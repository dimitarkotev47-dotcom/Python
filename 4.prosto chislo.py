n = int(input("n ="))

prosto = True

for i in range(2, n):
    if n % i == 0:
        prosto = False
        break

if prosto and n > 1:
    print("Числото е просто")
else:
    print("Числото не е просто")