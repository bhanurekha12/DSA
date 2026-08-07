#1)check the parenthses are balanced or not   (())()
#2)balance the unbalanced parentheses (()-(())-()(-()()
#3)remove the unbalanced parentheses (()-()

#check the expression is balanced or not
'''expression=input('Enter expresssion: ')
stack=[]
balanced =True
for ch in expression:
    if ch in '({[':
        stack.append(ch)
    elif ch in ')}]':
        if len(stack)==0:
            balanced=False
            break
        top=stack.pop()
        if (ch==')' and top!='(' or ch=='}' and top!='{' or ch==']' and top!='['):
            balanced=False
if len(stack)!=0:
    balanced=False
if balanced:
    print('Paranthesis is balanced')
else:
    print('Paranthesis is unbalanced')'''

#balance the unbalance parenthesis
'''expression=input('Enter expresssion: ')
stack=[]
result='' 
for ch in expression:
    if ch=='(':
        stack.append(ch)
        result+=ch
    elif ch==')':
        if stack:
            stack.pop()
        result+=ch
        else:
            result+='('+')'
    else:
        result+=ch
while stack:
    stack.pop()
    result+=')'
print("Balances expression:",result)'''

# another method of balnce the unbalanced parenthesis:
'''expression=input("Enter an expression: ")
stack=[]
result=""
prefix=''
for ch in expression:
    if ch == '(':
        stack.append(ch)
        result+=ch
    elif ch == ')':
        if stack:
            stack.pop()
        else:
            prefix+='('
            result+=ch
    else:
        result+=ch
while stack:
    stack.pop()
    result+=')'
print("Balanced expression:",prefix+result)'''


