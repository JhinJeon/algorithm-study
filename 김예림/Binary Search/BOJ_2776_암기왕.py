import sys
T=int(sys.stdin.readline())

def search(i,nlist):
    pl=0
    pr=len(nlist)-1
    while pl<=pr:
        pc=(pl+pr)//2
        if nlist[pc]==i:
            return 1
        elif nlist[pc]<i:
            pl=pc+1
        else:
            pr=pc-1
    return -1

for _ in range(T):
    n=int(sys.stdin.readline())
    nlist=sorted(map(int, sys.stdin.readline().split()))
    m=int(sys.stdin.readline())
    mlist=list(map(int, sys.stdin.readline().split()))
    
    for i in mlist:
        if search(i,nlist)==1:
            print(1)
        elif search(i,nlist)==-1:
            print(0)

   #시간초과가 자꾸 떠서 pypy3으로 변경하니 맞았음.
