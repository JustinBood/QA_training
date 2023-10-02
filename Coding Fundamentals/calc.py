num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

while True:
    op =  input("Would you like to add (+) subtract (-) Multiply (*) divide (/) or square (s)? ")
    if op == "+":
        print(num1 + num2)
        break
    elif op == "-":
        print(num1 - num2)
        break
    elif op == "*":
        print(num1 * num2)
        break
    elif op == "/":
        print(num1 / num2)
        break
    elif op == "s":
        print(num1 ** num2)
        break
    else:
        print("Your command wasnt recognised")