#integer square pattern using binary search pattern:
'''n=int(input("Enter a number: "))
left=0
right=n
ans=0
while left<=right :
    mid=(left+right)//2
    if mid * mid ==n:
        ans=mid
        break
    elif mid * mid < n:
        ans=mid
        left=mid+1
    else:
        right=mid-1
print("integer square root: ",ans)'''



 #rotational count using binary search patterns:
'''arr=list(map(int, input("Enter elements: ").split()))
left=0
right=len(arr)-1
while left<right:
   mid=(left +right)//2
   if arr[mid]>arr[right]:
      left=mid+1
   else:
     right=mid
print("rotational count", left)'''


