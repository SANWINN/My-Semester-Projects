#Saniya Winn
#11/18/2024
#Calculator

#Init


#Function
def add(num1, num2):
    answer = num1 + num2
    print(answer)
def sub(num1, num2):
    answer = num1 - num2
    print(answer)
def multi(num1, num2):
    answer = num1 * num2
    print(answer)
def div(num1, num2):
    answer = num1/num2
    print(answer)
def SimpleCalculator():
    while True:
        print("Please choose an operation!")
        print("""1. Addition
2. Subtract
3. Multiplication
4. Divison
5. Quit""")
        option = int(input("1-5: "))

        if option == 1:
            num1 = int(input("You have picked addition! Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            add(num1, num2)

        if option == 2:
            num1 = int(input("You have picked subtraction! Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            sub(num1, num2)

        if option == 3:
            num1 = int(input("You have picked multiplication! Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            multi(num1, num2)

        if option == 4:
            num1 = int(input("You have picked division! Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            div(num1, num2)

        if option == 5:
                print("Thank you for using Simple Calculator!")
                break
#Main
print("Welcome to Simple Calculator!")
SimpleCalculator()
