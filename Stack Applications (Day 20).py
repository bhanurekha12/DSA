#stack applications:
#1)using files navigations
#2) undo redo operations


'''text=input("Enter the text:")
file=open("notes.txt","w")
file.write(text)
file.close()    
#undo->clears the file
ch=input("Do you want to undo the changes(y/n):")
if ch=='y':
    file=open("notes.txt","w")
    file.write("")
    file.close()
    print("Changes are undone")
#redo->restores the file
ch=input("Do you want to redo the changes(y/n):")
if ch=='y':
    file=open("notes.txt","w")
    file.write(text)
    file.close()
    print("Changes are redone")
file=open("notes.txt","r")
print("File content:",file.read())
file.close()'''

#using file navigations
'''stack=[]
file=open("browser_history.txt","r")
for website in file:
    stack.append(website.strip())
file.close()
print("Current website:",stack[-1])
while len(stack)>1:
    input("Press enter to go back to previous website:")
    stack.pop()
    print("Current website:",stack[-1])
print("No more previous websites to go back to.")'''

##a+b->+ab
#a+b*c->+a*bc
#a*b+c->+*abc

#prefix conversion:
'''def precedence(op):
    if op=='+' or op=='-':
        return 1
    elif op=='*' or op=='/':
        return 2
    elif op=='^':
        return 3
    return 0
infix=input('Enter expression: ')
infix=infix[::-1]
stack=[]
postfix=''
for ch in infix:
    if ch.isalnum():
        postfix+=ch
    else:
        while stack and precedence(stack[-1])>precedence(ch):
            postfix+=stack.pop()
        stack.append(ch)
while stack:
    postfix+=stack.pop()
prefix=postfix[::-1]
print(prefix)'''

# postfix conversion:
'''def precedence(op):
    if op=='+' or op=='-':
        return 1
    elif op=='*' or op=='/':
        return 2
    elif op=='^':
        return 3
    return 0
infix=input('Enter expression: ')
stack=[]
postfix=''
for ch in infix:
    if ch.isalnum():
        postfix+=ch
    else:
        while stack and precedence(stack[-1])>precedence(ch):
            postfix+=stack.pop()
        stack.append(ch)
while stack:
    postfix+=stack.pop()
print(postfix)'''