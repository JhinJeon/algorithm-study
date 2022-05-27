from sys import stdin

n,m = map(int,stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int,stdin.readline().strip())))
    
def solution(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0:
        return False
    if graph[x][y] != 0:
        solution(x-1, y)
        solution(x, y-1)
        solution(x+1, y)
        solution(x, y+1)
        return True
    return False

answer = 0
for i in range(n):
    for j in range(m):
        if solution(n,m) == True:
            answer += 1
            
print(answer)

            