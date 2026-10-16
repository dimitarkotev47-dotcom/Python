a = float(input("a = "))
b = float(input("b = "))
deistvie = input("Въведете действие (+, -, *, /): ")
if deistvie == "+":
    print("a + b =", a + b)
elif deistvie == "-":
    print("a - b =", a - b)
elif deistvie == "*":
    print("a * b =", a * b)
elif deistvie == "/":
    if b != 0:
        print("a / b =", a / b)
    else:
        print("На нула не може да се дели! ")
