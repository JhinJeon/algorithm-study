import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())

graph=[]

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip())))




def bfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    if graph[x][y]==0:
        queue=deque()
        queue.append((x,y))
        while queue:
            x,y=queue.pop()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
                    continue 
                if graph[nx][ny]==0:
                    graph[nx][ny]=1
                    queue.append((nx,ny))
        return True
    return



count=0
for i in range(n):
    for j in range(m):
        if bfs(i,j)==True:
            count+=1
print(count)