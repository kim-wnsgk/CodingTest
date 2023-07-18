def calculate_postfix(expression, values):
    stack = []

    for char in expression:
        if char.isalpha():
            stack.append(values[ord(char) - ord('A')])
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = evaluate_expression(operand1, operand2, char)
            stack.append(result)

    return stack[0]

def evaluate_expression(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2

# 입력 처리
N = int(input())
postfix_expression = input().strip()
values = []
for _ in range(N):
    values.append(int(input()))

# 후위 표기식 계산
result = calculate_postfix(postfix_expression, values)
print("{:.2f}".format(result))

