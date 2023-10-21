# Реализуйте функцию rpn_calc, которая принимает список, каждый элемент которого содержит число или знак операции (+, -, *, /). Функция должна вернуть результат вычисления по обратной польской записи.

# Примеры
# rpn_calc([1, 2, '+', 4, '*', 3, '+'])  # 15
# rpn_calc([7, 2, 3, '*', '-'])  # 1

def rpn_calc(tokens):
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if isinstance(token, (int, float)):
            stack.append(token)
        elif token in operators:
            if len(stack) < 2:
                raise ValueError("Not enough operands for operator")
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                if operand2 == 0:
                    raise ValueError("Division by zero")
                result = operand1 / operand2
            stack.append(result)
        else:
            raise ValueError("Invalid token: " + str(token))

    if len(stack) == 1:
        return stack[0]
    else:
        raise ValueError("Invalid expression")

# Примеры использования:
result1 = rpn_calc([1, 2, '+', 4, '*', 3, '+'])  # Ожидаемый результат: 15
result2 = rpn_calc([7, 2, 3, '*', '-'])  # Ожидаемый результат: 1

print(result1)
print(result2)
