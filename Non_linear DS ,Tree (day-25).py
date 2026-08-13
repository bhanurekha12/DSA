#non linear data structures
# --trees
# --node
# --edge
# types of trees:
# 1)proper tree 
# 2)perfect tree
# 3)binary tree
# 4)skewed tree
# 5)de-gennerative trees
# 6)n-array tree
# 7)red-black tree 

#Creating a tree:
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# values=list(map(int,input("enter elements:").split()))
# nodes=[]
# for value in values:
#     nodes.append(node(value))
#     for i in range(len(nodes)):
#         left=2*i+1
#         right=2*i+2
#         if left<len(nodes):
#             nodes[i].left=nodes[left]
#         if right<len(nodes):
#             nodes[i].right=nodes[right]
# root=nodes[0]
# print("Root:",root.data)
# print("Left:",root.left.data)
# print("right:",root.right.data)
# print("Left.left:",root.left.left.data)
# print("Right.right:",root.left.right.data)

#preorder
'''class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
values=list(map(int,input("enter elements:").split()))
nodes=[]
for value in values:
    nodes.append(node(value))
    for i in range(len(nodes)):
        left=2*i+1
        right=2*i+2
        if left<len(nodes):
            nodes[i].left=nodes[left]
        if right<len(nodes):
            nodes[i].right=nodes[right]
root=nodes[0]
def preorder(root):
    if root:
        print(root.data,end=' ')
        preorder(root.left)
        preorder(root.right)
preorder(root)'''

#inorder:
'''class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
values=list(map(int,input("enter elements:").split()))
nodes=[]
for value in values:
    nodes.append(node(value))
    for i in range(len(nodes)):
        left=2*i+1
        right=2*i+2
        if left<len(nodes):
            nodes[i].left=nodes[left]
        if right<len(nodes):
            nodes[i].right=nodes[right]
root=nodes[0]
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)
inorder(root)'''

#postorder:
'''class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
values=list(map(int,input("enter elements:").split()))
nodes=[]
for value in values:
    nodes.append(node(value))
    for i in range(len(nodes)):
        left=2*i+1
        right=2*i+2
        if left<len(nodes):
            nodes[i].left=nodes[left]
        if right<len(nodes):
            nodes[i].right=nodes[right]
root=nodes[0]
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=' ')
postorder(root)'''

#vertical order traversal:
'''from collections import defaultdict,deque
class node:
    def __init__(self,data):
        self.data=data 
        self.left=None
        self.right=None
values=list(map(int,input("enter elements:").split()))
nodes=[]
for value in values:
    nodes.append(node(value))
    for i in range(len(nodes)):
        left=2*i+1
        right=2*i+2
        if left<len(nodes):
            nodes[i].left=nodes[left]
        if right<len(nodes):
            nodes[i].right=nodes[right]
root=nodes[0]
columns=defaultdict(list)
queue=deque([(root,0)])
while queue:
    node,column=queue.popleft()
    columns[column].append(node.data)
    if node.left:
        queue.append((node.left,column-1))
    if node.right:
            queue.append((node.right,column+1))
for column in sorted(columns):
    print(columns[column])'''