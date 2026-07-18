#program to print a  hollow square pattern with diagonals

'''n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==j or i+j==n-1:
            print("*",end=" ")
        else:
                print(" ",end=" ")
    print()'''

#print empty square :

'''n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
                print(" ",end=" ")
    print()'''

# print a square:
'''n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()'''

#hourglass:
'''n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if  i==0 or i==n-1 or  i==j or i+j==n-1:
            print("*",end=" ")
        else:
                print(" ",end=" ")
    print()'''


# print plus:
'''n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:
            print("*",end=" ")
        else:
                print(" ",end=" ")
    print()'''


#butterfly:
'''n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if   j==0 or  j==n-1 or i==j or i+j==n-1:
            print("*",end=" ")
        else:
                print(" ",end=" ")
    print()'''

#multiply:
'''n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if  i==j or i+j==n-1:
            print("*",end=" ")
        else:
                print(" ",end=" ")
    print()'''

#  hallow right angled triangle:
'''n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 or i==j:
            print("*",end=" ")
        else:
                print(" ",end=" ")
    print()'''

# hallow reverse right angles triangle:
'''n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==n-1 or j==n-1 or i+j==n-1:
            print("*",end=" ")
        else:
                print(" ",end=" ")
    print()'''

#right tilted triangle:
'''n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0  or i+j==n-1:
            print("*",end=" ")
        else:
                print(" ",end=" ")
    print()'''

#left tilted triangle:
'''n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0  or j==n-1 or i==j :
            print("*",end=" ")
        else:
                print(" ",end=" ")
    print()'''

#T :
'''n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2:
            print("*",end=" ")
        else:
                print(" ",end=" ")
    print()'''

#program to print a right angled triangle:
'''n=int(input("Enter size:"))
for i in range(n):
    for j in range(i):
        print("*", end=' ')
    print()
print()'''

# inverted rightangled traingle:
'''n=int(input("enter size:"))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=' ')
    print()'''

