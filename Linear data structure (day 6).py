#Reverse an array without slicing: O(n/2),O(1)
'''arr=list(map(int, input("Enter numbers:").split()))
left=0
right= len(arr)-1
while left<right:
    arr[left], arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print("reversed array",*arr)'''

# Left Rotate an array by one:1 2 3 4 5->2 3 4 5 1(clock wise)
'''arr=list(map(int,input("Enter Values: ").split()))
temp=arr[0]
for i in range(len(arr)-1):
    arr[i]=arr[i+1]
arr[-1]=temp
print(*arr)'''


