import math

while True:
    print("\n===== Scientific Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Sin")
    print("8. Cos")
    print("9. Tan")
    print("10. Log")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "0":
        print("Calculator Closed")
        break

    elif choice in ["1", "2", "3", "4", "5"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result =", a + b)

        elif choice == "2":
            print("Result =", a - b)

        elif choice == "3":
            print("Result =", a * b)

        elif choice == "4":
            if b == 0:
                print("Cannot divide by zero")
            else:
                print("Result =", a / b)

        elif choice == "5":
            print("Result =", a ** b)

    elif choice == "6":
        num = float(input("Enter number: "))
        print("Result =", math.sqrt(num))

    elif choice == "7":
        angle = float(input("Enter angle in degrees: "))
        print("Result =", math.sin(math.radians(angle)))

    elif choice == "8":
        angle = float(input("Enter angle in degrees: "))
        print("Result =", math.cos(math.radians(angle)))

    elif choice == "9":
        angle = float(input("Enter angle in degrees: "))
        print("Result =", math.tan(math.radians(angle)))

    elif choice == "10":
        num = float(input("Enter number: "))
        print("Result =", math.log10(num))

    else:
        print("Invalid Choice")