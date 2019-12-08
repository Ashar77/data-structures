user_input = input('enter infix expression: ')

infix = []

for i in user_input:
    infix.append(i)



stack = []
postfix = ''
operators = ['+','-','*','/','^','(',')']
highest_precedence = ['^']
higher_precedence = ['*','/']
lower_precedence = ['+','-']
associativity_L_R = ['+','-','*','/'] 
associativity_R_L = ['^']

for i in infix:
    if i not in operators:
        postfix+=i
    
    elif i in operators:
        while True:
             if len(stack)==0 or stack[-1]=='(':
                stack.append(i)
                break

             elif infix[infix.index(i)-1] == '(':
                postfix += i
                break 

             elif i == ')':
                for j in stack:
                    while j != '(':
                        stack.pop()
                        postfix += j
                        break
             
             elif (len(stack)==0) or (((i in highest_precedence) and (stack[-1] in lower_precedence or stack[-1] in higher_precedence )))or(i in higher_precedence and stack[-1] in lower_precedence):
                stack.append(i)
                break
            
             
             elif (len(stack)==0) or (((i in lower_precedence) and (stack[-1] in higher_precedence or stack[-1] in highest_precedence )))or(i in higher_precedence and stack[-1] in highest_precedence):
                postfix+=stack.pop()
                
             elif (len(stack)==0) or (i in lower_precedence and stack[-1] in lower_precedence)or(i in higher_precedence and stack[-1] in higher_precedence)or(i in highest_precedence and stack[-1] in highest_precedence):
                 if i in associativity_L_R:
                     postfix+=stack.pop()
                     stack.append(i)
                     break

                 elif i in associativity_R_L:
                     stack.append(i)
                     break
                
while len(stack)!=0:
    pop_till_empty = stack.pop()
    postfix+=pop_till_empty

                 
final_postfix = ""
for i in postfix:
    if i !='(' and i!=')':
        final_postfix += i 


print('your postfix expression is:',final_postfix)






