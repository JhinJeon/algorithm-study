# 듣보잡

from sys import stdin

n, m = map(int,stdin.readline().split())

dbj = []
dbjcheck = []
for k in range(n):
    dbj.append(input().rstrip()) # 듣보잡 리스트
for c in range(m):
    dbjcheck.append(input().rstrip())    #검색 리스트

result = sorted(list(set(dbj) & set(dbjcheck)))
print(len(result))
for x in result:
    print(x)

# 구글링 하니까 교재의 코드처럼 복잡하게 안 쓰는 것 같다