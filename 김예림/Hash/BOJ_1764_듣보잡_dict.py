import sys
N,M=map(int,sys.stdin.readline().split())
D=dict()
result=[]
for i in range(N):
    D[sys.stdin.readline().rstrip()]=i
for i in range(M):
    temp=sys.stdin.readline().rstrip()
    if D.get(temp)!=None:
        result.append(temp)
result.sort()
print(len(result))
for i in result:
    print(i)

