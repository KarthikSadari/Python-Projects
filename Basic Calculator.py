logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
import os
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def rem(a,b):
    return a%b

operators = {
    '+':add,
    '-':sub,
    '*':mul,
    '/':div,
    '%':rem
}
def calculator():
    number1 = float(input("Enter first number: "))
    continue_flag = True
    while continue_flag:
        for symbol in operators:
            print(symbol)
        operator = input("Enter the Operator you want: ")
        number2 = float(input("Enter second number: "))
        calculation_function = operators[operator]
        output_fun = calculation_function(number1,number2)
        print(f"{number1} {operator} {number2} = {output_fun}")
        
        should_continue = input(f"Press y to continue with {output_fun} or press n to start new calculation or press x to exit :---> ")
        if should_continue == 'y':
            number1 = output_fun
        elif should_continue == 'n':
            continue_flag = False
            os.system('cls')
            calculator()
        else:
            continue_flag = False
            print("Thank You for Using Calculator")
calculator()
        
