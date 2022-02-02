
def Plus(x, y):
    return x + y
def Minus(x, y):
    return x - y
def Multiply(x, y):
    return x * y
def Divide(x, y):
    return x / y

print("Select an option")
print("1 = Plus")
print("2 = Minus")
print("3 = Multiply")
print("4 = Divide")

while True:
    choice = input("Choose between 1, 2, 3 or 4: ")

    if choice in ('1', '2', '3', '4'):
        a = float(input("a: "))
        b = float(input("b: "))

        if choice ==  '1':
            print(a, "+", b, "=", Plus(a, b))

        elif choice == '2':
            print(a, "-", b, "=", Minus(a, b))

        elif choice == '3':
            print(a, "*", b, "=", Multiply(a,b))

        elif choice == '4':
            print(a, "/", b, "=", Divide(a, b))
            break

        else:
            print("Unkown Input")