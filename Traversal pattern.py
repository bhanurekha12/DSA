n=int(input("enter the size of matrix:"))
matrix=[]
print("Enter elements row wise:")
for i in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
top=0
left=0
right=n-1
bottom=n-1
num=1
while top<=bottom and left<=right:
    #in top,left->right
    for i in range(left,right+1):
        print(matrix[top][i],end=" ")
        num+=1
    top+=1
    # in right,top->bottom
    for i in range(top,bottom+1):
        print(matrix[i][right],end=' ')
        num+=1
    right-=1
    #in bottom,left->right
    for i in range(right, left-1,-1):
        print(matrix[bottom][i],end=" ")
        num+=1
    bottom-=1
    #in left,bottom to top
    for i in range(bottom,top-1,-1):
        print(matrix[i][left],end=' ')
        num+=1
    left+=1

