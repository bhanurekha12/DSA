#flip sort/pankcake sort
'''arr=list(map(int,input("enter elements: ").split()))
def flip(arr, k):
    left=0
    right=k
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
n=len(arr)
for curr_size in range(n,1,-1):
    max_index=0
    for i in range(1,curr_size):
        if arr[i]>arr[max_index]:
            max_index=i
    if max_index != curr_size-1:
        flip(arr,max_index)
        flip(arr,curr_size-1)
print(*arr)  '''

#quick sort:
def part(arr,low,high):
    piv=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<piv:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quick_sort(arr,low,high):
    if low<high:
        piv=part(arr,low,high)
        quick_sort(arr,low,piv-1)
        quick_sort(arr,piv+1,high)
arr=list(map(int,input("enter elements: ").split()))
quick_sort(arr,0,len(arr)-1) 
print(*arr)
