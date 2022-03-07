import sys
import string
N,M=map(int,sys.stdin.readline().split())
memo=dict()
s=[]
for i in range(N):
    site,pw=sys.stdin.readline().split()
    memo[site]=pw
for i in range(M):
    s.append(sys.stdin.readline().rstrip())
for i in s:
    print(memo.get(i))
