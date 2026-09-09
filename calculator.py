# Command-Line Calculator
# This program allows the user to perform basic mathematical calculations.
# The calculator supports addition, subtraction, multiplication and division.
# The program continues running until the user chooses to exit.

import os


# This function adds two numbers and returns the answer.
def add(num1, num2):
    return num1 + num2


# This function subtracts the second number from the first number.
def subtract(num1, num2):
    return num1 - num2


# This function multiplies two numbers and returns the answer.
def multiply(num1, num2):
    return num1 * num2


# This function divides the first number by the second number.
def divide(num1, num2):
    # Check that the user is not trying to divide by zero.
    if num2 == 0:
        return "Error: Cannot divide by zero."

    return num1 / num2


# This function clears the command-line output.
def clear_screen():
    # Use "cls" on Windows and "clear" on macOS/Linux.
    os.system("cls" if os.name == "nt" else "clear")


# The sentinel variable controls whether the calculator keeps running.
running = True


# The while loop keeps the calculator running until running becomes False.
while running:

    print("\nCommand-Line Calculator")
    print("-----------------------")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Clear output")
    print("6. Exit")

    # Ask the user to select an option from the menu.
    choice = input("\nChoose an option (1-6): ")

    # Exit the loop when the user selects option 6.
    if choice == "6":
        running = False
        print("Goodbye!")

    # Clear the command-line output when the user selects option 5.
    elif choice == "5":
        clear_screen()

    # Perform a calculation if the user selects options 1 to 4.
    elif choice in ["1", "2", "3", "4"]:

        # Ask the user for the two numbers used in the calculation.
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Call the correct mathematical function.
        if choice == "1":
            result = add(num1, num2)

        elif choice == "2":
            result = subtract(num1, num2)

        elif choice == "3":
            result = multiply(num1, num2)

        elif choice == "4":
            result = divide(num1, num2)

        # Display the answer to the user.
        print("Result:", result)

    # Display an error if the user enters an invalid menu option.
    else:
        print("Invalid option. Please choose a number from 1 to 6.")