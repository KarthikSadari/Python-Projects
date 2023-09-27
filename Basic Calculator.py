logo = """
 _____________________
|  _________________  |
| | Python       0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
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

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
def rem(n1,n2):
    return n1%n2

operations = {
                '+':add,
                '-':sub,
                '*':mul,
                '/':div,
                '%':rem
             }

def cal():
    
    num1 = float(input("\nenter the first number: "))


    for symbol in operations:
        print(symbol)

        should_continue = True

    while should_continue :
        operation_symbol = input("choose ur operator : ")

        num2 = float(input("enter the next number: "))

        calculation_function = operations[operation_symbol]

        answer = calculation_function(num1,num2)

        print(f'\nthe solution is {num1} {operation_symbol} {num2} = {answer}')

        ask=input("enter Y to continue calculation or N to new calculator: ").lower()

        if ask == 'y':
            num1 = answer
        else:
            should_continue = False
            cal()
cal()
