operators = ['+', '-', '/', '//', '*', '**', '%']


def calculator(num1, num2, operator):
    if operator not in operators:
        return "Invalid operator"
    elif operator == '+':
        return num1 + num2
    elif operator == '-':
        return num2 - num1
    elif operator == '/':
        return num1 / num2
    elif operator == '//':
        return num1 // num2
    elif operator == '*':
        return num1 * num2
    elif operator == '**':
        return num1 ** num2
    elif operator == '%':
        return num1 % num2


if __name__ == "__main__":
    num1 = float(input())
    operator = input()
    num2 = float(input())
    result = calculator(num1, num2, operator)
    print(f"Result: {result}")
