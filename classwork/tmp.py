# calculator

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
