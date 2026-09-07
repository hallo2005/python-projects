print("Welcome to the Calculator App!")
play_again = "Yes"
while play_again.lower() == "yes":
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")
    if operation == "+":
        print(num_1 + num_2)
    elif operation == "-":
        print(num_1 - num_2)
    elif operation == "*":
        print(num_1 * num_2)
    elif operation == "/":
        print(num_1 / num_2)
    else:
        print("Invalid operation. Please choose +, -, *, or /.")
    play_again = input("Do you want to perform another calculation? (yes/no): ")
