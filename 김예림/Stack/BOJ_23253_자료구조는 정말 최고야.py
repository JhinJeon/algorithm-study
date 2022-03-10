import sys
N,M=map(int,sys.stdin.readline().split())
check=[]
for i in range(0,M):
    t=int(sys.stdin.readline())
    num=list(map(int,sys.stdin.readline().split()))
    for j in range(0,t-1):
        if num[j+1]>num[j]: #내림차순이 아니라면 
            check.append(1)
        else:
            check.append(0)
if 1 in check:
    print("No")
else:
    print("Yes")


    
