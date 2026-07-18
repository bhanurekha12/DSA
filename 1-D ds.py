'''n=int(input("enter a number:"))
while n!=0:             #n>0
    digit=n%10
    print(digit)
    n//=10
print(n)'''

#write a code to print sum of digits of a number:

'''n=int(input("enter a number:"))
sum=0
while n!=0:             #n>0
    digit=n%10
    sum+=digit
    n//=10
print(sum)'''

#write a code to print sum of series:
'''n=int(input("enter a number:")) #n=5
sum=0
i=1
while i<=n:
    sum+=i/(i+1)
    i+=1
print(sum)'''

#7,6,14,12,21,18,28,24,35....    find 14th term
'''n=int(input("enter a number:"))
s=[]
c=0
for i in range(1,n):
    if c==14:
        break
    else:
        s.append(7*i)
        c+=1
        s.append(6*i)
        c+=1
print(s[-1])'''




































  
