
from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide

while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print()
        print("Choose Operation")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = input("Enter your choice: ")
        if choice == "1":
         print("Answer =", add(num1, num2))

        elif choice == "2":
            print("Answer =", subtract(num1, num2))

        elif choice == "3":
            print("Answer =", multiply(num1, num2))

        elif choice == "4":
          print("Answer =", divide(num1, num2))

        else:
            print("Invalid Choice")
        print()
        print("Do you want another calculation?")
        print("1. Yes")
        print("2. Exit")

        again = input("Enter your choice: ")
        if again=="2":
           print("Thankyou for using Calculator")
           break
    except ValueError:
        print("Please enter only numbers.")