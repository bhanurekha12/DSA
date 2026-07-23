#searching in arrays
# 1. extract the index
# 2. first occurence
# 3. last occurence
# 4. count of occurence
# 5. largest/smallest
# 6. pair search
# 7. missing number search [1,2,3,5]

#extract the index
# arr=list(map(int,input("enter the elements:").split()))
# target=int(input("enter the target:"))
# found=False
# for i in range(len(arr)):
#     if arr[i]==target:
#         print("index of target:",i)
#         found=True
#         break
# if not found:
#     print("target not found")

#first occurence

# arr=list(map(int,input("enter the elements:").split()))
# target=int(input("enter the target:"))
# for i in range(len(arr)):
#     if arr[i]==target:
#         print("first occurence of target:",i)
#         break
#     else:
#         print("target not found")

# arr=list(map(int,input("enter the elements:").split()))
# target=int(input("enter the target:"))
# index=-1
# for i in range(len(arr)):
#     if arr[i]==target:
#         index=i
#         break
# if index!=-1:
#     print("first occurence of target:",index)
# else:
#     print("target not found")

# arr=list(map(int,input("enter the elements:").split()))
# target=int(input("enter the target:"))
# count=0
# for i in range(len(arr)):
#     if arr[i]==target:
#         count+=1
#         if count==2:
#             print("second occurence of target:",i)
#             break
# if count<2:
#     print("target not found")

# arr=list(map(int,input("enter the elements:").split()))
# target=int(input("enter the target:"))
# index=-1
# count=0
# for i in range(len(arr)):
#     if arr[i]==target:
#         index=i
#         count+=1
#         if count==2:
#             print("second occurence of target:",index)
#             break
# if index!=-1:
#     print("second occurence of target:",index)
# else:
#     print("target not found")
        
#last occurence
# arr=list(map(int,input("enter the elements:").split()))
# target=int(input("enter the target:"))
# index=-1
# for i in range(len(arr)):
#     if arr[i]==target:
#         index=i
# if index!=-1:
#     print("last occurence of target:",index)
# else:
#     print("target not found")

#count of occurence
# arr=list(map(int,input("enter the elements:").split()))
# target=int(input("enter the target:"))
# count=0
# for i in range(len(arr)):
#     if arr[i]==target:
#         count+=1
#     if count==0:
#         print("target not found")
# print("count of occurence of target:",count)

#largest/smallest
# arr=list(map(int,input("enter the elements:").split()))
# max_element=arr[0]
# f=-1
# for i in range(len(arr)):
#     if arr[i]>max_element:
#         max_element=arr[i]
#         f=i
# print("largest element:",max_element)
# print("index of largest element:",f)

#smallest element
# arr=list(map(int,input("enter the elements:").split()))
# min_element=arr[0]
# f=-1
# for i in range(len(arr)):
#     if arr[i]<min_element:
#         min_element=arr[i]
#         f=i
# print("smallest element:",min_element)
# print("index of smallest element:",f)

#pair search
# arr=list(map(int,input("enter the elements:").split()))
# target_sum=int(input("enter the target sum:"))
# found=False
# for i in range(len(arr)):
#     for j in range(i+1):
#         if arr[i]+arr[j]==target_sum:
#             print("pair found is",arr[i],arr[j])
#             print("pair found at",i,j)
#             found=True
#             break
#     if found:
#         break
# if not found:
#     print("pair not found")

#missing number search
# arr=list(map(int,input("enter the elements:").split()))
# ele=arr[-1]
# s=0
# a=sum(arr)
# for i in range(ele+1):
#     s+=i
# print("missing element:",s-a)

# arr=list(map(int,input("enter the elements:").split()))
# n=len(arr)+1
# expected=n*(n+1)//2
# actual=sum(arr)
# print("missing number:",expected-actual)