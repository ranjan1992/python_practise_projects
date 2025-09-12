def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def division(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x/y


def main():
    print("\n==== Simple Calculator ====")
    print("Select operation:")
    print("1. + Addition")
    print("2. - Subtraction")
    print("3. * Multiplication")
    print("4. / Division")

    while True:
        choice = input("\n Enter choice(1-4)")
        if choice not in ["1", '2', '3', "4"]:
            print("Invalid input. Please enter a num between 1 and 4")
        else:
            break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second numner: "))

    except ValueError:
        print("Error! Please enter valid numbers")

    if choice == "1":
        print(f"\n {num1} + {num2} = {add(num1, num2)}")

    if choice == "2":
        print(f"\n {num1} - {num2} = {subtract(num1, num2)}")
    if choice == "3":
        print(f"\n {num1} * {num2} = {multiply(num1, num2)}")
    if choice == "4":
        print(f"\n {num1} / {num2} = {division(num1, num2)}")

    again = input(
        "Do you want to perform another calculation? (yes/no): ").lower()

    if not again.startswith("y"):
        print("👋 Goodbye!")
    else:
        main()


main()
