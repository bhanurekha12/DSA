#traverse a circular queue
queue=[]
size=int(input("Enter size of queue: "))
for i in range(size):
    value=int(input("Enter element: "))
    queue.append(value)
start=int(input("enter the rotation point to start: "))
index=queue.index(start)
print("Circular Queue:  ",end=' ')
for i in range(size):
    print(queue[(index+i)%size], end=' ')
