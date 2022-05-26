#DFS
from sys import stdin

n,m = map(int,stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int,stdin.readline().strip())))
    
def solution(x,y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if graph[y][x] == 2:
        graph[y][x] = 1
        solution(x-1, y)
        solution(x, y-1)
        solution(x+1, y)
        solution(x, y+1)
    return False

result = 0
for i in range(n):
    for j in range(m):
        if solution(j,i) == 0:
            result += 1
            
print(result)