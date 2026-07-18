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
#1 direct recursion
'''def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
n=int(input("enter a value"))
print(fact(n))'''

    

    
