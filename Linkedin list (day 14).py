#insert at end:
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

head = node(10)
second = node(20)
third = node(30)

head.next = second
second.next = third

temp = head
while temp:
    print(temp.data, end='->')
    temp = temp.next
print("tail")'''



#insert to begin
'''class node:
    def __init__(self, data):
        self.data=data
        self.next=None
head=None
n= int(input("Enter SLL size: "))
for i in range(n):
    val=int(input("enter value: "))
    newnode=node(val)
    newnode.next=head
    head=newnode
temp=head
while temp:
    print(temp.data, end='->')
    temp=temp.next
print("tail")'''

#insert and begin-delete at end
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("enter SLL size:"))
for i in range(n):
    val=int(input("enter value:"))
    newnode=node(val)
    newnode.next=head
    head=newnode
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("tail")
if head is None:
    print('SLL Empty')
elif head.next is None:
    head=None
else:
    temp=head
    while temp.next.next:
        temp=temp.next
    temp.next=None
print('\nAfter deletion at end: ')
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print('tail')'''

#delete from begining:
'''if head is None:
    print("SLL Empty...")
else:
    head=head.next
print("\n after delete from begining... ")
temp=head
while temp:
    print(temp.data, end='->')
    temp=temp.next
print("tail")'''


#insert by position:
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
tail=None
n=int(input('Enter SLL size: '))
for i in range(n):
    val=int(input('Enter value: '))
    newnode=node(val)
    if head is None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode
        tail=newnode
pos=int(input('Enter position: '))
val=int(input('Enter value: '))
newnode=node(val)
if pos==1:
    newnode.next=head
    head=newnode
else:
    temp=head
    for i in range(pos-2):
        temp=temp.next
    newnode.next=temp.next
    temp.next=newnode
print('\nAfter insertion at begin: ')
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print('tail')'''
