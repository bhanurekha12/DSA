#Types of searches:(arays/list)
#1 linear search (sorted/unsorted)
#2 binary search(sorted)
#3 jump search (sorted)

#binary search:
'''arr=list(map(int,input("Enter elements: ").split()))
target=int(input("Enter element to be searched: "))
left=0
right=len(arr)-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        print("Element found at index: ",mid)
        break
    elif target<arr[mid]:
        right=mid-1
    else:
        left=mid+1
else:
    print("Element not in array.. ")'''


#jump search:
'''arr=list(map(int,input("Enter elements: ").split()))
target=int(input("Enter element to be searched: "))
n=len(arr)
step=int(n**0.5)
i=0
while i<n and arr[min(i+step, n)-1]<target:
    i+=step
found=  False
for j in range(i,min(i+step, n)):
    if arr[j]==target:
        print("Element found at index",j)
        found=True
        break
if not found:
    print("Element not in array..")'''