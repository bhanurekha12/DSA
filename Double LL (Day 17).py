#DLL creation:
'''class node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None
head=None
tail=None
n = int(input("Enter the size of DLL: "))
for i in range(n):
    value = int(input(f"Enter data value: "))
    new_node = node(value)
    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        new_node.prev = tail
        tail = new_node
print("Forward traversal:")        
temp = head
while temp:
    print(temp.data, end='<->')
    temp = temp.next
print("tail")'''

#reverse DLL
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
head=None
tail=None
n=int(input("enter DLL size:"))
for i in range(n):
    value=int(input("enter a value:"))
    newnode=node(value)
    if head is None:
        head=newnode
        tail=newnode
    else:
        tail.next=newnode
        newnode.prev=tail
        tail=newnode
print("forword traversal:")        
temp = tail
while temp:
    print(temp.data, end='<->')
    temp = temp.prev
print("tail")'''

#DLL insert at end:
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
head=None
tail=None
n=int(input("enter DLL size:"))
for i in range(n):
    value=int(input("enter a value:"))
    newnode=node(value)
    if head is None:
        head=newnode
        tail=newnode
    else:
        newnode.next=head
        head.prev=newnode
        head=newnode
print("forword traversal:")
temp = head
while temp:
    print(temp.data, end='<->')
    temp = temp.next
print("tail")'''

#DLL insert at end and delete at end:
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
head=None
tail=None
n=int(input("enter DLL size:"))
for i in range(n):
    value=int(input("enter a value:"))
    newnode=node(value)
    if head is None:
        head=newnode
        tail=newnode
    else:
        newnode.next=head
        head.prev=newnode
        head=newnode
print("forword traversal:")
temp = head
while temp:
    print(temp.data, end='<->')
    temp = temp.next
print("tail")

if head is None:
    print("DLL is empty")
elif head.next is None:
    head=None
    tail=None   
else:
    tail=tail.prev
    tail.next=None
print("After delete at end:")
temp=head
while temp:
    print(temp.data, end='<->')
    temp=temp.next
print("Tail")'''   

#delete at beginning of DLL:
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
head=None
tail=None
n=int(input("enter DLL size:"))
for i in range(n):
    value=int(input("enter a value:"))
    newnode=node(value)
    if head is None:
        head=newnode
        tail=newnode
    else:
        newnode.next=head
        head.prev=newnode
        head=newnode
print("forword traversal:")
temp = head
while temp:
    print(temp.data, end='<->')
    temp = temp.next
print("tail")
if head is None:
    print("DLL is empty")
elif head.next is None:
    head=None
    tail=None
else:
    head=head.next
    head.prev=None  
print("After delete at beginning:")
temp=head
while temp:
    print(temp.data, end='<->')
    temp=temp.next
print("Tail")'''

##DLL insert at begining and delete at begining:
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
head=None
tail=None
n=int(input("enter DLL size:"))
for i in range(n):
    value=int(input("enter a value:"))
    newnode=node(value)
    if head is None:
        head=newnode
        tail=newnode
    else:
        newnode.next=head
        head.prev=newnode
        head=newnode
print("forword traversal:")
temp = head
while temp:
    print(temp.data, end='<->')
    temp = temp.next
print("tail")

if head is None:
    print("DLL is empty")
elif head.next is None:
    head=None
    tail=None   
else:
    tail=tail.prev
    tail.next=None
print("After delete at end:")
temp=head
while temp:
    print(temp.data, end='<->')
    temp=temp.next
print("Tail") '''

#DLL insert at position:
#insert at position
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

head=None
tail=None

n=int(input("enter DLL size:"))

for i in range(n):
    value=int(input("enter a value:"))
    newnode=node(value)

    if head is None:
        head=newnode
        tail=newnode
    else:
        newnode.next=head
        head.prev=newnode
        head=newnode
print("Before inserting:")
temp=head
while temp:
    print(temp.data, end="<->")
    temp=temp.next
print("tail")

pos=int(input("enter position to insert:"))
val=int(input("enter value to insert:"))

newnode=node(val)

if pos==1:
    newnode.next=head
    if head is not None:
        head.prev=newnode
    head=newnode
else:
    temp=head
    for i in range(pos-2):
        temp=temp.next

    newnode.next=temp.next

    if temp.next is not None:
        temp.next.prev=newnode

    newnode.prev=temp
    temp.next=newnode

print("After inserting at position:")
temp=head
while temp:
    print(temp.data, end="<->")
    temp=temp.next
print("tail")'''


    

