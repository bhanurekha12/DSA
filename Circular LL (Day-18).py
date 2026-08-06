#circular LL operations insert at end:
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
tail=None
n=int(input("enter CLL size:"))
for i in range(n):
    data=int(input("enter size of CLL:"))
    newnode=node(data)
    if head is None:
        head=newnode       
        tail=newnode
        tail.next=head
    else:
        tail.next=newnode
        tail=newnode
        tail.next=head
print("Circular Lniked List")
temp=head
while temp.next != head:
    print(temp.data, end='->')
    temp=temp.next
print(temp.data, end= '->')
print(head.data)'''

#Circular LL operations insert at begining:
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
tail=None
n=int(input("enter CLL size:"))
for i in range(n):
    data=int(input("enter size of CLL:"))
    newnode=node(data)
    if head is None:
        head=newnode       
        newnode.next=head
    else:
        temp=head
        while temp.next !=head:
            temp=temp.next
        newnode.next=head
        temp.next=newnode
        head=newnode
print("Circular Linked List")
temp=head
while temp.next != head:
    print(temp.data, end='->')
    temp=temp.next
print(temp.data, end= '->')
print(head.data)'''

#insert at end-delete at begining:
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
tail=None
n=int(input("Enter the size of CLL:"))
for i in range(n):
    data=int(input("Enter value:"))
    newnode=node(data)
    if head is None:
        head=newnode
        tail=newnode
        tail.next=head
    else:
        tail.next=newnode
        tail=newnode
        tail.next=head
print("Circular Linked List")
temp=head
while temp.next!=head:
    print(temp.data,end='->')
    temp=temp.next
print(temp.data,end='->')
print(head.data)
if head is None:
    print("CLL is empty")
elif head.next==head:
    head=None
else:
    temp=head
    while temp.next!=head:
        temp=temp.next
    temp.next=head.next
    head=head.next
print("Circular Linked List after deletion")
temp=head
while temp.next!=head:
    print(temp.data,end='->')
    temp=temp.next
print(temp.data,end='->')
print(head.data)'''

##insert at end-delete at end
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
tail=None
n=int(input("Enter the size of CLL:"))
for i in range(n):
    data=int(input("Enter value:"))
    newnode=node(data)
    if head is None:
        head=newnode
        tail=newnode
        tail.next=head
    else:
        tail.next=newnode
        tail=newnode
        tail.next=head
print("Circular Linked List")
temp=head
while temp.next!=head:
    print(temp.data,end='->')
    temp=temp.next
print(temp.data,end='->')
print(head.data)
if head is None:
    print("CLL is empty")
elif head.next==head:
    head=None
else:
    temp=head
    while temp.next.next!=head:
        temp=temp.next
    temp.next=head
print("Circular Linked List after deletion")
temp=head
while temp.next!=head:
    print(temp.data,end='->')
    temp=temp.next
print(temp.data,end='->')
print(head.data)'''

