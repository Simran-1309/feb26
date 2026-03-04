class Calculator:
    def __init__(self, num1, operation, num2):
        self.num1 = num1
        self.operation = operation
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        if self.num2 == 0:
            return "Error: Division by zero is not allowed."
        return self.num1 / self.num2

def main():
    while True:
        print("/nSimple Calculator")
        choice = input("Q=> quit or press enter: ")
        if choice.lower() == "q":
            print("Goodbye")
            exit()
        num1 = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, /, *): ")
        num2 = float(input("Enter second number: "))
        calculator = Calculator(num1, operation, num2)

        if calculator.operation == "+":
            result = calculator.add()
        elif calculator.operation == "-":
            result = calculator.subtract()
        elif calculator.operation == "*":
            result = calculator.multiply()
        elif calculator.operation == "/":
            result = calculator.divide()
        
        else:
            result = "Invalid operation"
        print(f"Result = {result}")

if __name__ == "__main__":
    main()
