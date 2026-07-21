#patterns in spiral clock-wise direction:
'''n=int(input("Enter the size of matrix:"))
arr=[[0]*n for _ in range(n)]
top=0
left=0
right=n-1
bottom=n-1
num=1
while top<=bottom and left<=right:
    #in top ,left-> right
    for i in range(left, right+1):
        arr[top][i]=num
        num+=1
    top+=1
    # in right,top->bottom
    for i in range(top,bottom+1):
        arr[i][right]=num
        num+=1
    right-=1
    #in bottom, left->right
    for i in range(right, left-1,-1):
        arr[bottom][i]=num
        num+=1
    bottom-=1
    #in left, bottom to top
    for i in range(bottom, top-1,-1):
        arr[i][left]=num
        num+=1
    left+=1
for row in arr:
    print(*row)'''

