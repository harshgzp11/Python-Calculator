#Building an ADVANCED Calculator using PYTHON

import math

history = []   # To store all previous operations

while True:
    print("Choose the Operator: ")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulo (%)")
    print("6. Power")
    print("7. Floor Division")
    print("8. Square Root")
    print("9. Cube Root")
    print("10. Exit")
    print("11. Show History")
    print("12. Clear History")

    operator = input("Enter your choice: ")

    # Handling history BEFORE number inputs
    if operator == "11":
        print("History:")
        if len(history) == 0:
            print("No calculations yet.")
        else:
            for item in history:
                print(item)
        continue

    if operator == "12":
        history = []
        print("History cleared.")
        continue

    # TWO-NUMBER operations
    if operator in ["1", "2", "3", "4", "5", "6", "7"]:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))

    # ONE-NUMBER operations
    elif operator in ["8", "9"]:
        n1 = float(input("Enter the number: "))

    # EXIT
    elif operator == "10":
        break

    # INVALID CHOICE
    else:
        print("Invalid Operation")
        continue

    # PERFORM OPERATIONS + ADD HISTORY ENTRY
    if operator == "1":
        result = n1 + n2
        print(result)
        history.append(str(n1) + " + " + str(n2) + " = " + str(result))

    elif operator == "2":
        result = n1 - n2
        print(result)
        history.append(str(n1) + " - " + str(n2) + " = " + str(result))

    elif operator == "3":
        result = n1 * n2
        print(result)
        history.append(str(n1) + " * " + str(n2) + " = " + str(result))

    elif operator == "4":
        if n2 == 0:
            print("Invalid Operation")
        else:
            result = n1 / n2
            print(result)
            history.append(str(n1) + " / " + str(n2) + " = " + str(result))

    elif operator == "5":
        result = n1 % n2
        print(result)
        history.append(str(n1) + " % " + str(n2) + " = " + str(result))

    elif operator == "6":
        result = n1 ** n2
        print(result)
        history.append(str(n1) + " ** " + str(n2) + " = " + str(result))

    elif operator == "7":
        result = n1 // n2
        print(result)
        history.append(str(n1) + " // " + str(n2) + " = " + str(result))

    elif operator == "8":
        if n1 < 0:
            print("Invalid Operation")
        else:
            result = math.sqrt(n1)
            print(result)
            history.append("sqrt(" + str(n1) + ") = " + str(result))

    elif operator == "9":
        result = n1 ** (1/3)
        print(result)
        history.append("cbrt(" + str(n1) + ") = " + str(result))
