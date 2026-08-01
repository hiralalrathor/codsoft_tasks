x = int(input("Enter the first  number: "))
y = int(input("Enter the second number: "))
opration = input("Enter the operation (+, -, *, /): ")
if opration == "+":
    result = x + y
    print(f"The sum of {x} and {y} is: {result}")
elif opration == "-":
    result = x - y
    print(f"The difference between {x} and {y} is: {result}")
elif opration == "*":
    result = x * y
    print(f"The product of {x} and {y} is: {result}")
elif opration == "/":
    if y != 0:
        result = x / y
        print(f"The quotient of {x} and {y} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of the following: +, -, *, /.")
