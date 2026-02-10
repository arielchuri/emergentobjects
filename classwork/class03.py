# calculator
#
# homework
# - error message
# - error prevention
# - user chooses calculator or counter
# - user can enter what to count from and to numbers of their choice
# - comments
# - use function calls

# var user_choice
user_choice = input("Choose: 1. Calculator or 2. Counter")

match user_choice:
    case "1":
        func_calc()
    case "2":
        counter = 0
        for i in range(1, 1000):
            print(i)
            counter = counter + 1
            print(counter)
        

def func_calc():
    # variables
    first_number = 0
    second_number = 0
    operator = 0

    print("CALCULATOR")
    # user is asked to input the first number
    # first_number = input("Enter the first number: ")
    # first_number = int(first_number)
    first_number = int(input("Enter the first number: "))
    # user is asked to input the second number
    second_number = input("Enter the second number: ")
    second_number = int(second_number)
    # user is asked to input the operator

    operator = input("Enter an operator: ")
    # calculate the answer
    match operator:
        case '+':
            answer = first_number + second_number
            print(answer)
        case '-':
            answer = first_number - second_number
            print(answer)
        case _:
            print("ERROR")

# if operator == "*":
#     answer = first_number * second_number
# elif operator == "/":
#     answer = first_number / second_number
# elif operator == "+":
#     answer = first_number + second_number
# elif operator == "-":
#     answer = first_number - second_number
# else:
#     print("ERROR")
#     exit()
# show the answer
# print(answer)
