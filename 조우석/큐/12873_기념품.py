
from sys import stdin
N=int(stdin.readline())
que=[i for i in range(1,N+1)]

round=0
point=0

while len(que) !=1:
    round+=1
    point+=round**3-1
    point=point%(len(que))
    que.pop(point)
print(que[0])


