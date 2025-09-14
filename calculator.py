first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))
operator = input("Choose mathematical operator (+, -, *, /): ")

if operator == "+":
    result = first_num + second_num
elif operator == "-":
    result = first_num - second_num
elif operator == "*" or operator.lower() == "x":
    result = first_num * second_num
elif operator == "/":
    if second_num != 0:
        result = first_num / second_num
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation"

print(f"{first_num} {operator} {second_num} = {result}")
