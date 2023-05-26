# calculators

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
def calc():
    num1 = int(input('What is your first number?\n'))
    for symbols in operations:
        print(symbols)

    should_continue = True

    while should_continue:
        operations_symbol = input("What do you choose?\n")
        num2 = int(input('What is your next number?\n'))
        function = operations[operations_symbol]
        answer = function(num1, num2)
        print(f"{num1} {operations_symbol} {num2} = {answer}")
        choice = input(f"{answer} with calculate another time, 'yes' or 'no' or 'restart'.\n")
        if choice == 'yes':
            num1 = answer
        elif choice == 'no':
            should_continue = False
        else:
            should_continue = False
            calc()
calc()

