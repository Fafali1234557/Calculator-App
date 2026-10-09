def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

first_number = float(input("What's the first number?: "))
print("Please select operations form the following: ")
for operation in operations:
    print(operation)
selected_operation = input("Pick an operation: ")
if operations.get(selected_operation) is None:
    print("Invalid operation selected. Please try again.")

elif operations.get(selected_operation) is not None:
    second_number = float(input("What's the second number?: "))
    calculation_function = operations[selected_operation]
    answer = calculation_function(first_number, second_number)
    print(f"{first_number} {selected_operation} {second_number} = {answer}")
    continue_calculation = input("Do you want to continue calculating with the answer? Type 'yes' or 'no'.")
    if continue_calculation.lower() == "yes":
        while True:
            selected_operation = input("Pick another operation: ")
            if operations.get(selected_operation) is None:
                print("Invalid operation selected. Please try again.")
                break
            elif operations.get(selected_operation) is not None:
                next_number = float(input("What's the next number?: "))
                calculation_function = operations[selected_operation]
                new_answer = calculation_function(answer, next_number)
                print(f"{answer} {selected_operation} {next_number} = {new_answer}")
                answer = new_answer
                continue_calculation = input("Do you want to continue calculating with the answer? Type 'yes' or 'no'.")
                if continue_calculation.lower() == "no":
                    break
