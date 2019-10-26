print("Hello, this is a calculator!")

while True:

    x = float(input("Enter an x value: "))
    y = float(input("Enter an y value: "))
    operation = input("Enter a math operation (+, -, * or /): ")

    if operation == "+":
        print(x + y)
    elif operation == "-":
        print(x - y)
    elif operation == "*":
        print(x * y)
    elif operation == "/":
        print(x / y)
    else:
        print("You did not enter a valid math operation.")

    end = input("Do you want to do another calculation? ")

    if end != "yes":
        break
