from _collections import deque
n,m=map(int,input().split())
graph=[]

for i in range(n):
    graph.append(list(map(int,input())))

def bfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    queue=deque()
    queue.append((x,y))

    if graph[x][y]==0:
        while queue:
            x,y=queue.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                    continue
                if graph[nx][ny]==0:
                    graph[nx][ny]=1
                    queue.append((nx,ny))
            return True
    return False

result=0
for i in range(n):
    for j in range(m):
        if bfs(i,j)==True:
            result+=1

print(result)