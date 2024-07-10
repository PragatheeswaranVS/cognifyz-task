def add(num1,num2):
    return num1 + num2 
def sub(num1,num2):
    return num1 - num2
def mul(num1,num2):
    return num1 * num2
def div(num1,num2):
    if num2 == 0:
        return "can't divide by Zero"
    return num1 / num2
def mod(num1,num2):
    return num1 % num2
while(True):
    number1 = int(input("\nenter number 1 : ")) 
    number2 = int(input("enter number 2 : "))
    operator = input("Enter the operator (For example :+,-,*,/,%) : ")
    
    if operator == "+":
        print("\nResult =",add(number1,number2))
    elif operator == "-":
        print("\nResult =",sub(number1,number2))
    elif operator == "*":
        print("\nResult =",mul(number1,number2))
    elif operator == "/":
        print("\nResult =",div(number1,number2))
    elif operator == "%":
        print("\nResult =",mod(number1,number2))
    else:
        print("\nYou entered a Invalid operator")
    choice = input("\nIf you want to close (For example :(y -> Continue operation / n -> Exit)) : ")
    if choice == "y":
        break
    elif choice == "n":
        continue
    else:
        print("Invalid choice .please enter y  or n")
    