first_number = float(input("Enter a number: "))
operator = input("Enter a operator(+, -,/, *): ")
second_number = float(input("Enter another number: "))
if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number != 0:
        result = first_number / second_number
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operator."
print("Result:",result)