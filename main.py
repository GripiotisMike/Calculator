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

def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def multi(x, y):
    return x * y


def div(x, y):
    return x / y


operations = {"+": plus, "-": minus, "*": multi, "/": div}


def calculator():
    print(logo)
    f = True

    x = float(input("What is the.kugthsdtjhj 1st number? : "))
    for i in operations:
        print(i)
    oper = input("Pick an operation from above: ")
    y = float(input("What is the 2nd number? : "))
    what = operations[oper]
    first_answer = what(x, y)
    print(f"{x} {oper} {y} = {first_answer}")
    while x:
        k = input(f"Type 'y' to continue operating with {first_answer}, or type 'n' to start a new calculation.")
        if k == "y":
            oper = input("What operation you wanta do : ")
            z = float(input("What is the next number ? : "))
            what = operations[oper]
            second_answer = what(first_answer, z)
            print(f"{first_answer} {oper} {z} = {second_answer}")
            first_answer = second_answer
        else:
            f = False
            calculator()

calculator()
