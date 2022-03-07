import sys
N,M=map(int,sys.stdin.readline().split())
treelist=list(map(int, sys.stdin.readline().split()))
start=0
end=max(treelist)
while start<=end:
    mid=(start+end)//2
    rest=0
    rest = sum(i-mid if i > mid else 0 for i in treelist)
    if rest<M:
        end=mid-1 
        
    else:
        start=mid+1
        result=mid

print(result)
