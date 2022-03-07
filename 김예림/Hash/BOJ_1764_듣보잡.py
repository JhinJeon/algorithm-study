import sys
N,M=map(int,sys.stdin.readline().split())
nset=set()
mset=set()
for _ in range(N):
    nset.add(sys.stdin.readline().strip())
for _ in range(M):
    mset.add(sys.stdin.readline().strip())
s3=nset&mset
answer=sorted(list(s3))
print(len(s3))
for i in answer:
    print(i)
