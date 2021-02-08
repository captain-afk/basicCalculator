def add(numberOne,numberTwo):
    numberSum = float(numberOne) + float(numberTwo)
    return(numberSum)

def subtract(numberOne,numberTwo):
    difference = float(numberOne) - float(numberTwo)
    return(difference)

def multiply(numberOne, numberTwo):
    product = float(numberOne) * float(numberTwo)
    return(product)

def divide(numberOne, numberTwo):
    quotient = float(numberOne) / float(numberTwo)
    return(quotient)


def main():
    continueCalculation = True
    print("Welcome to the calculator")
    print("What is the first number?")
    numberOne = input()
    while continueCalculation == True:      # This loop allows the user to continue the calculation. The first number is simply replaced with the result of the previous calculation
        print("what function would you like to preform: add(+), subtract(-), multiply(*), divide(/) ?")
        function = input()
        print("What is the second number?")
        numberTwo = input()

        if function == '+':
            result = add(numberOne,numberTwo)
        elif function == '-':
            result = subtract(numberOne,numberTwo)
        elif function == '*':
            result = multiply(numberOne,numberTwo)
        elif function == '/':
            result = divide(numberOne,numberTwo)

        print(f"{numberOne} {function} {numberTwo} = {result}")
        print("Would you like to carry on with the calculation? y/n")
        userContinues = input()
        if userContinues == 'n':
            continueCalculation = False
            print("Okay bai!")
        numberOne = result

main()