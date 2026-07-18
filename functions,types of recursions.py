#argmnt pass,return value: O(1)/O(1)
'''def summate(a,b):
    return a+b
num1=int(input("enter a value:"))
num2=int(input("enter b value:"))
result=summate(num1,num2)
print("Sum:", result)'''

#argmnt pass, no return value:O(1)/O(1)
'''def summate(a,b):
   print("Sum: ", a+b)
num1=int(input("enter a value:"))
num2=int(input("enter b value:"))
summate(num1,num2)'''

#no argmnt,but return value:O(1)/O(1)
'''def summate():
    num1=int(input("enter a value:"))
    num2=int(input("enter b value:"))
    return num1+num2
print("Sum: ",summate())'''

#no argmnt,no return value:O(1)/O(1)
'''def summate():
    num1=int(input("enter a value:"))
    num2=int(input("enter b value:"))
    print("Sum:",num1+num2)
summate()'''

#types of recursions:
#1 direct recursion:O(n)/O(n)
'''def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
n=int(input("enter a value"))
print(fact(n))'''

#2 indirect recursion: numbere is even or odd without modulus. O(n+1)/O(n)
'''def even(n):
    if n==0:
      return True
    return odd(n-1)
def odd(n):
  if n==0:
    return False
  return even(n-1)
n=int(input("enter a value:"))
print(even(n))'''

#3 Tail recursion:O(n+1)/O(n)
'''def num(n):
    if n==0:
        return
    print(n, end='-')
    num(n-1)
n=int(input("Enter a value:"))
num(n)'''

 



    

    
