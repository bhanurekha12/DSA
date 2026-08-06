#stacks its a linear DS follows last in first out (LIFO) 
#stack of books
#stack of biscuits
#stack operation

#push - insert an element at the top of the stack  #append
#pop - remove an element from the top of the stack #pop
#peek - return the top element of the stack without removing it  #stack[-1]
#overflow - when stack is full and we try to push an element
#underflow - when stack is empty and we try to pop an element (#isempty)

#stack operations-insert
'''class stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
        print("Stack after push operation:",self.stack)
s=stack()
n=int(input("Enter the size of stack:"))
for i in range(n):
    val=int(input("Enter the value to push:"))
    s.push(val)'''

#stack operations-delete
'''class stack:
    def __init__(self):
        self.stack=[]
    def pop(self):
        if len(self.stack)==0:
            print("Stack is empty")
        else:
            item=self.stack.pop()
            print("Stack after pop operation:",item)
            print("Stack after pop operation:",self.stack)
s=stack()
n=int(input("Enter the size of stack:"))
for i in range(n):
    val=int(input("Enter the value to push:"))
    s.stack.append(val)
s.pop()'''

#stack operations-max range
'''class stack:
    def __init__(self):
        self.stack=[]
        self.max_size=5
    def pop(self):
        if len(self.stack)==0:
            print('Stack is empty.....')
        else:
            print('Deleted element: ',self.stack.pop())
            print('Stack after pop: ',self.stack)
    def push(self,item):
        self.stack.append(item)
        print('Stack after push: ',self.stack)
s=stack()
while True:
    if len(s.stack)==s.max_size:
        print('Stack overflow.......')
        break
    n=int(input('Enter value: '))
    s.stack.append(n)
    ch=input('Do you add another value(y/n): ')
    if ch.lower()=='n':
        break
print('Stack: ',s.stack)
s.pop()
s.pop()
print('Peek element: ',s.stack[-1])'''