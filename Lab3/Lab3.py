import math

""" --- Global variables --- """
user_Input = None
current_Result = 0.0
sum_Of_Calculations = 0
num_Of_Calculations = 0
first_Operand = 0
second_Operand = 0

"""
Helper Functions
"""


def get_user_input(last_user_input):
    if last_user_input != 7:
        print("Calculator Menu", "---------------", "0. Exit Program", "1. Addition", "2. Subtraction",
              "3. Multiplication", "4. Division",
              "5. Exponentiation", "6. Logarithm", "7. Display Average", sep="\n", end="\n\n")

    user_input = int(input("Enter Menu Selection: "))

    while user_input < 0 or user_input > 7:
        print("Error: Invalid selection!", end="\n\n")
        user_input = int(input("Enter Menu Selection: "))

    return user_input


def display_results(current_result):
    print("Current Result: ", current_result, end="\n")


def display_average(sum_of_calculations, num_of_calculations):
    if num_of_calculations == 0:
        print("Error: No calculations yet to average!", end="\n\n")
    else:
        print("Sum of calculations:", sum_of_calculations, end="\n")
        print("Number of calculations:", num_of_calculations, end="\n")
        print("Average of calculations:", round(sum_of_calculations / num_of_calculations, 2), end="\n\n")


def handle_operand_input(operand, current_result):
    if operand.upper() == "RESULT":
        return current_result
    else:
        return float(operand)


"""
MAIN LOOP
"""

print("Current Result:", current_Result, end="\n\n")
user_Input = get_user_input(user_Input)

while user_Input:
    if user_Input == 7:
        display_average(sum_Of_Calculations, num_Of_Calculations)
    else:

        first_Operand = input("Enter first operand: ")
        first_Operand = handle_operand_input(first_Operand, current_Result)

        second_Operand = input("Enter second operand: ")
        second_Operand = handle_operand_input(second_Operand, current_Result)

        if user_Input == 1:
            current_Result = first_Operand + second_Operand
        elif user_Input == 2:
            current_Result = first_Operand - second_Operand
        elif user_Input == 3:
            current_Result = first_Operand * second_Operand
        elif user_Input == 4:
            current_Result = first_Operand / second_Operand
        elif user_Input == 5:
            current_Result = first_Operand ** second_Operand
        else:
            current_Result = math.log(second_Operand, first_Operand)

        sum_Of_Calculations += current_Result
        num_Of_Calculations += 1
        print("Current Result:", round(current_Result, 2), end="\n\n")

    user_Input = get_user_input(user_Input)
print("Thanks for using this calculator. Goodbye!")
