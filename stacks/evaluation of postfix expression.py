postfix = input('enter your postfix expression for evaluation: ')

operators = ['+','-','*','/','^']

stack = []

for i  in postfix:
    if i not in operators:
        operand = int(i)
        stack.append(operand)

    elif i in operators:
        a = stack.pop()
        b = stack.pop()

        if i == '+':
           result = b + a
           stack.append(result)

        if i == '-':
            result = b-a
            stack.append(result)
        if i == '*':
            result = b*a 
            stack.append(result)
        if i == '/':
            result = b/a
            stack.append(result)
        if i=='^':
            result = b**a 
            stack.append(result)

answer = stack.pop() 

print(int(answer))
