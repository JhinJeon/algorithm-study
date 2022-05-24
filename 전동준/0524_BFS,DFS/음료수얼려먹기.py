#DFS 알고리즘 사용
#변수 x는 그래프(얼음틀)의 가로, 변수  y는 그래프의 세로를 표현

from sys import stdin

n,m = map(int,stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int,stdin.readline().strip())))
    
def solution(y,x):
    if y <= -1 or y >= n or x <= -1 or x >= m:
        return False
    if graph[y][x] == 0:
        graph[y][x] = 1
        solution(y-1, x)
        solution(y, x-1)
        solution(y+1, x)
        solution(y, x+1)
        return True
    return False

answer = 0
for i in range(n):
    for j in range(m):
        if solution(i,j) == True:
         answer += 1
         
print(answer)