def basic_calculator():
    print("Welcome to the Basic Calculator!")
    
    try:
        first_number = float(input("Please enter the first number: "))
        second_number = float(input("Please enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numeric values.")
        return

    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation_choice = input("Select an option (1/2/3/4): ")

    if operation_choice == '1':
        result = first_number + second_number
        operation_symbol = '+'
    elif operation_choice == '2':
        result = first_number - second_number
        operation_symbol = '-'
    elif operation_choice == '3':
        result = first_number * second_number
        operation_symbol = '*'
    elif operation_choice == '4':
        if second_number == 0:
            print("Error: Division by zero is not permitted.")
            return
        result = first_number / second_number
        operation_symbol = '/'
    else:
        print("Error: Invalid operation selected.")
        return

    print(f"The result of {first_number} {operation_symbol} {second_number} is {result}")

if __name__ == "__main__":
    basic_calculator()
