#graph
'''vertices=["A","B","C","D"]
graph={}
for vertex in vertices:
    graph[vertex]=[]
n=int(input("Enter number of edges:"))
for i in range(n):
    e,v=input("Enter edge(e,v): ").split()
    graph[e].append(v)
    graph[v].append(e)
print("\n Graph")
for vertex in graph:
    print(vertex,"->",graph[vertex])'''

#weighted graph
'''vertices=["A","B","C","D"]
graph={}
for vertex in vertices:
    graph[vertex]=[]
n=int(input("Enter number of edges:"))
for i in range(n):
    e,v,w=input("Enter edge(e,v,w): ").split()
    w=int(w)
    graph[e].append((v,w))
    graph[v].append((e,w))
print("\n Graph")
for vertex in graph:
    print(vertex,"->",graph[vertex])'''

#Depth-First-Search:FIFO
'''vertices=["A","B","C","D"]
graph={}
for vertex in vertices:
    graph[vertex]=[]
n=int(input("Enter number of edges:"))
for i in range(n):
    e,v=input("Enter edge(e,v): ").split()
    graph[e].append(v)
    graph[v].append(e)
start=input("enter starting vertex: ")
visited=set()
def dfs(vertex):
    print("Visit:",  vertex)
    visited.add(vertex)
    for adj  in graph[vertex]:
        if adj not in visited:
            print(vertex,'->', adj)
            dfs(adj)
            print("Backtracking to",vertex)
print("\n DFS with BT:")
dfs(start)
print("\n graph")
for vertex in graph:
    print(vertex,"->",graph[vertex])'''

#Breadth-First-Search:LIFO
'''vertices=["A","B","C","D"]
graph={}
for vertex in vertices:
    graph[vertex]=[]
n=int(input("Enter number of edges:"))
for i in range(n):
    e,v=input("Enter edge(e,v): ").split()
    graph[e].append(v)
    graph[v].append(e)
start=input("enter starting vertex: ")
visited=set()
queue=[]
visited.add(start)
queue.append(start)
print("\n BFS traversal")
while queue:
    vertex=queue.pop(0)
    print(vertex, end=' ')
    for adj in graph[vertex]:
        if adj not in visited:
            visited.add(adj)
            queue.append(adj)  '''  

#Dijkstras algo:shortest path-where edge weight represents distance

'''vertices=input("Enter vertices:").split()
graph={}
for v in vertices:
    graph[v]=[]
n=int(input("enter number of edges: "))
for i in  range(n):
    e,v,w=input("enter edge(source,destination,distance)").split()
    w=int(w)
    graph[e].append((v,w))
    graph[v].append((e,w))
source=input("Enter source vertex: ")
destination=input("Enter destination vertex: ")
distance={}
previous={}
for v in vertices:
    distance[v]=float('inf')
    previous[v]=None
distance[source]=0
visited=set()
for i in range(len(vertices)):
    current=None
    minimum=float('inf')
    for v in vertices:
        if v not in visited and distance[v]<minimum:
            minimum=distance[v]
            current=v
    if current is None:
        break
    visited.add(current)
    for adj,weight in graph[current]:
        new_distance=distance[current]+weight
        if new_distance<distance[adj]:
            distance[adj]=new_distance
            previous[adj]=current
path=[]
current=destination
while current is not None:
    path.append(current)
    current=previous[current]
path.reverse()
if distance[destination]==float('inf'):
    print("path exists")
else:
    print("\n shortest distance: ",distance[destination])
    print("\n shortest path: ","->".join(path))'''



