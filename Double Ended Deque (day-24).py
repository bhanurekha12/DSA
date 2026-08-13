#built-ins of deque:
'''from collections import deque
dq=deque()
dq.append(10)
dq.append(20)
dq.append(30)
dq.append(40)
print(dq)
dq.appendleft(0)
print(dq)
dq.pop()
print(dq)
dq.popleft()
print(dq)
dq.extend([40,50])
print(dq)
dq.extendleft([-20,-10])
print(dq)
dq.rotate(2)
print(dq)'''

#reverse double ended deque:
'''dq.remove(10)
print(dq)
print(dq.count(30))
print(dq.index(30))
dq.reverse()
print(dq)
dq.clear()
print(dq)'''

#i/p
# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft



# from collections import deque
# d=deque()
# n=int(input())
# for  _ in range(n):
#     x=input().split()
#     if x[0]=='append':
#         d.append(int(x[1]))
#     elif x[0]=='appendleft':
#         d.appendleft(int(x[1]))
#     elif x[0]=='pop':
#         d.pop()
#     elif x[0]=='popleft':
#         d.popleft()
# print(*d)
