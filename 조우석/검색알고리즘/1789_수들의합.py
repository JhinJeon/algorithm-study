import sys
N=int(sys.stdin.readline())
start=1
end=N
while start<=end:
    mid=(start+end)//2
    if mid*(mid+1)//2<=N: #1부터중앙까지합이 N보다작으면 
        answer=mid
        start=mid+1
    else:
        end=mid-1
print(answer) 
        
# 1 2 3 4 